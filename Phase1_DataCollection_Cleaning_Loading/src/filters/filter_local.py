import pandas as pd
from ..datasets.load_data import cargar_archivo_local

class FilterDataLocal:
    def __init__(self):
        self.df_local = cargar_archivo_local()

    def is_alpha(self, value):
        return value.isalpha()

    def is_positive_integer(self, value):
        return pd.notna(value) and isinstance(value, int) and value > 0

    def is_numeric(self, value):
        if isinstance(value, (int, float)):
            return True
        return str(value).isnumeric()

    def is_alpha_numeric(self, value):
        return value.isalnum()
    
    def is_valid_date(self, value):
        try:
            pd.to_datetime(value)
            return True
        except:
            return False

    def prepare_data(self, year):
        print("Applying filters to the columns...")
        # Remove duplicates
        self.df_local = self.df_local.drop_duplicates()

        # Check and correct data
        self.df_local = self.df_local[self.df_local['departamento'].apply(lambda x: self.is_alpha(x))]
        self.df_local = self.df_local[self.df_local['municipio'].apply(lambda x: self.is_alpha(x))]
        self.df_local = self.df_local[self.df_local['codigo_departamento'].apply(lambda x: self.is_numeric(x))] # is_alpha_numeric
        self.df_local = self.df_local[self.df_local['codigo_municipio'].apply(lambda x: self.is_numeric(x))] # is_alpha_numeric
        self.df_local = self.df_local[self.df_local['poblacion'].apply(lambda x: self.is_positive_integer(x) if pd.notna(x) else False)]

        # Remove invalid columns after the first 5 columns
        valid_date_columns = [col for col in self.df_local.columns[5:] if self.is_valid_date(col)]

        # Filter by the specified year
        # self.df_local = self.df_local.drop(columns=[col for col in valid_date_columns if pd.to_datetime(col, errors='coerce').dt.year.notna().any() and pd.to_datetime(col, errors='coerce').dt.year != year])

        # Replace NaN values with 0 in all remaining date columns
        for col in valid_date_columns:
            try:
                self.df_local[col] = self.df_local[col].apply(lambda x: 0 if pd.isna(x) or not self.is_positive_integer(x) else int(x))
            except Exception as e:
                print(f"Error processing column {col}: {e}")

        # Fill empty population values with 0
        self.df_local['poblacion'] = self.df_local['poblacion'].fillna(0)

        print("Data preparation completed.")

    def prepare_data_for_insertion_dept_mun(self):
        # Select relevant columns
        relevant_columns_local = ['departamento', 'codigo_departamento', 'municipio', 'codigo_municipio', 'poblacion']
        prepared_data_dept_mun = self.df_local[relevant_columns_local].copy()

        # Rename columns to English
        prepared_data_dept_mun.columns = ['name_department', 'code_department', 'municipality', 'code_municipality', 'population']

        # Assign 'GT' to the 'code_country' column
        prepared_data_dept_mun['code_country'] = 'GT'

        print("Data insertion preparation for Municipality and Department completed.")
        return prepared_data_dept_mun
    
    def prepare_data_for_insertion_department(self):
        # Select relevant columns
        relevant_columns_local = ['codigo_departamento', 'departamento']
        prepared_data_department = self.df_local[relevant_columns_local].copy()

        # Remove duplicates
        prepared_data_department = prepared_data_department.drop_duplicates()

        # Rename columns
        prepared_data_department.columns = ['code_department', 'name_department']

        # Assign 'GT' to the 'code_country' column
        prepared_data_department['code_country'] = 'GT'

        print("Data insertion preparation for Department completed.")
        return prepared_data_department

    def prepare_data_for_insertion_municipality(self):
        # Select relevant columns
        relevant_columns_local = ['codigo_municipio', 'municipio', 'codigo_departamento', 'poblacion']
        prepared_data_municipality = self.df_local[relevant_columns_local].copy()

        # Remove duplicates
        prepared_data_municipality = prepared_data_municipality.drop_duplicates()

        # Rename columns
        prepared_data_municipality.columns = ['code_municipality', 'municipality', 'code_department', 'population']

        print("Data insertion preparation for Municipality completed.")
        return prepared_data_municipality
    
    def prepare_data_for_insertion_municipality_deaths_reported(self):
        # Select relevant columns for deaths reported
        relevant_columns_local = ['codigo_municipio'] + list(self.df_local.columns[5:])
        df_prepared_reported_deaths = self.df_local[relevant_columns_local].copy()

        # Reshape the dataframe to long format for deaths reported
        df_prepared_reported_deaths = pd.melt(df_prepared_reported_deaths, id_vars=['codigo_municipio'], var_name='date_reported', value_name='new_deaths')

        # Rename columns to English
        df_prepared_reported_deaths.columns = ['code_municipality', 'date_reported', 'new_deaths']

        # Convert 'date_reported' to datetime format
        df_prepared_reported_deaths['date_reported'] = pd.to_datetime(df_prepared_reported_deaths['date_reported'], format='%m/%d/%Y')

        print("Data insertion preparation for Deaths_reported completed.")
        return df_prepared_reported_deaths