import pandas as pd
import argparse
from src.filters.filter_global import FilterDataGlobal
from src.filters.filter_local import FilterDataLocal
from src.connections.sql_server_connection import SQLServerConnection
from src.connections.mysql_server_connection import MySQLConnection
from services.sql_query_executor import SQLQueryExecutor, generate_queries_for_cases, generate_queries_for_reported_deaths, generate_queries_for_country, generate_queries_for_department, generate_queries_for_municipality

def insert_data_to_sql_server(connection, batch_size, df_prepared_country, df_prepared_department, df_prepared_municipality, df_prepared_cases, df_prepared_reported_deaths):
    # Create SQLQueryExecutor instance
    sql_executor = SQLQueryExecutor(connection)

    # Generate queries
    queries_country = generate_queries_for_country(df_prepared_country)
    queries_department = generate_queries_for_department(df_prepared_department)
    queries_municipality = generate_queries_for_municipality(df_prepared_municipality)
    queries_cases = generate_queries_for_cases(df_prepared_cases)
    queries_reported_deaths = generate_queries_for_reported_deaths(df_prepared_reported_deaths)

    # Execute queries in batches
    sql_executor.execute_batch_insert(sql_executor, queries_country, batch_size)
    sql_executor.execute_batch_insert(sql_executor, queries_department, batch_size)
    sql_executor.execute_batch_insert(sql_executor, queries_municipality, batch_size)
    sql_executor.execute_batch_insert(sql_executor, queries_cases, batch_size)
    sql_executor.execute_batch_insert(sql_executor, queries_reported_deaths, batch_size)

    # Close connection
    connection.close()

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Process country and year for data filtering.')
    parser.add_argument('country', type=str, nargs='?', default='Guatemala', help='Country for data filtering')
    parser.add_argument('year', type=int, nargs='?', default=2020, help='Year for data filtering')
    parser.add_argument('batch_size', type=int, nargs='?', default=50, help='Number of records per batch for batched SQL inserts')
    parser.add_argument('db', type=str, nargs='?', default='SQL_Server', help='Database MySQL or SQL_Server')
    args = parser.parse_args()

    # Create instances of objects
    filter_global_instance = FilterDataGlobal()
    filter_local_instance = FilterDataLocal()
    filter_local_instance.prepare_data(args.year)
    filter_global_instance.prepare_data(args.country, args.year)

    # OG Data
    filter_local_instance.df_local.to_csv('files/archivo_local.csv', index=False)
    filter_global_instance.df_global.to_csv('files/archivo_global.csv', index=False)

    # Prepare insertion data for global data
    df_prepared_country = filter_global_instance.prepare_data_for_insertion_country()
    df_prepared_department = filter_local_instance.prepare_data_for_insertion_department()
    df_prepared_municipality = filter_local_instance.prepare_data_for_insertion_municipality()
    df_prepared_cases = filter_global_instance.prepare_data_for_insertion_cases()
    df_prepared_reported_deaths = filter_local_instance.prepare_data_for_insertion_municipality_deaths_reported()

    # Save prepared DataFrames to CSV files
    df_prepared_country.to_csv('files/prepared_country.csv', index=False)
    df_prepared_department.to_csv('files/prepared_department.csv', index=False)
    df_prepared_municipality.to_csv('files/prepared_municipality.csv', index=False)
    df_prepared_cases.to_csv('files/prepared_cases.csv', index=False)
    df_prepared_reported_deaths.to_csv('files/prepared_reported_deaths.csv', index=False)

    # Create connection to SQL Server
    db_type = args.db
    connection = None

    if db_type == 'MySQL':
        mysql_connection = MySQLConnection()
        connection = mysql_connection.get_connection()
    else:   
        sql_server_connection = SQLServerConnection()
        connection = sql_server_connection.get_connection()

    # Insert data to SQL Server
    insert_data_to_sql_server(connection, args.batch_size, df_prepared_country, df_prepared_department, df_prepared_municipality, df_prepared_cases, df_prepared_reported_deaths)
