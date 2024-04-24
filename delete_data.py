from flask import Blueprint, jsonify
from redis_store import redis_store

delete_data = Blueprint('delete_data', __name__)

# Ruta para eliminar un registro de Redis por su ID
@delete_data.route('/students/delete/<string:id>', methods=['DELETE'])
def delete_student(id):
    if redis_store.exists(id):
        redis_store.delete(id)
        return jsonify({'message': 'Student deleted successfully from Redis'})
    else:
        return jsonify({'message': 'Student not found in Redis'}), 404
