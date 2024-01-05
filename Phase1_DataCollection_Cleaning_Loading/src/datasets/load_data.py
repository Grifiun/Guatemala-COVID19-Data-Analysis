import pandas as pd
from io import StringIO
import requests
import chardet
import tkinter as tk
from tkinter import filedialog, simpledialog

# Función para cargar y procesar el archivo local
def cargar_archivo_local():
    # Definir la ruta predeterminada del archivo local
    default_local_file_path = '/home/denilson/Downloads/municipio.csv'

    # Crear una ventana Tkinter para que el usuario seleccione el archivo local
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Solicitar la ruta del archivo local
    local_file_path = filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo local CSV",
                                                  filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))

    # Utilizar la ruta predeterminada si no se selecciona ninguna
    if not local_file_path:
        local_file_path = default_local_file_path

    # Cerrar la ventana Tkinter
    root.destroy()

    # Leer el archivo CSV local
    df_local = pd.read_csv(local_file_path)

    # Paso 1: Remover registros duplicados
    df_local = df_local.drop_duplicates()

    return df_local

# Función para cargar y procesar el archivo global
def cargar_archivo_global():
    # Solicitar la URL
    url_global = simpledialog.askstring("Input", "Introduce la URL global CSV:",
                                        initialvalue="https://seminario2.blob.core.windows.net/fase1/global.csv?sp=r&st=2023-12-06T03:45:26Z&se=2024-01-04T11:45:26Z&sv=2022-11-02&sr=b&sig=xdx7LdUOekGyBvGL%2FNE55ZZj9SBvCC%2FWegxtpSsKjJg%3D")

    # Utilizar la URL predeterminada si no se proporciona ninguna
    if not url_global:
        url_global = 'https://seminario2.blob.core.windows.net/fase1/global.csv?sp=r&st=2023-12-06T03:45:26Z&se=2024-01-04T11:45:26Z&sv=2022-11-02&sr=b&sig=xdx7LdUOekGyBvGL%2FNE55ZZj9SBvCC%2FWegxtpSsKjJg%3D'

    # Realizar la solicitud GET con manejo del encoding
    response = requests.get(url_global)
    result = chardet.detect(response.content)
    encoding = result['encoding']

    # Imprimir el encoding detectado (puede ser útil para depurar)
    print(f"Encoding detectado: {encoding}")

    # Leer el contenido de la respuesta y convertirlo a texto utilizando el encoding detectado
    content_text = response.content.decode(encoding)

    # Crear un objeto StringIO con el contenido
    data_global = StringIO(content_text)

    # Leer el archivo CSV
    df_global = pd.read_csv(data_global)

    # Guardar el DataFrame en un archivo CSV
    # df_global.to_csv('file/archivo_global.csv', index=False)

    return df_global

if __name__ == "__main__":
    # df_local = cargar_archivo_local()
    # print("DataFrame Local:")
    # print(df_local.head())

    # df_global = cargar_archivo_global()
    # print("\nDataFrame Global:")
    # print(df_global.head())
    print("")