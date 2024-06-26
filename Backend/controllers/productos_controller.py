from flask import Blueprint, request, jsonify
from .config import config
from models import Producto

productos_bp = Blueprint('productos', __name__, url_prefix='/productos')

@productos_bp.route('/', methods=['GET'])
def obtener_productos():
    try:
        conn = config()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM Productos")
        productos = []
        for row in cursor.fetchall():
            producto = Producto(row[0], row[1], row[2], row[3])
            productos.append(producto.__dict__)
        cursor.close()
        conn.close()
        return jsonify(productos), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@productos_bp.route('/agregar', methods=['POST'])
def agregar_producto():
    try:
        data = request.get_json()
        nombre = data['nombre']
        precio = data['precio']
        stock = data['stock']
        
        conn = config()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Productos (nombre, precio, stock)
            VALUES (%s, %s, %s)
        """, (nombre, precio, stock))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Producto agregado correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
