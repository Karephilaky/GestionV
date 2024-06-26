import React, { useState, useEffect } from 'react';

const Productos = () => {
  const [productos, setProductos] = useState([]);
  const [nombre, setNombre] = useState('');
  const [precio, setPrecio] = useState('');
  const [stock, setStock] = useState('');

  const obtenerProductos = async () => {
    try {
      const response = await fetch('/productos/');
      const data = await response.json();
      setProductos(data);
    } catch (error) {
      console.error('Error al obtener productos:', error);
    }
  };

  const agregarProducto = async () => {
    try {
      const response = await fetch('/productos/agregar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nombre, precio, stock }),
      });
      if (response.ok) {
        console.log('Producto agregado correctamente');
        // Opcional: Limpiar campos después de agregar
        setNombre('');
        setPrecio('');
        setStock('');
        // Actualizar la lista de productos
        obtenerProductos();
      } else {
        console.error('Error al agregar producto:', response.statusText);
      }
    } catch (error) {
      console.error('Error al agregar producto:', error);
    }
  };

  useEffect(() => {
    obtenerProductos();
  }, []);

  return (
    <div>
      <h2>Gestión de Productos</h2>
      <ul>
        {productos.map(producto => (
          <li key={producto.id}>
            {producto.nombre} - Precio: {producto.precio} - Stock: {producto.stock}
          </li>
        ))}
      </ul>
      <h3>Agregar Producto</h3>
      <input type="text" value={nombre} onChange={e => setNombre(e.target.value)} placeholder="Nombre" />
      <input type="number" value={precio} onChange={e => setPrecio(e.target.value)} placeholder="Precio" />
      <input type="number" value={stock} onChange={e => setStock(e.target.value)} placeholder="Stock" />
      <button onClick={agregarProducto}>Agregar Producto</button>
    </div>
  );
};

export default Productos;
