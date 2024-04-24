from flask import Blueprint, jsonify
from models import Student, db
from redis_store import redis_store
import os


load_all_data = Blueprint('load_all_data', __name__)

@load_all_data.route('/studentsLoad', methods=['POST'])
def load_students():
        # Si la solicitud es vacía, cargar todos los datos de la base de datos a Redis
        try:
            students = Student.query.all()
            for student in students:
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
                redis_store.hmset(student.id, student_info)
                redis_store.expire(student.id, int(os.getenv('REDIS_EXPIRATION')))  
            # Usar variable de entorno para el tiempo de vida
            return jsonify({'message': 'All data loaded from database to Redis'}), 201
        except Exception as e:
            return jsonify({'message': str(e)}), 500
