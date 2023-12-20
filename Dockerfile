# Usa la imagen base de Alpine
FROM python:3.9-alpine

# Crea un entorno virtual y establece el PATH
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Instala las dependencias necesarias
RUN apk --no-cache add \
    unixodbc \
    unixodbc-dev \
    bash \
    wget \
    curl \
    gnupg

# Copia tu aplicación al contenedor
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Descarga e instala los controladores ODBC de SQL Server
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.10.5.1-1_amd64.apk \
    && curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.10.1.1-1_amd64.apk \
    && apk add --allow-untrusted msodbcsql17_17.10.5.1-1_amd64.apk \
    && apk add --allow-untrusted mssql-tools_17.10.1.1-1_amd64.apk \

# Comando de inicio de tu aplicación
# CMD ["python", "main.py"]
