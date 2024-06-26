# models.py

class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Vendedor:
    def __init__(self, id, nombre, region):
        self.id = id
        self.nombre = nombre
        self.region = region

class Venta:
    def __init__(self, id, producto_id, vendedor_id, cantidad, fecha_venta):
        self.id = id
        self.producto_id = producto_id
        self.vendedor_id = vendedor_id
        self.cantidad = cantidad
        self.fecha_venta = fecha_venta
