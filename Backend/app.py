from flask import Flask
from flask_cors import CORS
from controllers.productos_controller import productos_bp
from controllers.vendedores_controller import vendedores_bp
from controllers.ventas_controller import ventas_bp

app = Flask(__name__)
CORS(app)  # Agregar esta línea para permitir CORS
app.register_blueprint(productos_bp)
app.register_blueprint(vendedores_bp)
app.register_blueprint(ventas_bp)

if __name__ == '__main__':
    app.run(debug=True)
