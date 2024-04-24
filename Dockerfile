# Usa una imagen base de Python 3.12
FROM python:3.12-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir flask Flask-SQLAlchemy psycopg2-binary flask_redis

# Expone el puerto 5000 para que Flask pueda ser accedido externamente
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]
