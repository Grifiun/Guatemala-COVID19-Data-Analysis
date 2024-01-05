import pypyodbc 

class SQLQueryExecutor:
    def __init__(self, connection):
        self.connection = connection

    def execute_query(self, query):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
            print("Query executed successfully.")
        except Exception as e:
            print(f"Error during query execution: {e}")
            self.connection.rollback()

    def execute_batch_insert(self, table_name, batch_queries, batch_size, max_retries=2):
        total_queries = len(batch_queries)
        success_report = []
        failure_report = []

        for i in range(0, total_queries, batch_size):
            batch = batch_queries[i:i + batch_size]
            retries = 0
            init = i
            end = min(i + batch_size, total_queries)  # Asegura que end no supere el total de queries
            formatted_table_name = f"{table_name:<20}"  # Alinea a la izquierda con un ancho de 20 caracteres

            while retries <= max_retries:
                try:
                    with self.connection.cursor() as cursor:
                        try:
                            cursor.execute("BEGIN TRANSACTION;")
                            for query in batch:
                                cursor.execute(query)
                            self.connection.commit()
                            cursor.execute("COMMIT;")
                            success_message = f"TABLE: {formatted_table_name} from {init:<5} to {end:<5}: successful"
                            success_report.append(success_message)
                            print(success_message)
                            break  # Salir del bucle de reintentos si el lote tiene éxito
                        except Exception as batch_error:
                            print(f"Error during batch insert: {batch_error}")
                            self.connection.rollback()
                            cursor.execute("ROLLBACK;")
                            retries += 1
                            if retries <= max_retries:
                                failure_message = f"TABLE: {formatted_table_name} from {init:<5} to {end:<5}  {retries}/{max_retries} : failure"
                                failure_report.append(failure_message)
                                print(failure_message)
                            else:
                                failure_message = f"TABLE: {formatted_table_name} from {init:<5} to {end:<5}  {retries}/{max_retries}: failure"
                                failure_report.append(failure_message)
                                print(failure_message)
                                break
                except Exception as e:
                    print(f"Error starting transaction: {e}")
                    self.connection.rollback()
                    retries += 1
                    if retries <= max_retries:
                        print(f"Retrying transaction start (Attempt {retries}/{max_retries})")
                    else:
                        failure_message = f"TABLE: {formatted_table_name} from {init:<5} to {end:<5} Max retries reached, SKIP BATCH : failure"
                        failure_report.append(failure_message)
                        print(failure_message)
                        break

        return success_report, failure_report

def generate_queries_for_department(df):
    queries = []
    # Ajusta esta lógica según tu estructura de DataFrame
    unique_rows = df[['code_department', 'name_department', 'code_country']].drop_duplicates()
    for index, row in unique_rows.iterrows():
        query = f"INSERT INTO Department (code_department, name_department, code_country) VALUES ('{row['code_department']}', '{row['name_department']}', '{row['code_country']}')"
        queries.append(query)
    return queries

def generate_queries_for_municipality(df):
    queries = []
    # Ajusta esta lógica según tu estructura de DataFrame
    unique_rows = df[['code_municipality', 'population', 'municipality', 'code_department']].drop_duplicates()
    for index, row in unique_rows.iterrows():
        query = f"INSERT INTO Municipality (code_municipality, population, municipality, code_department) VALUES ('{row['code_municipality']}', {row['population']}, '{row['municipality']}', '{row['code_department']}')"
        queries.append(query)
    return queries

def generate_queries_for_country(df):
    queries = []
    # Ajusta esta lógica según tu estructura de DataFrame
    unique_rows = df[['code_country', 'name_country']].drop_duplicates()
    for index, row in unique_rows.iterrows():
        query = f"INSERT INTO Country (code_country, name_country) VALUES ('{row['code_country']}', '{row['name_country']}')"
        queries.append(query)
    return queries

def generate_queries_for_cases(df):
    queries = []
    # Ajusta esta lógica según tu estructura de DataFrame
    for index, row in df.iterrows():
        query = f"INSERT INTO Cases (code_country, date_reported, new_cases, cumulative_cases, new_deaths, cumulative_deaths) VALUES ('{row['code_country']}', '{row['date_reported']}', {row['new_cases']}, {row['cumulative_cases']}, {row['new_deaths']}, {row['cumulative_deaths']})"
        queries.append(query)
    return queries

def generate_queries_for_reported_deaths(df):
    queries = []
    # Ajusta esta lógica según tu estructura de DataFrame
    for index, row in df.iterrows():
        query = f"INSERT INTO MunicipalityDeathsReported (code_municipality, date_reported, new_deaths) VALUES ('{row['code_municipality']}', '{row['date_reported']}', {row['new_deaths']})"
        queries.append(query)
    return queries

def generate_queries_for_table(df, table_name):
    queries = []

    if table_name == "Country":
        queries = generate_queries_for_country(df)
    elif table_name == "Department":
        queries = generate_queries_for_department(df)
    elif table_name == "Municipality":
        queries = generate_queries_for_municipality(df)
    elif table_name == "Cases":
        queries = generate_queries_for_cases(df)
    elif table_name == "MunicipalityDeathsReported":
        queries = generate_queries_for_reported_deaths(df)

    return queries