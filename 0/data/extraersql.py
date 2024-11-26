import os
import re
import time
from table import create_connection  # Importar la función desde table.py
import mysql

file_directory = './data'

if not os.path.exists(file_directory):
    print(f"La carpeta {file_directory} no se encuentra.")
else:
    print(f"Carpeta {file_directory} encontrada.")

sql_files = ['trafico_red_db.sql', 'trafico_red_db2.sql', 'trafico_red_db3.sql']

output_file = os.path.join(file_directory, 'combined_trafico_red_db.sql')

id_counter = 1000

try:
    connection = create_connection()
    cursor = connection.cursor()

    with open(output_file, 'w', encoding='utf-8') as output_f:
        for sql_file in sql_files:
            file_path = os.path.join(file_directory, sql_file)

            print(f"Verificando archivo: {file_path}")

            if not os.path.exists(file_path):
                print(f"El archivo {file_path} no se encuentra. Se omite este archivo.")
                continue 

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    sql_query = f.read()

                sql_query = sql_query.replace("INSERT INTO", "INSERT IGNORE INTO")

                sql_query = '\n'.join(
                    line for line in sql_query.splitlines() if not line.strip().startswith('/*!') and not line.strip().startswith('SET')
                )

                def replace_id_with_counter(match, counter):
                    values_part = match.group(1)
                    values_list = values_part.strip('()').split(',')
                    
                    values_list[0] = str(counter)
                    counter += 1
                    return f"VALUES ({','.join(values_list)})", counter

                
                def replace_ids_and_update_counter(sql_query, counter):
                    result_query = sql_query
                    for match in re.finditer(r"VALUES \(([^)]+)\)", sql_query):
                        new_values, counter = replace_id_with_counter(match, counter)
                        result_query = result_query.replace(match.group(0), new_values, 1)
                    return result_query, counter

                sql_query, id_counter = replace_ids_and_update_counter(sql_query, id_counter)

                output_f.write(sql_query + "\n\n")

                print(f"El archivo {sql_file} se procesó correctamente.")

                start_time = time.time()
                rows_inserted = 0
                time_limit = 60
                stop_logging = False

                for statement in sql_query.split(';'):
                    statement = statement.strip()
                    if statement:
                        try:
                            # Mostrar la sentencia SQL antes de ejecutarla
                            print(f"Ejecutando sentencia: {statement[:100]}...") 
                            cursor.execute(statement)
                            rows_inserted += 1
                            
                            # Mostrar el contenido de la fila insertada
                            print(f"Fila insertada: {statement}")

                            # Controlar el log cada 0.5 segundos
                            if time.time() - start_time < time_limit and not stop_logging:
                                print(f"Fila {rows_inserted} insertada.")
                                time.sleep(1)

                            if time.time() - start_time >= time_limit:
                                stop_logging = True

                        except mysql.connector.Error as err:
                            print(f"Error ejecutando la sentencia: {err}")

                # Confirmar la transacción
                connection.commit()
                print(f"Las consultas del archivo {sql_file} se han insertado correctamente en la base de datos.")

            except Exception as e:
                print(f"Error al procesar el archivo {sql_file}: {e}")

    print(f"Los archivos SQL se han combinado y modificado correctamente en: {output_file}")

except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
finally:
    # Cerrar la conexión
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión a la base de datos cerrada.")
