# SS2_DataAnalysis
Data Analysis Phase 2
# University of San Carlos of Guatemala
## Faculty of Engineering
### Engineering in Computer Science and Systems.
##### Denilson Florentín de León Aguilar

## OBJECTIVES

### General Objective

The main objective of Phase 2 is to perform a comprehensive data analysis of the information collected by the Ministry of Health during the Covid-19 pandemic in Guatemala. This includes understanding the data analysis process, utilizing previously processed data stored in the SQL database, and applying Python programming language and Pandas library knowledge for data analysis. Additionally, students will apply their knowledge of data science and data analysis.

## PROBLEM

As an external consultant, you have been hired to conduct a study of the data collected by the Ministry of Health during the Covid-19 pandemic in Guatemala. The data, obtained through daily tabulation throughout the year 2020, has been collected and stored in an SQL database by the data engineer. Your task as a data analyst is to perform an analysis based on this information.

## DATA ACQUISITION

As a data analyst, you must be able to obtain the data that your colleagues have processed through an ETL process. Currently, this data is in an SQL database; therefore, you need to retrieve this data using Pandas.

## UNIVARIABLE EDA

### Quantitative Data

Perform a univariate analysis of the number of new deaths, cumulative deaths, and population of municipalities. The analysis should display count statistics, unique values, mean, standard deviation, minimum, maximum, and quartiles. Additionally, create a histogram and a box plot for each of the mentioned variables.

### Qualitative Data

Perform a univariate analysis of municipalities and departments. Only bar charts for record counts should be created for this analysis.

## TRANSFORMATIONS

If skewness or incorrect scaling is identified in the data, necessary transformations must be performed to proceed with multivariable EDA.

## MULTIVARIABLE EDA

### Quantitative Data

Create scatter plots between the variables: number of new deaths, cumulative deaths, and population of municipalities.

### Qualitative Data

Create bar charts, heat maps, and any other suitable graphs to compare municipalities and departments with quantitative variables. Specifically:
- Municipalities vs. number of new deaths
- Departments vs. number of new deaths
- Municipalities vs. population
- Departments vs. population
- Municipalities vs. cumulative deaths
- Departments vs. cumulative deaths

Insights and observations obtained from each analysis should be considered for further steps. At the end of the analysis, derive three relevant conclusions for decision-making. The entire process should be executed using the Pandas library. While the use of matplotlib and seaborn libraries for visualization is recommended, it is not mandatory.
