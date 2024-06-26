# insert_data.py

import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

def insert_data():
    try:
        # Establecer conexión a la base de datos
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        
        cursor = conn.cursor()
        
        # Insertar datos en la tabla Productos
        cursor.execute("""
            INSERT INTO Productos (nombre, precio, stock)
            VALUES ('Producto A', 100.00, 50),
                   ('Producto B', 75.50, 100),
                   ('Producto C', 200.75, 25);
        """)
        
        # Insertar datos en la tabla Vendedores
        cursor.execute("""
            INSERT INTO Vendedores (nombre, region)
            VALUES ('Juan Pérez', 'Norte'),
                   ('María Gómez', 'Sur'),
                   ('Pedro López', 'Este');
        """)
        
        # Insertar datos en la tabla Ventas
        cursor.execute("""
            INSERT INTO Ventas (producto_id, vendedor_id, cantidad, fecha_venta)
            VALUES (1, 1, 10, '2024-06-25'),
                   (2, 2, 5, '2024-06-25'),
                   (3, 3, 8, '2024-06-26');
        """)
        
        # Confirmar la transacción y cerrar la conexión
        conn.commit()
        print("Datos insertados correctamente")
        
    except psycopg2.Error as e:
        print(f"Error al insertar datos: {e}")
        
    finally:
        if conn is not None:
            conn.close()
            print("Conexión cerrada")

# Ejecutar la función insert_data si este script se ejecuta directamente
if __name__ == "__main__":
    insert_data()
