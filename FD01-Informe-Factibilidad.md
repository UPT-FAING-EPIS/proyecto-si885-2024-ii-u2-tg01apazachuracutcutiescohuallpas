
<center>


![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)**

Curso: Inteligencia de Negocios

Docente: Mag. Patrick Cuadros Quiroga

Integrantes:

Escobar Rejas, Carlos Andrés (2021070016)  
Apaza Ccalle, Albert Kenyi   (2021071075)  
Cutipa Gutierrez, Ricardo    (2021069827)  
Churacutipa Blass, Erick     (2020067578)  
Churacutipa Blas, Erick     (2020067578)  
Huallpa Maron, Jesus Antonio (2021071085) 

**Tacna – Perú**

2024


**  
**
</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**Sistema *"Herramienta de Seguimiento y Evaluación del Desempeño de Red en Computadoras UPT"***

Informe de Factibilidad

Versión *{1.0}*

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|24/08/2024|Versión Original|

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# **INDICE GENERAL**

[1. Descripción del Proyecto](#_Toc52661346)

[2. Riesgos](#_Toc52661347)

[3. Análisis de la Situación actual](#_Toc52661348)

[4. Estudio de Factibilidad](#_Toc52661349)

[4.1 Factibilidad Técnica](#_Toc52661350)

[4.2 Factibilidad económica](#_Toc52661351)

[4.3 Factibilidad Operativa](#_Toc52661352)

[4.4 Factibilidad Legal](#_Toc52661353)

[4.5 Factibilidad Social](#_Toc52661354)

[4.6 Factibilidad Ambiental](#_Toc52661355)

[5. Análisis Financiero](#_Toc52661356)

[6. Conclusiones](#_Toc52661357)


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**<u>Informe de Factibilidad</u>**

1. <span id="_Toc52661346" class="anchor"></span>**Descripción del Proyecto**

1.1. Nombre del proyecto

"Herramienta de Seguimiento y Evaluación del Desempeño en Redes de Computadoras UPT"

1.2. Duración del proyecto

Empieza el 13 de agosto y termina el 13 diciembre

1.3. Descripción

El proyecto "Herramienta de Seguimiento y Evaluación del Desempeño de Red en Computadoras UPT" consiste en el desarrollo de una solución integral para monitorear y evaluar el rendimiento de la red de computadoras dentro de la Universidad Privada de Tacna (UPT). Esta herramienta está diseñada para proporcionar un análisis detallado del estado y desempeño de los recursos tecnológicos, permitiendo a los administradores de TI identificar y solucionar problemas de manera proactiva. A través de la recopilación de datos en tiempo real, la herramienta facilita la gestión eficiente del rendimiento, asegurando que la red funcione sin interrupciones. Además, incluye funciones de evaluación continua, que ayudan a realizar un seguimiento del rendimiento a lo largo del tiempo, identificar patrones de uso, y proponer mejoras basadas en datos concretos.

1.4. Objetivos

1.4.1 Objetivo general

- Desarrollar e implementar un sistema robusto que permita la recopilación y supervisión de la red en las computadoras en los laboratorios de la UPT.

1.4.2 Objetivos Específicos

   -Diseñar un script para la recolección de datos que monitorice el rendimiento de la red de cada computadora en los laboratorios.
    -Establecer un mecanismo eficiente para enviar los datos recopilados a una base de datos centralizada, asegurando un almacenamiento adecuado para su análisis posterior. 
    -Facilitar la comprensión de la información recopilada mediante la organización de datos que permitan su visualización clara y efectiva.
    -Analizar el tráfico de red en el laboratorio A para identificar las horas de mayor actividad, facilitando la optimización del uso de recursos en los laboratorios.
    -Evaluar el consumo de internet diario para establecer patrones de uso y detectar posibles congestiones en la red.
    -Identificar las direcciones IP con mayor tráfico de red, permitiendo a los administradores detectar equipos o usuarios que puedan estar consumiendo excesivos recursos.
    -Determinar los docentes que generan mayor tráfico de red, lo cual puede ayudar en la planificación de recursos y en la mejora del servicio durante las clases.
    -Establecer qué clases presentan mayor tráfico de red, proporcionando información valiosa para la gestión de recursos durante los períodos de mayor demanda.
    -Apoyar al área de soporte proporcionando información detallada a través de reportes o un dashboard interactivo, lo que permitirá una gestión más proactiva y eficiente de los recursos tecnológicos, facilitando la identificación y resolución de problemas de la red.


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

2. <span id="_Toc52661347" class="anchor"></span>**Riesgos**

    -Retrasos en el Cronograma: Los retrasos en el desarrollo, pruebas o implementación podrían afectar la fecha de finalización del proyecto, especialmente si dependen de factores externos como la disponibilidad de recursos o la integración con sistemas existentes.

    -Definición Inadecuada de Requisitos: Cambios en los requisitos durante el desarrollo podrían llevar a la necesidad de rediseñar partes del sistema, afectando el alcance y el tiempo del proyecto.  

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

3. <span id="_Toc52661348" class="anchor"></span>**Análisis de la Situación actual**

    3.1. Planteamiento del problema

      La Universidad Privada de Tacna (UPT) enfrenta desafíos significativos en la gestión del rendimiento de su red. En el entorno actual, los administradores de TI lidian con la falta de herramientas adecuadas para monitorear y evaluar el estado y desempeño de los recursos tecnológicos. La ausencia de una solución integral limita la capacidad para identificar y solucionar problemas de manera proactiva, afectando la operación eficiente de la red.

   Actualmente, la supervisión del rendimiento se realiza de manera fragmentada y manual, lo que resulta en un seguimiento inadecuado de los recursos tecnológicos. Esto genera dificultades para mantener las computadoras en un nivel óptimo de operación y para asegurar un funcionamiento continuo de la red. Además, la falta de análisis detallado y de datos en tiempo real impide una gestión efectiva del rendimiento y la identificación de patrones de uso, lo que podría llevar a problemas recurrentes no detectados a tiempo.

   Para abordar estas deficiencias, es esencial desarrollar una herramienta de seguimiento y evaluación que permita un análisis detallado y en tiempo real del desempeño de la red. Esta solución permitirá a los administradores de TI tomar decisiones informadas, identificar problemas potenciales antes de que se conviertan en fallos graves, y proponer mejoras basadas en datos concretos, optimizando así el rendimiento general de la infraestructura tecnológica de la UPT.


    3.2. Consideraciones de software

   Para el proyecto "Herramienta de Seguimiento y Evaluación del Desempeño de Red en Computadoras UPT", se utilizará Python 3.12.5 por su estabilidad y compatibilidad, y Tableau 2021.4 para visualizaciones avanzadas. Estas tecnologías, ampliamente reconocidas y estandarizadas en la industria, ofrecerán un entorno de desarrollo robusto y confiable.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

4. <span id="_Toc52661349" class="anchor"></span>**Estudio de
    Factibilidad**

    Describir los resultados que esperan alcanzar del estudio de factibilidad, las actividades que se realizaron para preparar la evaluación de factibilidad y por quien fue aprobado.

    4.1. <span id="_Toc52661350" class="anchor"></span>Factibilidad Técnica


      Infraestructura de Red:
         • Conectividad a Internet: La UPT cuenta con conectividad a internet mediante fibra óptica, ofreciendo alta velocidad y estabilidad para la transferencia de datos en tiempo real.
         • Red Física: La infraestructura de red incluye routers, switches y puntos de acceso inalámbricos distribuidos por el campus. Esta red está diseñada para soportar múltiples dispositivos conectados simultáneamente, facilitando la recolección de datos de diferentes puntos sin sobrecargar los recursos.

      Dominio y Gestión de Red:
         • Dominio Institucional: La UPT dispone de un dominio institucional que permite la administración centralizada de las aplicaciones y herramientas de monitoreo. Esto facilita la integración del sistema y su gestión a nivel de toda la red universitaria.


    4.2. <span id="_Toc52661351" class="anchor"></span>Factibilidad Económica

   El propósito del estudio de viabilidad económica, es determinar los beneficios económicos del proyecto o sistema propuesto para la organización, en contraposición con los costos.
        Como se mencionó anteriormente en el estudio de factibilidad técnica wvaluar si la institución (departamento de TI) cuenta con las herramientas necesarias para la implantación del sistema y evaluar si la propuesta requiere o no de una inversión inicial en infraestructura informática.
        Se plantearán los costos del proyecto.
        Costeo del Proyecto: Consiste en estimar los costos de los recursos Humanos, materiales o consumibles y/o máquinas) directos para completar las actividades del proyecto}.*

   Definir los siguientes costos:

      4.2.1. Costos Generales

      Los costos generales son todos los gastos realizados en accesorios y material de oficina y de uso diario, necesarios para los procesos, tales como, papeles, plumas, cartuchos de impresora, marcadores, computadora etc. Colocar tabla de costos.

   |Material|Cantidad|Costo Unitario (S/)|
   | :-: | :- | :- |
   |LAPTOP INTEL CORE I7 3.4 GHZ MONITOR 27'' RAM 16GB DISCO DURO 1TB + SSD 480GB|1|2900.00||
   |Disco de almacenamiento de seguridad (2 TB), color negro|1|262.00||
   |Cooler Laptop|1|60||
   |Total||3,222.00|


      4.2.2. Costos operativos durante el desarrollo 

      Evaluar costos necesarios para la operatividad de las actividades de la empresa durante el periodo en el que se realizara el proyecto. Los costos de operación pueden ser renta de oficina, agua, luz, teléfono, etc.

   |Concepto|Costo|
   | :-: | :- |
   |Viáticos|300.00||
   |Movilidad del equipo de trabajo|200.00||
   |Total|500.00|

      4.2.3. Costos del ambiente

      Evaluar si se cuenta con los requerimientos técnicos para la implantación del software como el dominio, infraestructura de red, acceso a internet, etc.

   |Concepto|Costo|
   | :-: | :- |
   |Servicio VPS (Nube)|350.00||
   |Software de Diagramas y Arquitectura del Proyecto|100.00|
   |Total|450.00|

      4.2.4. Costos de personal

      Aquí se incluyen los gastos generados por el recurso humano que se necesita para el desarrollo del sistema únicamente.

      No se considerará personal para la operación y funcionamiento del sistema.

      Incluir tabla que muestra los gastos correspondientes al personal.

      Indicar organización y roles. Indicar horario de trabajo del personal.

   |Rol|Personas|Salario Mensual|Horas Mensuales|
   | :-: | :- | :- | :- |
   |Desarrollador|4|1000|60|
   |Gerente de Proyecto|1|1200|60|

      4.2.5.  Costos totales del desarrollo del sistema

      {Totalizar costos y realizar resumen de costo final del proyecto y la forma de pago.

   |Concepto|Costo Total (S/)|
   | :-: | :- |
   |Costos Generales|3,222.00|
   |Costos Operativos durante el Desarrollo|500.00|
   |Costos del Ambiente|450.00|
   |Costos del Personal|6,000.00|
   |Total|10,172.00|

      4.3. <span id="_Toc52661352" class="anchor"></span>Factibilidad Operativa

      - Optimización de Recursos: La herramienta ayudará a optimizar la utilización de los recursos tecnológicos al proporcionar datos detallados sobre el uso de la red. Esta información permitirá a la universidad tomar decisiones informadas sobre el mantenimiento, la actualización o la redistribución de recursos.
     - Mejora en la Toma de Decisiones: Al disponer de información precisa y actualizada sobre el desempeño de la infraestructura tecnológica, los administradores podrán tomar decisiones basadas en datos para mejorar la eficiencia operativa y la calidad del servicio ofrecido a los estudiantes y personal académico.
     - Facilidad de Uso e Integración: La herramienta está diseñada para ser fácil de usar e integrarse con los sistemas existentes, lo que reduce la curva de aprendizaje para el personal y minimiza el impacto en las operaciones diarias.

    4.4. <span id="_Toc52661353" class="anchor"></span>Factibilidad Legal

     - Protección de Datos Personales: La recopilación y análisis de datos debe cumplir con las leyes de protección de datos personales en Perú, como la Ley de Protección de Datos Personales (Ley N° 29733). La herramienta debe garantizar que cualquier dato personal recogido sea anonimizado y utilizado exclusivamente con fines académicos y de mejora del desempeño de los equipos.
     - Licenciamiento de Software: El uso de la biblioteca Python psutil y cualquier otro software o herramienta debe estar conforme a sus respectivas licencias de uso. Se debe asegurar que no haya violación de derechos de propiedad intelectual en el desarrollo y aplicación de la herramienta.

    4.5. <span id="_Toc52661354" class="anchor"></span>Factibilidad Social 

	- Aceptación del Proyecto: La herramienta de monitoreo proporcionará beneficios claros para la comunidad universitaria al mejorar el rendimiento de las computadoras en los laboratorios, optimizando los recursos y asegurando que los equipos estén disponibles y operativos para los estudiantes y profesores. La aceptación del proyecto entre los usuarios será positiva si se comunica adecuadamente el propósito y los beneficios del proyecto.
	- Impacto en los Usuarios: Los estudiantes y docentes se beneficiarán de un entorno de aprendizaje más eficiente, con equipos que funcionan de manera óptima. Además, el personal de TI podrá responder proactivamente a problemas antes de que se conviertan en fallas significativas, lo que reducirá los tiempos de inactividad y mejorará la satisfacción del usuario.
	- Capacitación y Adaptación: Para asegurar la adopción efectiva del proyecto, se deben realizar capacitaciones para el personal de TI y otros usuarios relevantes sobre el uso de la herramienta y la interpretación de los datos generados. Esto ayudará a minimizar cualquier resistencia al cambio y facilitará una transición fluida.


    4.6. <span id="_Toc52661355" class="anchor"></span>Factibilidad Ambiental

     - Uso de Recursos: La herramienta hace uso de software basado en Python y otras herramientas digitales, lo que no requiere recursos físicos adicionales significativos que impacten negativamente en el medio ambiente. Además, la implementación se realiza en la infraestructura existente de la universidad, minimizando la necesidad de recursos adicionales.
     - Eficiencia Energética: La herramienta está diseñada para identificar patrones de uso y consumo de recursos como energía y datos, permitiendo así una optimización del consumo de energía de las computadoras. Al monitorizar el rendimiento y la eficiencia de los equipos, se pueden identificar oportunidades para reducir el consumo energético, lo que contribuye a los objetivos de sostenibilidad de la universidad.   

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# 5. Análisis Financiero

El plan financiero se ocupa del análisis de ingresos y gastos asociados a cada proyecto, desde el punto de vista del instante temporal en que se producen. Su misión fundamental es detectar situaciones financieramente inadecuadas. Se tiene que estimar financieramente el resultado del proyecto.

## 5.1. Justificación de la Inversión
La inversión en este proyecto se justifica con base en los siguientes beneficios

**Beneficios tangibles**:
- Reducción de costos operativos
- Mejora en la eficiencia del área bajo estudio
- Optimización del uso de recursos

**Beneficios intangibles**:

-Toma de decisiones más informada

## 5.1.2. Criterios de Inversión
Costo de inversión del proyecto: 10,172.00
Tasa de descuento : 9%

**Egresos** (gastos operacionales como parte del funcionamiento del software en la puesta en produccion)

|Gasto|Cantidad|Costo Unitario (S/)|
   | - | :- | :- |
   |Viáticos|1|300||
   |Movilidad del equipo de trabajo|1|200||
   |Total||3,222.00|

**Ingreso anual y beneficios del sistema**

|Gasto|Cantidad|Costo Unitario (S/)|
   | - | :- | :- |
   |Reducción en pérdidas|50%|2000||
   |Mejora del sistema|50%|2000||
   |Total||4000|

  **Flujo de caja**

  |Periodo|Ingreso|Egreso|Flujo efectivo
   | -: | :-: | :-: | :-:
   |0|||-10 172|
   |1|4000|500|3500|
   |3|4000|500|3500
   |4|4000|500|3500
   |5|4000|500|3500


### 5.1.2.1. Relación Beneficio/Costo (B/C)


B/C = 1.34

**Interpretación**: Dado que el B/C es mayor a 1 (1.34), el proyecto es financieramente viable y debería aceptarse y por cada unidad monetaria invertida, se espera obtener aproximadamente 0.34 unidades monetarias de beneficio.

### 5.1.2.2. Valor Actual Neto (VAN)


- **Tasa de descuento (r)**: 9%
- **Inversión inicial**: S/ 10,172
- **Flujos de caja proyectados**: S/ 3500 anuales por 5 años.
VAN = S/. 13,613.78 - S/ 10,172
VAN = S/. 3,441.78


**Interpretación**: El VAN es positivo (S/. 3,441.78), lo que indica que el proyecto generará un valor adicional neto sobre la inversión inicial, por lo que es viable.

### 5.1.2.3. Tasa Interna de Retorno (TIR)

TIR = 21%

**Interpretación**: Dado que la TIR (21%) es mayor que la tasa de descuento asumida (10%), el proyecto es rentable.

---
# 6. Conclusiones

El proyecto es completamente viable, dado que la infraestructura de la UPT permite su implementación sin requerir grandes inversiones adicionales, y los costos previstos son justificados por los beneficios que ofrecerá. Entre estos beneficios destacan una gestión más eficiente de los recursos tecnológicos, optimización del rendimiento de los equipos, reducción de costos operativos a largo plazo y un mantenimiento preventivo más eficaz. Además, el sistema cumple con las normativas legales, asegurando un impacto positivo en la comunidad universitaria, mejorando la calidad del servicio tecnológico, y manteniendo un impacto ambiental mínimo.
