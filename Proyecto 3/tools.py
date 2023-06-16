class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos[nodo] = set()

    def agregar_arista(self, nodo1, nodo2):
        self.agregar_nodo(nodo1)
        self.agregar_nodo(nodo2)
        self.nodos[nodo1].add(nodo2)
        self.nodos[nodo2].add(nodo1)

    def eliminar_nodo(self, nodo):
        if nodo in self.nodos:
            vecinos = self.nodos[nodo]
            del self.nodos[nodo]
            for vecino in vecinos:
                self.nodos[vecino].remove(nodo)

    def eliminar_arista(self, nodo1, nodo2):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.nodos[nodo1].remove(nodo2)
            self.nodos[nodo2].remove(nodo1)

    def obtener_nodos(self):
        return list(self.nodos.keys())

    def obtener_vecinos(self, nodo):
        if nodo in self.nodos:
            return list(self.nodos[nodo])
        else:
            return []
        
    def is_bipartite(self):
        color = [-1] * self.V
        for v in range(self.V):
            if color[v] == -1:
                color[v] = 0
                queue = [v]
                while queue:
                    u = queue.pop(0)
                    for v in self.adj[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            return False
        return True


    def __str__(self):
        return str(self.nodos)
