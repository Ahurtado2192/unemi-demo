from flask import Blueprint, jsonify
from redis_store import redis_store

get_all_keys = Blueprint('get_all_keys', __name__)

@get_all_keys.route('/keys', methods=['GET'])
def get_keys():
    try:
        keys = redis_store.keys('*')  # Obtener todas las claves en Redis
        return jsonify({'keys': keys}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
