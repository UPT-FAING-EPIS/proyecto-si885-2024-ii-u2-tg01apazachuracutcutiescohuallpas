<center>

[comment]: <img src="./media/media/image1.png" style="width:1.088in;height:1.46256in" alt="escudo.png" />

![./media/media/image1.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)**

**Curso:** Inteligencia de Negocios

**Docente:** Mag. Patrick Cuadros Quiroga

**Integrantes:**

Escobar Rejas, Carlos Andrés (2021070016)  
Apaza Ccalle, Albert Kenyi   (2021071075)  
Cutipa Gutierrez, Ricardo    (2021069827)  
Churacutipa Blass, Erick     (2020067578)  
Huallpa Maron, Jesus Antonio (2021071085) 

**Tacna – Perú**

**2024**

</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|Apaza|ELV|ARV|24/08/2024|Versión Original|












**Sistema *"Herramienta de Seguimiento y Evaluación del Desempeño de Red en Computadoras UPT"***

**Documento de Visión**

**Versión *{1.0}***
**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


### **ÍNDICE GENERAL**

1. [Introducción](#introduccion)  
    1.1 [Propósito](#proposito)  
    1.2 [Alcance](#alcance)  
    1.3 [Definiciones, Siglas y Abreviaturas](#definiciones)  
    1.4 [Referencias](#referencias)  
    1.5 [Visión General](#vision-general)  
2. [Posicionamiento](#posicionamiento)  
    2.1 [Oportunidad de negocio](#oportunidad-de-negocio)  
    2.2 [Definición del problema](#definicion-del-problema)  
3. [Descripción de los interesados y usuarios](#descripcion-de-interesados)  
    3.1 [Resumen de los interesados](#resumen-interesados)  
    3.2 [Resumen de los usuarios](#resumen-usuarios)  
    3.3 [Entorno de usuario](#entorno-usuario)  
    3.4 [Perfiles de los interesados](#perfiles-interesados)  
    3.5 [Perfiles de los Usuarios](#perfiles-usuarios)  
    3.6 [Necesidades de los interesados y usuarios](#necesidades-interesados-usuarios)  
4. [Vista General del Producto](#vista-general-producto)  
    4.1 [Perspectiva del producto](#perspectiva-producto)  
    4.2 [Resumen de capacidades](#resumen-capacidades)  
    4.3 [Suposiciones y dependencias](#suposiciones-dependencias)  
    4.4 [Costos y precios](#costos-precios)  
    4.5 [Licenciamiento e instalación](#licenciamiento-instalacion)  
5. [Características del producto](#caracteristicas-producto)  
6. [Restricciones](#restricciones)  
7. [Rangos de calidad](#rangos-calidad)  
 

[8.	Precedencia y Prioridad](#_Toc52661353)

[9.	Otros requerimientos del producto](#_Toc52661354)

b) Estandares legales

c) Estandares de comunicación	](#_toc394513800)37

d) Estandaraes de cumplimiento de la plataforma	](#_toc394513800)42

e) Estandaraes de calidad y seguridad	](#_toc394513800)42

[CONCLUSIONES](#_Toc52661355)

[RECOMENDACIONES](#_Toc52661356)

[BIBLIOGRAFIA](#_Toc52661357)

[WEBGRAFIA](#_Toc52661358)


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**<u>Informe de Visión</u>**


## 1. Introducción <span id="introduccion" class="anchor"></span>

Este documento de visión presenta el proyecto "Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)", cuyo objetivo es mejorar la gestión y optimización de los recursos tecnológicos en los laboratorios de la Universidad Privada de Tacna. La herramienta permitirá un monitoreo continuo y análisis detallado del rendimiento de la red, proporcionando datos críticos para la toma de decisiones en la administración de la infraestructura tecnológica.

### 1.1 Propósito <span id="proposito" class="anchor"></span>

Recopilar y analizar datos de red: Obtener información detallada sobre el uso de recursos de red en los laboratorios de la universidad, con el fin de identificar patrones y áreas de mejora.

Evaluar el rendimiento de red: Identificar el consumo de internet y disponibilidad de ancho de banda para optimizar la eficiencia operativa.

Optimización de la conectividad: Proporcionar datos útiles para mejorar el soporte de red, mantenimiento preventivo y asegurar su óptimo funcionamiento.

### 1.2 Alcance <span id="alcance" class="anchor"></span>
Área de estudio: Infraestructura de red en los laboratorios de la Universidad Privada de Tacna.

Datos a recopilar: Consumo de internet (Mbps), disponibilidad de red, servicios con mayor consumo de ancho de banda.

Metodología: Utilización de un script en Python para recopilar datos de rendimiento de red, que serán almacenados y analizados para generar reportes de desempeño.

### 1.3 Definiciones, Siglas y Abreviaturas <span id="definiciones" class="anchor"></span>
- Ancho de banda: Capacidad máxima de transmisión de datos a través de una conexión de red.

- Mbps: Megabits por segundo, unidad de medida de velocidad de transferencia de datos en redes.
    
- psutil: Biblioteca de Python para la recopilación de información del sistema y el monitoreo de recursos.

### 1.4 Referencias <span id="referencias" class="anchor"></span>

- Documentación de psutil: https://psutil.readthedocs.io
    
- Guías de Python: https://docs.python.org
    
- Manual de la Universidad Privada de Tacna: Normas y permisos para el uso de laboratorios.

### 1.5 Visión General <span id="vision-general" class="anchor"></span>

- Implementación del script: El script en Python se ejecutará para capturar datos necesarios para el análisis de rendimiento de red.
  
- Análisis de datos: Evaluar los datos recopilados para identificar tendencias y problemas en la infraestructura de red.
  
- Informe de resultados: Presentar un informe detallado con los hallazgos y recomendaciones para optimizar el uso de los recursos de red.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 2. Posicionamiento <span id="posicionamiento" class="anchor"></span>

### 2.1 Oportunidad de negocio <span id="oportunidad-de-negocio" class="anchor"></span>

- Optimización de recursos de red: Mejorar la eficiencia de la infraestructura de conectividad.

- Mejora en la experiencia educativa: Asegurar una conectividad confiable y de alto rendimiento.

- Eficiencia operativa: Reducir costos asociados con problemas de conectividad.

### 2.2 Definición del problema <span id="definicion-del-problema" class="anchor"></span>

| **LA FALTA** | La ausencia de un sistema automatizado de monitoreo de red conlleva dificultades para detectar problemas de conectividad e ineficiencias en el uso de recursos de red. |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LA NECESIDAD** | La necesidad de un monitoreo continuo y detallado se vuelve crucial para asegurar la eficiencia de la infraestructura de red. |
| **EL PROBLEMA** | La falta de un sistema de monitoreo automatizado provoca una falta de visibilidad sobre el uso de recursos de red. |
| **LA SOLUCIÓN** | Implementar una herramienta de monitoreo que permita la evaluación continua del rendimiento de red, proporcionando datos y alertas. |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 3. Descripción de los interesados y usuarios <span id="descripcion-de-interesados" class="anchor"></span>

### 3.1 Resumen de los interesados <span id="resumen-interesados" class="anchor"></span>

| **Nombre**        | **Descripción** | **Responsabilidad** |
|-------------------|-----------------|---------------------|
| **Área de TI**    | Encargada de la gestión de la infraestructura de red. | Gestionar y optimizar los recursos de conectividad. |
| **Soporte Técnico** | Personal que mantiene la infraestructura de red. | Diagnosticar y resolver problemas de conectividad. |
| **Estudiantes**   | Usuarios finales de los servicios de red. | Utilizar los recursos de conectividad para actividades académicas. |
| **Administración** | Supervisión general de las operaciones de red. | Optimizar los costos operativos de la infraestructura de red. |


### 3.2 Resumen de los usuarios <span id="resumen-usuarios" class="anchor"></span>

| **Nombre**      | **Descripción** | **Responsabilidad** |
|-----------------|-----------------|---------------------|
| **Soporte Técnico** | Interactúa con todas las funcionalidades del sistema para el monitoreo, diagnóstico y resolución de problemas. | Monitorear el rendimiento de las computadoras, realizar mantenimientos preventivos y correctivos. |
| **Área de TI**  | Utiliza los reportes generados por el sistema para la planificación del mantenimiento y las actualizaciones. | Gestionar los recursos tecnológicos, planificar mantenimientos y actualizaciones. |
| **Estudiantes** | Utilizan las computadoras para realizar actividades académicas, beneficiándose de un mejor rendimiento y menos interrupciones. | Utilizar los recursos tecnológicos para actividades académicas y proyectos prácticos. |

### 3.3 Entorno de usuario <span id="entorno-usuario" class="anchor"></span>

    Los usuarios interactuarán con el sistema a través de una interfaz desarrollada en Python, diseñada para ser intuitiva y fácil de usar. El sistema será accesible desde computadoras, permitiendo la carga de datos, la generación de informes y la configuración de alertas.

### 3.4 Perfiles de los interesados <span id="perfiles-interesados" class="anchor"></span>

| **Representante** | **Descripción** | **Tipo** | **Responsabilidades** | **Criterios de éxito** |
|-------------------|-----------------|----------|-----------------------|------------------------|
| **Área de TI**    | Encargados de la administración y mantenimiento de la infraestructura tecnológica. | Administrador | Configurar usuarios, permisos, horarios y generar informes. | Gestionar con éxito las funcionalidades del sistema. |
| **Administración** | Supervisores de las operaciones generales de la universidad y la gestión presupuestaria. | Supervisor | Asegurar que los costos operativos sean optimizados y la calidad del servicio educativo se mantenga alta. | Eficiencia en la operación de la infraestructura tecnológica. |

### 3.5 Perfiles de los Usuarios <span id="perfiles-usuarios" class="anchor"></span>

| **Representante** | **Descripción** | **Tipo** | **Responsabilidades** | **Criterios de éxito** | **Implicación** |
|-------------------|-----------------|----------|-----------------------|------------------------|----------------|
| **Soporte Técnico** | Personal técnico encargado del monitoreo, diagnóstico y resolución de problemas. | Técnico | Configurar el sistema, gestionar el rendimiento de los equipos. | Eficacia en la resolución de problemas y mantenimiento de equipos. | Participación activa en la gestión diaria de los recursos tecnológicos. |
| **Estudiantes** | Usuarios finales que utilizan las computadoras para sus actividades académicas. | Usuario final | Utilizar los recursos tecnológicos para tareas académicas. | Eficiencia y efectividad en el uso de los recursos tecnológicos. | Uso regular de los equipos en sus actividades académicas. |

### 3.6 Necesidades de los interesados y usuarios

| **Nro.** | **Requerimiento Funcional** | **Descripción** | **Prioridad** | **Inquietudes** | **Solución Propuesta** |
| --- | --- | --- | --- | --- | --- |
| 1 | Autenticación segura | Los interesados y usuarios necesitan un sistema de autenticación que asegure que solo el personal autorizado pueda acceder a los datos y funciones del sistema. | Alta | Seguridad de los datos | Implementar un sistema de autenticación con contraseñas seguras y, de ser posible, autenticación de dos factores. |
| 2 | Generación de informes personalizados | Los administradores requieren la capacidad de generar informes detallados sobre el estado y el uso de la red. | Media | La personalización puede hacer que el sistema sea más complejo de usar | Proveer plantillas de informes que puedan ser personalizadas fácilmente por los usuarios. |
| 3 | Optimización del soporte técnico | Los interesados necesitan una forma de mejorar la eficiencia en el soporte técnico mediante datos precisos sobre el uso de los recursos. | Media | La cantidad de datos podría ser abrumadora | Filtrar y mostrar los datos más relevantes para el soporte técnico. |
| 4 | Interfaz intuitiva | Los usuarios finales prefieren una interfaz sencilla e intuitiva para interactuar con el sistema. | Media | Algunos usuarios podrían necesitar formación adicional | Realizar pruebas de usabilidad y ofrecer una guía de uso dentro del sistema. |
| 5 | Almacenamiento de datos | Los datos recolectados sobre el uso de la red deben almacenarse en una base de datos para análisis futuro. | Alta | Seguridad y consistencia de los datos en la base de datos | Implementar una base de datos robusta (ej. MySQL, PostgreSQL) con procedimientos de respaldo y restauración. |
| 6 | Exportación de datos para Tableau | Los administradores deben poder exportar los datos en formatos compatibles con herramientas de análisis como Tableau (ej. CSV, Excel, etc.). | Alta | Formatos incompatibles o pérdida de datos en la exportación | Proporcionar una opción para exportar los datos a formatos estándar como CSV, que puedan ser fácilmente integrados con Tableau. |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 4. Vista General del Producto <span id="vista-general-producto" class="anchor"></span>

### 4.1 Perspectiva del producto <span id="perspectiva-producto" class="anchor"></span>

El sistema de monitoreo proporcionará una solución integral para el seguimiento y evaluación del rendimiento de las computadoras de los laboratorios, facilitando la gestión proactiva de la infraestructura tecnológica.

### 4.2 Resumen de capacidades <span id="resumen-capacidades" class="anchor"></span>

| **Beneficios para el Área de TI y Soporte Técnico** | **Principales características** |
|----------------------------------------------------|---------------------------------|
| **Monitoreo continuo** | Permite el seguimiento del uso de la red, así como la identificación de posibles cuellos de botella en el uso de recursos. |
| **Alertas automáticas** | Genera notificaciones ante cualquier anomalía detectada en la red, facilitando una respuesta rápida y efectiva. |
| **Reportes detallados** | Genera informes automatizados y personalizables sobre el uso de la red, lo que permite una toma de decisiones informada. |
| **Análisis comparativo** | Posibilidad de comparar el rendimiento de la red entre distintos laboratorios para identificar cuáles presentan más problemas de conectividad. |

### 4.3 Suposiciones y dependencias <span id="suposiciones-dependencias" class="anchor"></span>

- Acceso a la infraestructura: Se asume que el Área de TI proporcionará el acceso necesario a las computadoras y la red para la implementación del sistema de monitoreo.
    
- Estabilidad del sistema: Se asume que el script de monitoreo será lo suficientemente ligero para no afectar el rendimiento normal de las computadoras.
    
- Disponibilidad de recursos: Se presupone que los recursos técnicos y humanos necesarios para el desarrollo e implementación del sistema estarán disponibles según lo planificado.

### 4.4 Costos y precios <span id="costos-precios" class="anchor"></span>

| **Concepto**  | **Costo Total (S/.)** |
|---------------|------------------------|
| **Costos Generales** | 3,222.00 |
| **Costos Operativos durante el Desarrollo** | 500.00 |
| **Costos del Ambiente** | 450.00 |
| **Costos de Personal** |  6,000.00 |
| **Total** | 10,172.00 |

### 4.5 Licenciamiento e instalación <span id="licenciamiento-instalacion" class="anchor"></span>

Licenciamiento: La herramienta se distribuirá bajo una licencia de software libre para su uso interno en la universidad.
    
Instalación: La instalación del sistema se llevará a cabo en los laboratorios de informática, con soporte técnico a cargo del Área de TI, asegurando una implementación sin contratiempos.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 5. Características del producto <span id="caracteristicas-producto" class="anchor"></span>

Monitoreo continuo: Seguimiento del consumo de red en las computadoras de los laboratorios.
    
Generación de reportes automatizados: Creación de informes personalizados sobre el estado y uso de la red, facilitando la toma de decisiones informadas.
    
Alertas automáticas: Notificaciones instantáneas en caso de detectar anomalías en la red, permitiendo una rápida intervención


## 6. Restricciones <span id="restricciones" class="anchor"></span>

Acceso limitado a la infraestructura: El proyecto dependerá del acceso proporcionado por el Área de TI, lo que podría limitar la implementación y el monitoreo completo de los equipos.
    
Recursos computacionales: El script de monitoreo debe ser lo suficientemente ligero para no afectar negativamente el rendimiento de las computadoras durante su operación.
    
Compatibilidad de software: La herramienta debe ser compatible con el entorno operativo actual de la universidad, lo que podría restringir las tecnologías y plataformas que pueden ser utilizadas.
## 7. Rangos de calidad <span id="rangos-calidad" class="anchor"></span>

Exactitud de los datos: Se requiere un nivel alto de precisión en la recopilación y procesamiento de datos para asegurar su utilidad y fiabilidad en la toma de decisiones.
    
Disponibilidad del sistema: El sistema debe estar operativo al menos un 95% del tiempo para garantizar un monitoreo continuo y confiable.
    
Usabilidad: La interfaz del sistema debe ser intuitiva y fácil de usar para los técnicos y el personal del Área de TI.
    
Escalabilidad: El sistema debe ser escalable para soportar el crecimiento de la infraestructura tecnológica de la universidad, permitiendo la incorporación de nuevos laboratorios y equipos sin comprometer el rendimiento.

## 8. Precedencia y Prioridad
    El desarrollo del sistema de monitoreo y evaluación de red debe priorizar los componentes más críticos para su correcta implementación y operación. El enfoque principal será asegurar que las funcionalidades esenciales estén disponibles en la primera fase de desarrollo, y posteriormente se añadirán características adicionales.

| **Roles**         | **Nro.** | **Requerimiento Funcional**          | **Descripción**                                                                                                      |
|-------------------|----------|--------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Administrador**  | 1        | Autenticación segura                 | Implementar un sistema de autenticación para proteger el acceso al sistema y los datos.                               |
| **Administrador**  | 2        | Almacenamiento de datos              | Almacenar los datos recolectados sobre el rendimiento de la red en una base de datos segura.                  |
| **Administrador**  | 3        | Generación de informes personalizados| Permitir a los administradores crear informes detallados sobre el rendimiento y uso de los recursos.                  |
| **Soporte Técnico**| 4        | Optimización del soporte técnico     | Usar los datos recolectados para mejorar la eficiencia del soporte técnico mediante diagnósticos rápidos.             |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 9. Otros requerimientos del producto
### a) Estándares legales
    El sistema debe cumplir con normativas de protección de datos, como la Ley N° 29733 de Perú y el GDPR en caso de datos internacionales, garantizando la privacidad de la información recolectada.

### b) Estándares de comunicación
    Se deben utilizar protocolos seguros (HTTPS, TLS) para proteger la transmisión de datos entre los clientes y el servidor, asegurando la privacidad y seguridad de la información.

### c) Estándares de cumplimiento de la plataforma
    El sistema debe ser compatible con los sistemas operativos existentes en la universidad, asegurando su correcto funcionamiento sin afectar el rendimiento de las computadoras.

### d) Estándares de calidad y seguridad
    El sistema debe garantizar la seguridad (control de acceso, encriptación) y la calidad de los datos recolectados, asegurando su precisión, integridad y disponibilidad para análisis y toma de decisiones.



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## CONCLUSIONES <span id="conclusiones" class="anchor"></span>

1. **Alertas automáticas:** Las alertas automáticas ayudarán a mantener la red optimizada y a detectar problemas de conectividad antes de que se conviertan en fallos graves, mejorando la capacidad de respuesta del personal técnico.

2. **Generación de informes detallados:** Los informes detallados permitirán realizar análisis de rendimiento sobre la red, facilitando la toma de decisiones informadas sobre cómo mejorar la infraestructura tecnológica en base a datos concretos.

3. **Optimización de recursos:** El monitoreo de los recursos de red permitirá optimizar el uso de los equipos, evitando sobrecargas y asegurando que los recursos estén siendo utilizados de manera eficiente, lo que redundará en un mejor desempeño general de la infraestructura tecnológica.

4. **Satisfacción de los usuarios finales:** Al garantizar un mejor desempeño de la red y una experiencia más estable para los usuarios (estudiantes, docentes, etc.), se incrementará la satisfacción de los usuarios finales, lo que también impactará positivamente en la percepción de la calidad del servicio educativo.

5. **Eficiencia operativa:** La recopilación de datos de manera automatizada y la generación de informes periódicos permitirán al personal administrativo tomar decisiones con base en datos y mejorar la eficiencia operativa de los laboratorios, reduciendo posibles ineficiencias o fallos en los procesos tecnológicos.


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## RECOMENDACIONES <span id="recomendaciones" class="anchor"></span>

1. **Capacitación continua:** Es crucial proporcionar capacitación continua al personal de soporte técnico y administración para garantizar que estén actualizados sobre el funcionamiento del sistema, la interpretación de los informes y la resolución de problemas detectados por el monitoreo.

2. **Evaluaciones periódicas:** Realizar revisiones periódicas del sistema para asegurarse de que se mantenga actualizado y eficiente. Esto incluye comprobar la precisión de las alertas, la fiabilidad de los informes y la capacidad de respuesta ante eventos críticos.

3. **Retroalimentación de usuarios:** Recoger feedback de los usuarios finales (estudiantes, docentes, etc.) para mejorar la funcionalidad y la usabilidad del sistema a lo largo del tiempo. Esto permitirá ajustar el sistema a las necesidades reales de los usuarios.

4. **Mejora de la interfaz de usuario:** Continuar con la mejora de la interfaz del sistema para que sea más intuitiva y fácil de usar, especialmente para el personal que no tiene experiencia técnica. La interfaz debe facilitar la toma de decisiones rápidas y claras basadas en los datos recopilados.

5. **Escalabilidad del sistema:** A medida que la universidad crezca, se deben tomar medidas para asegurar que el sistema de monitoreo sea escalable y pueda soportar un mayor número de equipos sin perder rendimiento ni fiabilidad.

