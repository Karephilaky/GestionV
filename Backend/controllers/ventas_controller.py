from flask import Blueprint, request, jsonify
from .config import config
from models import Venta

ventas_bp = Blueprint('ventas', __name__, url_prefix='/ventas')

@ventas_bp.route('/', methods=['GET'])
def obtener_ventas():
    try:
        conn = config()
        cursor = conn.cursor()
        cursor.execute("SELECT id, producto_id, vendedor_id, cantidad, fecha_venta FROM Ventas")
        ventas = []
        for row in cursor.fetchall():
            venta = Venta(row[0], row[1], row[2], row[3], row[4])
            ventas.append(venta.__dict__)
        cursor.close()
        conn.close()
        return jsonify(ventas), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ventas_bp.route('/agregar', methods=['POST'])
def agregar_venta():
    try:
        data = request.get_json()
        producto_id = data['producto_id']
        vendedor_id = data['vendedor_id']
        cantidad = data['cantidad']
        fecha_venta = data['fecha_venta']
        
        conn = config()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Ventas (producto_id, vendedor_id, cantidad, fecha_venta)
            VALUES (%s, %s, %s, %s)
        """, (producto_id, vendedor_id, cantidad, fecha_venta))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Venta agregada correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
