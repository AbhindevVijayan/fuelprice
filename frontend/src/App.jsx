import { useState } from "react";
import RouteForm from "./components/RouteForm";
import FuelResult from "./components/FuelResult";
import "./App.css";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="app">
      <h1>⛽ Fuel Planner</h1>

      <RouteForm setResult={setResult} />

      <FuelResult result={result} />
    </div>
  );
}

export default App;