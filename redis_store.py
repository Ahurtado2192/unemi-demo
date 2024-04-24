import redis
import os

# Configuración de la conexión a Redis
redis_store = redis.StrictRedis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), decode_responses=True)
