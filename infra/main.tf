# Proveedor AWS
provider "aws" {
  region = "us-east-1"  # Cambia la región si es necesario
}

# Crear un nuevo VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = "172.31.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true

  tags = {
    Name = "my-vpc"
  }
}

# Crear un Internet Gateway y asociarlo con la VPC
resource "aws_internet_gateway" "my_igw" {
  vpc_id = aws_vpc.my_vpc.id
  tags = {
    Name = "my-igw"
  }
}

# Crear una Subnet pública
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "172.31.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
  tags = {
    Name = "public-subnet"
  }
}

# Crear una Subnet privada
resource "aws_subnet" "private_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "172.31.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = false
  tags = {
    Name = "private-subnet"
  }
}

# Crear un Security Group para RDS
resource "aws_security_group" "rds_sg" {
  name        = "rds-security-group"
  description = "Security group for RDS instance"
  vpc_id      = aws_vpc.my_vpc.id

  # Permitir acceso a MySQL (puerto 3306) desde cualquier IP
  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Permitir todo el tráfico saliente
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "rds-security-group"
  }
}

# Crear un DB Subnet Group
resource "aws_db_subnet_group" "my_db_subnet_group" {
  name        = "my-db-subnet-group"
  subnet_ids  = [aws_subnet.public_subnet.id, aws_subnet.private_subnet.id]
  description = "Subnet group for RDS instance"
}

# Crear la instancia de RDS MySQL
resource "aws_db_instance" "mydb_instance" {
  identifier            = "mydb-instance"
  engine                = "mysql"
  engine_version        = "5.7"
  instance_class        = "db.t3.micro"
  allocated_storage     = 20
  storage_type          = "gp2"
  db_subnet_group_name  = aws_db_subnet_group.my_db_subnet_group.name
  vpc_security_group_ids = [aws_security_group.rds_sg.id]
  username              = "admin"
  password              = "MySecurePassword123!"
  db_name               = "mydatabase"
  publicly_accessible   = true
  multi_az              = false
  backup_retention_period = 7
  skip_final_snapshot   = true
  tags = {
    Name = "mydb-instance"
  }
}
