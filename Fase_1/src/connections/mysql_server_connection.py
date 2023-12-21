import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class MySQLConnection:
    def __init__(self):
        self.host = os.getenv("MYSQL_SERVER_SERVER")
        self.user = os.getenv("MYSQL_SERVER_USERNAME")
        self.password = os.getenv("MYSQL_SERVER_PASSWORD")
        self.database = os.getenv("MYSQL_SERVER_DATABASE")
        self.port = os.getenv("MYSQL_SERVER_PORT")

    def get_connection(self):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        return connection
