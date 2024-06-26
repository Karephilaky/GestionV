import React, { useState, useEffect } from 'react';

const Vendedores = () => {
  const [vendedores, setVendedores] = useState([]);
  const [nombre, setNombre] = useState('');
  const [region, setRegion] = useState('');

  const obtenerVendedores = async () => {
    try {
      const response = await fetch('/vendedores/');
      const data = await response.json();
      setVendedores(data);
    } catch (error) {
      console.error('Error al obtener vendedores:', error);
    }
  };

  const agregarVendedor = async () => {
    try {
      const response = await fetch('/vendedores/agregar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nombre, region }),
      });
      if (response.ok) {
        console.log('Vendedor agregado correctamente');
        // Opcional: Limpiar campos después de agregar
        setNombre('');
        setRegion('');
        // Actualizar la lista de vendedores
        obtenerVendedores();
      } else {
        console.error('Error al agregar vendedor:', response.statusText);
      }
    } catch (error) {
      console.error('Error al agregar vendedor:', error);
    }
  };

  useEffect(() => {
    obtenerVendedores();
  }, []);

  return (
    <div>
      <h2>Gestión de Vendedores</h2>
      <ul>
        {vendedores.map(vendedor => (
          <li key={vendedor.id}>
            {vendedor.nombre} - Región: {vendedor.region}
          </li>
        ))}
      </ul>
      <h3>Agregar Vendedor</h3>
      <input type="text" value={nombre} onChange={e => setNombre(e.target.value)} placeholder="Nombre" />
      <input type="text" value={region} onChange={e => setRegion(e.target.value)} placeholder="Región" />
      <button onClick={agregarVendedor}>Agregar Vendedor</button>
    </div>
  );
};

export default Vendedores;
