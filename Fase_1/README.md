# SS2_Proyecto_Fase_1

## Descripción del Proyecto
Este proyecto es parte del curso ofrecido por la Universidad de San Carlos de Guatemala en la Facultad de Ingeniería, específicamente en la Escuela de Ciencias y Sistemas. Está supervisado por el Ing. Marlon Orellana y cuenta con la asistencia del Aux. Erick Villatoro en el Laboratorio de Seminario de Sistemas 2.

## Proceso de Limpieza de Datos
El proceso de limpieza de datos es crucial para garantizar la calidad y la integridad de la información utilizada en el proyecto. A continuación, se describen algunos de los pasos clave seguidos en el proceso de limpieza de datos:

### 1. Extracción de Datos
Los datos se obtuvieron desde [fuente de datos] (el cual se provee comon un enlace) y se cargaron en el proyecto para su análisis.

### 2. Limpieza y Transformación

En el proceso de limpieza y transformación de los datos, se aplicaron diversos filtros y transformaciones utilizando el script `main.py`. A continuación, se describen algunos de los filtros clave aplicados en la limpieza de datos:

- **Eliminación de Duplicados:** Se eliminaron registros duplicados en los conjuntos de datos para garantizar la integridad y consistencia de la información.

- **Manejo de Fechas:** Se aplicaron transformaciones en las fechas para asegurar la uniformidad y consistencia en el formato. En caso de fechas incorrectas o formatos inválidos, se realizaron correcciones o se eliminaron las filas correspondientes.

- **Filtros Específicos para Country y Year:** Se implementaron filtros específicos para el país y el año seleccionados, asegurando que los datos sean relevantes para el análisis.

- **Ajustes en Columnas Numéricas:** Se realizaron ajustes en las columnas numéricas para llenar los valores nulos con ceros y asegurar que los datos sean del tipo correcto (enteros). Además, se aplicaron filtros para garantizar que los valores numéricos sean positivos.

### 3. Preparación de Datasets

Se generaron varios datasets independientes para cada tabla del modelo de datos. Estos datasets se utilizaron en el proceso de inserción de datos en la base de datos. A continuación, se detallan los datasets generados y los pasos específicos de preparación para algunas de las tablas:

- **Dataset para la Tabla "Country":** Se preparó un dataset que incluye las columnas `name_country` y `code_country`. Se eliminaron duplicados y se ajustaron los nombres de las columnas para que coincidan con el esquema de la base de datos.

```python
# Ejemplo de código para generar el dataset de Country
 df_prepared_country = filter_global_instance.prepare_data_for_insertion_country()
```

- **Dataset para la Tabla "Cases":** Se creó un dataset que incluye las columnas `name_country`, `code_country`, `date_reported`, `new_cases`, `cumulative_cases`, `new_deaths` y `cumulative_deaths`. Se aplicaron filtros y transformaciones específicos para garantizar la consistencia y relevancia de los datos.

```python
# Ejemplo de código para generar el dataset de Cases
 df_prepared_cases = filter_global_instance.prepare_data_for_insertion_cases()
```

Estos son ejemplos simplificados y basados en la estructura del código proporcionado. Puedes adaptar y expandir estos ejemplos según las necesidades específicas de tu proyecto.
## Modelo de Datos

El modelo de datos implementado en este proyecto refleja una estructura relacional que permite organizar la información de manera coherente. A continuación, se describen las principales tablas que componen el modelo:

### Tablas Principales

#### 1. "Country"

- **Atributos:**
  - `code_country` (Clave primaria): Código único que identifica a un país.
  - `name_country`: Nombre del país.

#### 2. "Department"

- **Atributos:**
  - `code_department` (Clave primaria): Código único para identificar un departamento.
  - `name_department`: Nombre del departamento.
  - `code_country` (Clave foránea): Relación con la tabla "Country" mediante el código de país.

#### 3. "Municipality"

- **Atributos:**
  - `code_municipality` (Clave primaria): Código único para identificar un municipio.
  - `population`: Población del municipio.
  - `municipality`: Nombre del municipio.
  - `code_department` (Clave foránea): Relación con la tabla "Department" mediante el código de departamento.

#### 4. "Cases"

- **Atributos:**
  - `code_country` (Clave foránea): Relación con la tabla "Country" mediante el código de país.
  - `date_reported`: Fecha de reporte.
  - `new_cases`: Nuevos casos reportados.
  - `cumulative_cases`: Total acumulado de casos.
  - `new_deaths`: Nuevas muertes reportadas.
  - `cumulative_deaths`: Total acumulado de muertes.

#### 5. "MunicipalityDeathsReported"

- **Atributos:**
  - `code_municipality` (Clave foránea): Relación con la tabla "Municipality" mediante el código de municipio.
  - `date_reported`: Fecha de reporte.
  - `new_deaths`: Nuevas muertes reportadas en el municipio.

### Relaciones

- La tabla "Country" está relacionada con la tabla "Department" mediante el código de país.
- La tabla "Department" está relacionada con la tabla "Municipality" mediante el código de departamento.
- La tabla "Cases" está relacionada con las tablas "Country" y "Municipality" mediante los códigos de país y municipio, respectivamente.
- La tabla "MunicipalityDeathsReported" está relacionada con la tabla "Municipality" mediante el código de municipio.

Este modelo de datos proporciona una estructura organizada y coherente que facilita la representación de la información relacionada con casos, muertes, países, departamentos y municipios. Para una visualización más detallada, consulta el archivo `ER_SS2.png` en la carpeta de documentación del proyecto.
![Diagrama ER](documentation/ER_SS2.png)

### Ejecución del Modelo
La ejecución del modelo se lleva a cabo mediante el script `main.py`, que utiliza la clase `SQLQueryExecutor` para ejecutar consultas SQL y la clase `SQLServerConnection` para establecer la conexión con la base de datos.

## Instrucciones de Ejecución
Si alguien más quiere ejecutar este proyecto, a continuación se presentan las instrucciones básicas:

1. Clonar este repositorio.
2. Instalar las dependencias necesarias.
3. Configurar las variables de entorno en un archivo `.env`.
4. Ejecutar el script `main.py`.

## Contribuciones
Las contribuciones a este proyecto son bienvenidas. Si desea contribuir, abra un problema o envíe una solicitud de extracción.

