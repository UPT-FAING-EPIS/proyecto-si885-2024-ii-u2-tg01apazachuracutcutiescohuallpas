[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17040174)


# Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)

**Descripción:**  
El **Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)** tiene como objetivo supervisar en tiempo real el uso y desempeño de la red en los laboratorios de la Universidad Privada de Tacna. El sistema recopila datos sobre el consumo de ancho de banda, estabilidad de la conexión y otros aspectos relacionados con el rendimiento de la red. Esto permite identificar problemas de conectividad, optimizar el uso de los recursos de red y proporcionar soporte técnico proactivo, asegurando así un entorno educativo eficiente y libre de interrupciones.

### Integrantes

| Nombre                             | Insights Totales |
|------------------------------------|-------------------|
| Escobar Rejas, Carlos Andrés  | (2021070016) |
| Apaza Ccalle, Albert Kenyi   | (2021071075) |
| Ricardo Cutipa Gutierrez     | (2021069827) |
| Erick Churacutipa Blass     | (2020067578) |
| Jesus Huallpa Maron          | (2021071085) |




```markdown
# Inventario de Archivos y Carpetas

## **Carpeta Raíz**
### Archivos Principales
1. **`data/`**  
   - Carpeta que contiene los archivos de datos en formato CSV.
2. **`G02_UPTRED.pbix`**  
   - Archivo de Power BI para el análisis y visualización de datos.
3. **`lambda_function.zip`**  
   - Archivo comprimido que contiene el código necesario para la función Lambda.
     - `s3bucket.py`: Script para subir datos al bucket de S3.
     - `datos_combinados.csv`: Archivo combinado generado a partir de los datos en `data`.
4. **`requirements.txt`**  
   - Archivo con las dependencias necesarias para ejecutar los scripts relacionados.
5. **`s3bucket.py`**  
   - Script Python para subir datos al bucket S3.
6. **`sqlcsv.py`**  
   - Script Python que toma los archivos CSV en la carpeta `data` y genera el archivo `datos_combinados.csv`.

---

## **Carpeta PruebasExpo**
### Archivos y Aplicaciones
1. **`APPs3uploaddata.exe`**  
   - Aplicación desarrollada en Python para subir archivos CSV al bucket S3.
2. **`final data prueba.csv`**  
   - Archivo CSV de prueba para insertar datos durante la demostración.
3. **`s3uploaddata.py`**  
   - Código fuente de la aplicación **`APPs3uploaddata.exe`**.

---

### **Estructura General**

```
/
├── data/
│   ├── [Archivos CSV...]
├── G02_UPTRED.pbix
├── lambda_function.zip
│   ├── s3bucket.py
│   ├── datos_combinados.csv
├── requirements.txt
├── s3bucket.py
├── sqlcsv.py
├── PruebasExpo/
│   ├── APPs3uploaddata.exe
│   ├── final data prueba.csv
│   ├── s3uploaddata.py
```

### **Notas**
- **`data/`**: Asegúrate de que esta carpeta contiene los archivos CSV necesarios antes de ejecutar `sqlcsv.py`.
- **`APPs3uploaddata.exe`**: Es una versión compilada de Python y debe ser probada antes de la exposición.
- **`final data prueba.csv`**: Archivo dedicado a las pruebas de inserción durante la exposición.
- **`s3bucket.py` y `sqlcsv.py`**: Los scripts deben ser configurados adecuadamente con las credenciales y configuraciones del bucket S3.
```


```markdown
# EJECUCIÓN DE AUTOMATIZACIÓN DE RECURSOS
### Primero eliminar recursos existentes y volver a armarlo:

1. Tener los archivos de artefactos (en tu entorno de trabajo local descargando el repositorio):
   - `sqlcsv.py`
   - `s3bucket.py`
   - `requirements.txt`
   - `lambda_function.zip` (este es el `datos_combinados.csv` con `s3bucket.py` generado)
   - `datos_combinados.csv`
   - La carpeta `data` con los SQL que transformaremos a CSV.

2. Debemos ubicarnos donde está `cd infra` y tener:
   - `main.tf` y `terraform.tfstate` (el `tfstate` se saca del repositorio. En tal caso, si da error, borrar manualmente desde la consola).

3. Eliminar los recursos existentes de AWS:
   ```bash
   aws s3 rm s3://netuptinteligencianegocios --recursive
   aws glue delete-crawler --name netuptinteligencianegocios-crawler
   ```

4. Destruir la infraestructura con Terraform:
   ```bash
   terraform destroy --auto-approve
   ```

5. Ejecutar el workflow (esperar a que se creen las tablas).

---

# CONTROLADOR ODBC CONFIGURACIÓN

6. Descargar ODBC: [Amazon Athena ODBC Driver v2.0.3.0](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.3.0/Windows/AmazonAthenaODBC-2.0.3.0.msi)

7. Buscar en Windows "ODBC" (hay dos resultados: 32 bits y 64 bits, selecciona el controlador de **64 bits**).

8. Agregar el controlador Amazon Athena:
   - **Data Source Name**: `athena-in`
   - **Description**: `athena-in in power bi`
   - **Region**: `us-east-1`
   - **Catalog**: `AwsDataCatalog`
   - **Database**: `default`
   - **Workgroup**: `primary`
   - **S3 Output**: `s3://netuptinteligencianegocios/athena-output/`
   - **Authentication Options**: `DEFAULT CREDENTIALS` (Recuerda tener tus credenciales configuradas: `Access ID` y `Token`).

9. Ejecutar el test:
   - **Resultado esperado**:
     ```
     Successfully connected to: Athena engine version 3
     Region: us-east-1
     Catalog: AwsDataCatalog
     Workgroup: primary
     Auth Type: Default Credentials
     ```

---

# CARGAR DATOS EN POWER BI

10. Abrir Power BI y obtener datos de otro origen.

11. Buscar y seleccionar **Amazon Athena**.

12. En el campo **DSN** colocar: `athena-in` y presionar **OK**. Los datos deberían cargar automáticamente.

13. Expandir **AwsDataCatalog** → Expandir la tabla `tb_...` → Seleccionar la tabla deseada → Hacer clic en el botón verde de **Cargar**.

   **Nota**: Si aparece un error relacionado con un paréntesis en 3 filas, simplemente bórralo, ya que no afecta al proceso de carga de datos.
```
