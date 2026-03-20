
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Nodo:
    def __init__(self, datos, padre=None):
        self.datos = datos
        self.padre = padre

def iguales(a, b):
    return a == b

def en_lista(nodo, lista):
    return any(n.datos == nodo.datos for n in lista)

def bfs(estado_inicial, solucion):
    visitados = []
    frontera = []

    nodo_inicial = Nodo(estado_inicial)
    frontera.append(nodo_inicial)

    while frontera:
        nodo = frontera.pop(0)
        visitados.append(nodo)

        if iguales(nodo.datos, solucion):
            resultado = []
            while nodo:
                resultado.append(nodo.datos)
                nodo = nodo.padre
            return list(reversed(resultado))

        d = nodo.datos

        hijos = [
            [d[1], d[0], d[2], d[3]],
            [d[0], d[2], d[1], d[3]],
            [d[0], d[1], d[3], d[2]]
        ]

        for h in hijos:
            hijo = Nodo(h, nodo)
            if not en_lista(hijo, visitados) and not en_lista(hijo, frontera):
                frontera.append(hijo)

    return []

class RequestData(BaseModel):
    inicio: list
    objetivo: list

@app.post("/solve")
def solve(data: RequestData):
    pasos = bfs(data.inicio, data.objetivo)
    return {"pasos": pasos}
