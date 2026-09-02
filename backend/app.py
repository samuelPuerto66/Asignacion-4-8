import os

import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

def conectar_db():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'servidor-bd-ejemplo'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', ''),
        database=os.environ.get('DB_NAME', 'taller_db'),
        connect_timeout=5,
    )

@app.route('/')
def inicio():
    return jsonify({"status": "ok", "mensaje": "API desplegada con CI/CD funcionando!"})

@app.route('/api')
def status():
    # Sin try/except a proposito: si la BD esta caida, PyMySQL debe
    # propagar el OperationalError para que quede visible en Dozzle (Fase 4).
    conexion = conectar_db()
    conexion.close()
    return jsonify({"status": "ok", "mensaje": "API de prueba funcionando perfectamente en Docker!", "db": "conectada"})

if __name__ == '__main__':
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
