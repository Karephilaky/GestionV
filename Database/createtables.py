import psycopg2
from psycopg2 import sql
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

# Configuración de la conexión a la base de datos
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT
)

try:
    # Crear un cursor para ejecutar operaciones SQL
    cursor = conn.cursor()

    # Script SQL para crear las tablas
    create_tables_sql = """
        CREATE TABLE IF NOT EXISTS Productos (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            precio NUMERIC(10, 2) NOT NULL,
            stock INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Vendedores (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            region VARCHAR(50) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Ventas (
            id SERIAL PRIMARY KEY,
            producto_id INTEGER REFERENCES Productos(id),
            vendedor_id INTEGER REFERENCES Vendedores(id),
            cantidad INTEGER NOT NULL,
            fecha_venta DATE NOT NULL
        );
    """

    # Ejecutar el script SQL
    cursor.execute(create_tables_sql)
    conn.commit()

    print("Tablas creadas correctamente.")

except psycopg2.Error as e:
    print(f"Error al crear las tablas: {e}")

finally:
    # Cerrar el cursor y la conexión
    if cursor is not None:
        cursor.close()

    if conn is not None:
        conn.close()

    print("Conexión cerrada.")
