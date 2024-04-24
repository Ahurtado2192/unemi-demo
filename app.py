from flask import Flask
from load_data import load_data
from delete_data import delete_data
from load_all_data import load_all_data
from get_all_keys import get_all_keys
from models import db
import os

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')  # Usar variable de entorno para la URI de la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la instancia de SQLAlchemy
db.init_app(app)

# Registro de las rutas relacionadas con los estudiantes
app.register_blueprint(load_data)
app.register_blueprint(delete_data)
app.register_blueprint(load_all_data)
app.register_blueprint(get_all_keys)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
