import pypyodbc # as odbc
from dotenv import load_dotenv
import os

load_dotenv()

class SQLServerConnection:
    def __init__(self):
        self.server = os.getenv("SQL_SERVER_SERVER")
        self.database = os.getenv("SQL_SERVER_DATABASE")
        self.username = os.getenv("SQL_SERVER_USERNAME")
        self.password = os.getenv("SQL_SERVER_PASSWORD")
        self.port = os.getenv("SQL_SERVER_PORT")

    # f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    def get_connection(self):
        try:          
                    
            trusted_connection = 'yes'  # Utiliza 'yes' para Windows Authentication
            driver = '{SQL Server}'                   
            # Cadena de conexión para Windows Authentication
            connection_string = f'DRIVER={driver};SERVER={self.server};DATABASE={self.database};Trusted_Connection={trusted_connection}'
            connection = pypyodbc.connect(connection_string)
            return connection
        except Exception as e:
            print(f"Error de conexión: {str(e)}")
            return None
         
        connection_string = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={self.server},{self.port};"
            f"DATABASE={self.database};"
            #f"UID={self.username};"
            #f"PWD={self.password};"
            f"Trust_Connection=YES;"
        )
        return odbc.connect(connection_string)
