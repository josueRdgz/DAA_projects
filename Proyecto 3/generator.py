import random
from tools import Grafo

class GeneradorEntradas:
    def __init__(self):
        self.num_nodos = random.random(5,10)
        self.probabilidad_arista = 0.5

    def generar_grafo(self):
        grafo = Grafo()
        for i in range(self.num_nodos):
            grafo.agregar_nodo(i)
        for i in range(self.num_nodos):
            for j in range(i+1, self.num_nodos):
                if random.random() < self.probabilidad_arista:
                    grafo.agregar_arista(i, j)
        return grafo

    def generar_k(self):
        return random.randint(1, self.num_nodos)

