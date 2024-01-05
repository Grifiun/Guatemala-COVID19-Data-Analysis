# University of San Carlos of Guatemala
## Faculty of Engineering
### Engineering in Computer Science and Systems.
##### Denilson Florentín de León Aguilar

## Project Description
This project is part of the course offered by the University of San Carlos de Guatemala in the Faculty of Engineering, specifically in the School of Computer Science and Systems. It is supervised by Engineer Marlon Orellana and assisted by Assistant Erick Villatoro in Systems Seminar 2 Laboratory.

## Data Cleaning Process
The data cleaning process is crucial to ensure the quality and integrity of the information used in the project. Below are some key steps followed in the data cleaning process:

### 1. Data Extraction
The data was obtained from [data source] (provided as a link) and loaded into the project for analysis.

### 2. Cleaning and Transformation

In the process of cleaning and transforming the data, various filters and transformations were applied using the `main.py` script. Here are some key filters applied in data cleaning:

- **Duplicate Removal:** Duplicate records were removed from the datasets to ensure data integrity and consistency.

- **Date Handling:** Transformations were applied to dates to ensure uniformity and consistency in the format. Incorrect dates or invalid formats were corrected or corresponding rows were removed.

- **Specific Filters for Country and Year:** Specific filters were implemented for the selected country and year, ensuring that the data is relevant for analysis.

- **Adjustments in Numeric Columns:** Adjustments were made in numeric columns to fill null values with zeros and ensure that the data is of the correct type (integers). Filters were also applied to ensure that numeric values are positive.

### 3. Dataset Preparation

Several independent datasets were generated for each table in the data model. These datasets were used in the process of inserting data into the database. Below are the generated datasets and specific preparation steps for some tables:

- **Dataset for the "Country" Table:** A dataset was prepared that includes the columns `name_country` and `code_country`. Duplicates were removed, and column names were adjusted to match the database schema.

```python
# Example code to generate the Country dataset
df_prepared_country = filter_global_instance.prepare_data_for_insertion_country()
```

- **Dataset for the "Cases" Table:** A dataset was created that includes the columns `name_country`, `code_country`, `date_reported`, `new_cases`, `cumulative_cases`, `new_deaths`, and `cumulative_deaths`. Specific filters and transformations were applied to ensure data consistency and relevance.

```python
# Example code to generate the Cases dataset
df_prepared_cases = filter_global_instance.prepare_data_for_insertion_cases()
```

These are simplified examples based on the structure of the provided code. You can adapt and expand these examples according to the specific needs of your project.

## Data Model

The data model implemented in this project reflects a relational structure that allows for the organized representation of information. Below are the main tables that make up the model:

### Main Tables

#### 1. "Country"

- **Attributes:**
  - `code_country` (Primary key): Unique code identifying a country.
  - `name_country`: Name of the country.

#### 2. "Department"

- **Attributes:**
  - `code_department` (Primary key): Unique code to identify a department.
  - `name_department`: Name of the department.
  - `code_country` (Foreign key): Relationship with the "Country" table through the country code.

#### 3. "Municipality"

- **Attributes:**
  - `code_municipality` (Primary key): Unique code to identify a municipality.
  - `population`: Population of the municipality.
  - `municipality`: Name of the municipality.
  - `code_department` (Foreign key): Relationship with the "Department" table through the department code.

#### 4. "Cases"

- **Attributes:**
  - `code_country` (Foreign key): Relationship with the "Country" table through the country code.
  - `date_reported`: Report date.
  - `new_cases`: Newly reported cases.
  - `cumulative_cases`: Cumulative total of cases.
  - `new_deaths`: Newly reported deaths.
  - `cumulative_deaths`: Cumulative total of deaths.

#### 5. "MunicipalityDeathsReported"

- **Attributes:**
  - `code_municipality` (Foreign key): Relationship with the "Municipality" table through the municipality code.
  - `date_reported`: Report date.
  - `new_deaths`: Newly reported deaths in the municipality.

### Relationships

- The "Country" table is related to the "Department" table through the country code.
- The "Department" table is related to the "Municipality" table through the department code.
- The "Cases" table is related to the "Country" and "Municipality" tables through the country and municipality codes, respectively.
- The "MunicipalityDeathsReported" table is related to the "Municipality" table through the municipality code.

This data model provides an organized and coherent structure that facilitates the representation of information related to cases, deaths, countries, departments, and municipalities. For a more detailed visualization, refer to the `ER_SS2.png` file in the project's documentation folder.
![ER Diagram](documentation/ER_SS2.png)

### Model Execution
The execution of the model is carried out using the `main.py` script, which uses the `SQLQueryExecutor` class to execute SQL queries and the `SQLServerConnection` class to establish a connection with the database.

## Execution Instructions
If someone else wants to run this project, the basic instructions are as follows:

1. Clone this repository.
2. Install the necessary dependencies.
3. Set up environment variables in a `.env` file.
4. Run the `main.py` script.

## Contributions
Contributions to this project are welcome. If you want to contribute, open an issue, or submit a pull request.