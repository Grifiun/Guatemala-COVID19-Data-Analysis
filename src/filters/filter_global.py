import pandas as pd
from ..datasets.load_data import cargar_archivo_global

class FilterDataGlobal:
    def __init__(self):
        self.df_global = cargar_archivo_global()

    def is_positive_integer(self, value):
        return pd.notna(value) and isinstance(value, int) and value > 0

    def prepare_data(self, country, year):
        # Remove duplicates
        self.df_global = self.df_global.drop_duplicates()

        # Filter by country
        self.df_global = self.df_global[self.df_global['Country'] == country]

        # Drop unnecessary column
        self.df_global = self.df_global.drop(columns=['WHO_region'])

        # Filter by year and handle incorrect date formats
        try:
            self.df_global['Date_reported'] = pd.to_datetime(self.df_global['Date_reported'], format='%m/%d/%Y')
        except (ValueError, TypeError) as e:
            # Handle invalid or missing date formats
            print(f"Error converting date: {e}")
            self.df_global = self.df_global[~self.df_global['Date_reported'].str.contains(r'\D')]  # Remove rows with non-numeric characters in the date

        # Remove rows with NaN dates
        self.df_global = self.df_global.dropna(subset=['Date_reported'])

        # Filter by year
        self.df_global = self.df_global[self.df_global['Date_reported'].dt.year == int(year)]

        # Sort by date
        self.df_global = self.df_global.sort_values(by='Date_reported')

        # Fill NaN values and convert to integers, applying is_positive_integer filter
        numeric_columns = ['New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']
        for col in numeric_columns:
            try:
                self.df_global[col] = self.df_global[col].fillna(0).astype(int).apply(lambda x: 0 if not self.is_positive_integer(x) else x)
            except Exception as e:
                print(f"Error processing column {col}: {e}")

        print(f'Filters added to {country} and year {year}')

    def prepare_data_for_insertion_country(self):
        # Select relevant columns
        relevant_columns_global = ['Country', 'Country_code']
        df_prepared_country = self.df_global[relevant_columns_global].copy()

        # Remove duplicates
        df_prepared_country = df_prepared_country.drop_duplicates()

        # Rename columns to match database schema
        df_prepared_country.columns = ['code_country', 'name_country']

        print("Data insertion preparation for Country completed.")
        return df_prepared_country

    def prepare_data_for_insertion_cases(self):
        # Select relevant columns
        relevant_columns_global = ['Country', 'Country_code', 'Date_reported', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']
        df_prepared_cases = self.df_global[relevant_columns_global].copy()

        # Rename columns to match database schema
        df_prepared_cases.columns = ['name_country','code_country', 'date_reported', 'new_cases', 'cumulative_cases', 'new_deaths', 'cumulative_deaths']

        # Remove duplicates
        df_prepared_cases = df_prepared_cases.drop_duplicates()

        print("Data insertion preparation for Cases completed")
        return df_prepared_cases
