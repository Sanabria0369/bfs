
"use client";
import { useState } from "react";

export default function Home() {
  const [inicio, setInicio] = useState("");
  const [objetivo, setObjetivo] = useState("");
  const [resultado, setResultado] = useState([]);

  const resolver = async () => {
    const res = await fetch("http://localhost:8000/solve", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        inicio: inicio.split(",").map(Number),
        objetivo: objetivo.split(",").map(Number),
      }),
    });

    const data = await res.json();
    setResultado(data.pasos || []);
  };

  return (
    <main style={{ padding: 20 }}>
      <h1>BFS Solver</h1>

      <input
        placeholder="4,2,3,1"
        value={inicio}
        onChange={(e) => setInicio(e.target.value)}
      />
      <br /><br />

      <input
        placeholder="1,2,3,4"
        value={objetivo}
        onChange={(e) => setObjetivo(e.target.value)}
      />
      <br /><br />

      <button onClick={resolver}>Resolver</button>

      <h2>Resultado:</h2>
      {resultado.map((p, i) => (
        <div key={i}>Paso {i}: [{p.join(", ")}]</div>
      ))}
    </main>
  );
}
