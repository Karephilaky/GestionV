from flask import Blueprint, request, jsonify
from .config import config
from models import Vendedor

vendedores_bp = Blueprint('vendedores', __name__, url_prefix='/vendedores')

@vendedores_bp.route('/', methods=['GET'])
def obtener_vendedores():
    try:
        conn = config()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, region FROM Vendedores")
        vendedores = []
        for row in cursor.fetchall():
            vendedor = Vendedor(row[0], row[1], row[2])
            vendedores.append(vendedor.__dict__)
        cursor.close()
        conn.close()
        return jsonify(vendedores), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@vendedores_bp.route('/agregar', methods=['POST'])
def agregar_vendedor():
    try:
        data = request.get_json()
        nombre = data['nombre']
        region = data['region']
        
        conn = config()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Vendedores (nombre, region)
            VALUES (%s, %s)
        """, (nombre, region))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Vendedor agregado correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

