import random
from tools import Grafo
class GeneradorEntradas:
    def __init__(self, num_nodos, probabilidad_arista):
        self.num_nodos = num_nodos
        self.probabilidad_arista = probabilidad_arista

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

# Ejemplo de uso
random.random(5,10)
generador = GeneradorEntradas(10, 0.5)
grafo = generador.generar_grafo()
k = generador.generar_k()
print(grafo)
print(k)
