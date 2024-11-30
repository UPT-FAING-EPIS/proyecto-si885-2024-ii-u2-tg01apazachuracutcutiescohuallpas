provider "aws" { 
  region = "us-east-1"
}

# Crear un bucket S3 con replicación global y versionado
resource "aws_s3_bucket" "s3_bucket" {
  bucket = "netuptinteligencianegocios"
  
  versioning {
    enabled = true
  }

  replication_configuration {
    role = aws_iam_role.lab_role.arn
    rules = [
      {
        id     = "replicate-to-eu"
        status = "Enabled"
        destination {
          bucket        = "arn:aws:s3:::netuptinteligencianegocios-eu"
          storage_class = "INTELLIGENT_TIERING"
        }
      },
      {
        id     = "replicate-to-ap"
        status = "Enabled"
        destination {
          bucket        = "arn:aws:s3:::netuptinteligencianegocios-ap"
          storage_class = "INTELLIGENT_TIERING"
        }
      }
    ]
  }

  logging {
    target_bucket = "arn:aws:s3:::netuptinteligencianegocios-logs"
    target_prefix = "access-logs/"
  }

  tags = {
    Name = "S3 Bucket Inteligencia Negocios (Costoso)"
  }
}

# Crear un bucket para logs
resource "aws_s3_bucket" "log_bucket" {
  bucket = "netuptinteligencianegocios-logs"
  acl    = "log-delivery-write"
  tags = {
    Name = "S3 Bucket Logs"
  }
}

# Crear la base de datos en AWS Glue Data Catalog
resource "aws_glue_catalog_database" "albertapaza_database" {
  name        = "tb_redupt_database"
  description = "Base de datos para almacenar tablas de inteligencia de negocios"
}

# Crear un Crawler de AWS Glue
resource "aws_glue_crawler" "netuptinteligencianegocios_crawler" {
  name          = "netuptinteligencianegocios-crawler"
  role          = "arn:aws:iam::571600849867:role/LabRole"  # Usar el rol existente
  database_name = aws_glue_catalog_database.albertapaza_database.name

  s3_target {
    path = "s3://netuptinteligencianegocios/netuptinteligencianegocios/"
  }

  recrawl_policy {
    recrawl_behavior = "CRAWL_EVERYTHING"
  }

  schema_change_policy {
    update_behavior = "UPDATE_IN_DATABASE"
    delete_behavior = "DEPRECATE_IN_DATABASE"
  }

  tags = {
    Name = "Glue Crawler Inteligencia Negocios"
  }

  depends_on = [aws_s3_bucket.s3_bucket]
}

# Crear el rol IAM LabRole
resource "aws_iam_role" "lab_role" {
  name               = "LabRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = ["glue.amazonaws.com", "lambda.amazonaws.com", "s3.amazonaws.com"]
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# Crear las políticas necesarias para el LabRole
resource "aws_iam_policy" "in_rol_policy" {
  name        = "InRol"
  description = "Política que otorga permisos globales a todas las acciones en todos los recursos"
  policy      = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow"
        Action   = "*"
        Resource = "*"
      }
    ]
  })
}

# Asociar la política al rol LabRole
resource "aws_iam_role_policy_attachment" "in_rol_policy_attachment" {
  role       = aws_iam_role.lab_role.name
  policy_arn = aws_iam_policy.in_rol_policy.arn
}

# Crear la función Lambda con máxima memoria y timeout
resource "aws_lambda_function" "s3_upload_lambda" {
  filename         = "../artefactos/lambda_function.zip"
  function_name    = "s3-upload-function-costosa"
  role             = aws_iam_role.lab_role.arn
  handler          = "s3bucket.lambda_handler"
  runtime          = "python3.8"
  timeout          = 900             # 15 minutos
  memory_size      = 10240           # 10 GB
  source_code_hash = filebase64sha256("../artefactos/lambda_function.zip")

  environment {
    variables = {
      BUCKET_NAME = "netuptinteligencianegocios"
    }
  }
}

# Crear un evento en S3 para activar la función Lambda frecuentemente
resource "aws_s3_bucket_notification" "s3_event_to_lambda" {
  bucket = aws_s3_bucket.s3_bucket.bucket

  lambda_function {
    events             = ["s3:ObjectCreated:*", "s3:ObjectRemoved:*"]
    lambda_function_arn = aws_lambda_function.s3_upload_lambda.arn
  }

  depends_on = [aws_lambda_function.s3_upload_lambda]
}

# Dar permiso a S3 para invocar la función Lambda
resource "aws_lambda_permission" "allow_s3_to_invoke_lambda" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.s3_upload_lambda.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.s3_bucket.arn
}
