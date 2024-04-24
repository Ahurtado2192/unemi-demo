from flask import Blueprint, jsonify
from models import Student, db
from redis_store import redis_store
import os

load_data = Blueprint('load_data', __name__)

# Ruta para obtener un alumno por su ID
@load_data.route('/students/<string:id>', methods=['GET'])
def get_student(id):
    # Consultar Redis
    if redis_store.exists(id):
        student_info = redis_store.hgetall(id)
        return jsonify(student_info)
    else:
        # Consultar en la base de datos
        student = Student.query.get(id)
        if student:
            student_info = {
                'id': student.id,
                'name': student.name,
                'last_name': student.last_name,
                'age': student.age,
                'phone': student.phone,
                'address': student.address,
                'career': student.career,
                'is_active': student.is_active
            }
            # Almacenar en Redis con expiración en segundos
            redis_store.hmset(id, student_info)
            redis_store.expire(id, int(os.getenv('REDIS_EXPIRATION')))  # Usar variable de entorno para el tiempo de vida
            return jsonify(student_info)
        else:
            return jsonify({'message': 'Student not found'}), 404
