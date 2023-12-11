import pandas as pd
import numpy as np
from io import StringIO
import requests
import chardet
# Import to MySQL
import mysql.connector
import argparse
# Import to SQL Server
# import pyodbc

from src.filters.filter_global import FilterDataGlobal
from src.filters.filter_local import FilterDataLocal

# Uso
if __name__ == "__main__":
    # Parse command lines arguments
    parser = argparse.ArgumentParser(description='Process country and year for data filtering.')
    parser.add_argument('country', type=str, nargs='?', default='Guatemala', help='Country for data filtering')
    parser.add_argument('year', type=int, nargs='?', default=2020, help='Year for data filtering')
    args = parser.parse_args()

    # create instances of objects
    filter_global_instance = FilterDataGlobal()
    filter_local_instance = FilterDataLocal()

    # OG Data
    # df_global.to_csv('file/archivo_global.csv', index=False)
    filter_local_instance.df_local.to_csv('files/archivo_local.csv', index=False)
    filter_global_instance.df_global.to_csv('files/archivo_global.csv', index=False)

    # Prepare data local and global data
    filter_local_instance.prepare_data()
    filter_global_instance.prepare_data(args.country, args.year)

    # Prepare insertion data for Local Data
    prepared_data_dept_mun = filter_local_instance.prepare_data_for_insertion_dept_mun()
    prepared_data_dept_mun.to_csv('files/local_prepared_insertion_dept_mun.csv', index=False)

    df_prepared_reported_deaths = filter_local_instance.prepare_data_for_insertion_municipality_deaths_reported()
    df_prepared_reported_deaths.to_csv('files/local_prepared_insertion_mun_dr.csv', index=False)

    # prepare insertion data for global data
    df_prepared_cases = filter_global_instance.prepare_data_for_insertion_cases()
    df_prepared_cases.to_csv(f'files/prepared_data_global_{args.country}_cases.csv', index=False)