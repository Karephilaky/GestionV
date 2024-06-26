import React, { useState, useEffect } from 'react';

const Ventas = () => {
  const [ventas, setVentas] = useState([]);
  const [productoId, setProductoId] = useState('');
  const [vendedorId, setVendedorId] = useState('');
  const [cantidad, setCantidad] = useState('');
  const [fechaVenta, setFechaVenta] = useState('');

  const obtenerVentas = async () => {
    try {
      const response = await fetch('/ventas/');
      const data = await response.json();
      setVentas(data);
    } catch (error) {
      console.error('Error al obtener ventas:', error);
    }
  };

  const agregarVenta = async () => {
    try {
      const response = await fetch('/ventas/agregar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ producto_id: productoId, vendedor_id: vendedorId, cantidad, fecha_venta: fechaVenta }),
      });
      if (response.ok) {
        console.log('Venta agregada correctamente');
        // Opcional: Limpiar campos después de agregar
        setProductoId('');
        setVendedorId('');
        setCantidad('');
        setFechaVenta('');
        // Actualizar la lista de ventas
        obtenerVentas();
      } else {
        console.error('Error al agregar venta:', response.statusText);
      }
    } catch (error) {
      console.error('Error al agregar venta:', error);
    }
  };

  useEffect(() => {
    obtenerVentas();
  }, []);

  return (
    <div>
      <h2>Gestión de Ventas</h2>
      <ul>
        {ventas.map(venta => (
          <li key={venta.id}>
            Producto ID: {venta.producto_id} - Vendedor ID: {venta.vendedor_id} - Cantidad: {venta.cantidad} - Fecha de Venta: {venta.fecha_venta}
          </li>
        ))}
      </ul>
      <h3>Agregar Venta</h3>
      <input type="text" value={productoId} onChange={e => setProductoId(e.target.value)} placeholder="Producto ID" />
      <input type="text" value={vendedorId} onChange={e => setVendedorId(e.target.value)} placeholder="Vendedor ID" />
      <input type="number" value={cantidad} onChange={e => setCantidad(e.target.value)} placeholder="Cantidad" />
      <input type="date" value={fechaVenta} onChange={e => setFechaVenta(e.target.value)} placeholder="Fecha de Venta" />
      <button onClick={agregarVenta}>Agregar Venta</button>
    </div>
  );
};

export default Ventas;
