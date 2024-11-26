import mysql.connector
import os
from mysql.connector import Error

try:
    # Configuración de conexión con variables de entorno
    connection = mysql.connector.connect(
        host=os.environ['DB_ENDPOINT'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        port=int(os.environ['DB_PORT'])
    )

    if connection.is_connected():
        print("Conexión exitosa al RDS MySQL")
        db_info = connection.get_server_info()
        print(f"Versión del servidor MySQL: {db_info}")

        # Crear un cursor para ejecutar las consultas SQL
        cursor = connection.cursor()

        # Seleccionar la base de datos 'mydatabase'
        cursor.execute("USE mydatabase;")

        # Crear la tabla 'trafico_red'
        create_table_query = """
        CREATE TABLE IF NOT EXISTS `trafico_red` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `fecha` date NOT NULL,
          `ip` varchar(255) NOT NULL,
          `clase` varchar(255) NOT NULL,
          `horario` varchar(255) NOT NULL,
          `dia` varchar(255) NOT NULL,
          `turno` varchar(255) NOT NULL,
          `laboratorio` varchar(255) NOT NULL,
          `total_enviado_mb` decimal(10,2) NOT NULL,
          `total_recibido_mb` decimal(10,2) NOT NULL,
          `tema` varchar(255) NOT NULL,
          `navegador` varchar(255) NOT NULL,
          `seccion` varchar(255) NOT NULL,
          `docente` varchar(255) NOT NULL,
          `total_mbps` decimal(20,6) DEFAULT NULL,
          `total_GB` decimal(20,6) DEFAULT NULL,
          `tiempo_sesion` time DEFAULT NULL,
          `consumo_energia_kwh` decimal(20,6) DEFAULT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=691 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """

        # Crear los procedimientos almacenados sin DELIMITER
        create_procedure_convertir_a_gb = """
        CREATE PROCEDURE `CONVERTIR A GB`()
        BEGIN
           UPDATE trafico_red
            SET total_GB = ROUND(total_mbps / 1024, 2);
        END;
        """
        
        create_procedure_sumar_total = """
        CREATE PROCEDURE `SUMAR TOTAL`()
        BEGIN
        UPDATE trafico_red
        SET total_mbps = ROUND(total_enviado_mb + total_recibido_mb, 2);
        END;
        """

        # Ejecutar las consultas
        cursor.execute(create_table_query)
        cursor.execute(create_procedure_convertir_a_gb)
        cursor.execute(create_procedure_sumar_total)

        # Confirmar los cambios
        connection.commit()

        print("Las tablas y procedimientos se han creado correctamente")

except Error as e:
    print(f"Error al conectar con la base de datos: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexión cerrada")
