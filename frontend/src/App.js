import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'; // Archivo de estilos por defecto
import Productos from './components/Productos'; // Asegúrate de importar los componentes existentes
import Vendedores from './components/Vendedores';
import Ventas from './components/Ventas';

function App() {
  return (
    <Router>
      <div className="App">
        <nav>
          <ul>
            <li>
              <a href="/">Inicio</a>
            </li>
            <li>
              <a href="/productos">Productos</a>
            </li>
            <li>
              <a href="/vendedores">Vendedores</a>
            </li>
            <li>
              <a href="/ventas">Ventas</a>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/productos" element={<Productos />} />
          <Route path="/vendedores" element={<Vendedores />} />
          <Route path="/ventas" element={<Ventas />} />
        </Routes>
      </div>
    </Router>
  );
}

// Componente Home (si prefieres tenerlo como componente separado)
const Home = () => (
  <div>
    <h2>Bienvenido a la Aplicación de Gestión</h2>
    <p>Seleccione una opción:</p>
  </div>
);

export default App;
