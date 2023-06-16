from tools import Grafo
from ant_colony import AntColony
V = 6
E = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)]
G = Grafo(V, E)
G.color = [0, 1, 0, 1, 0, 1]

colony = AntColony(G, 2, 10, 1, 1, 0.5, 1)
solution = colony.run(100)

for u, v in solution:
    G.remove_edge(u, v)

if G.is_bipartite():
    print("La solución encontrada es una solución aproximada al problema de eliminación de k aristas para obtener un grafo bipartito.")
else:
    print("La solución encontrada no es una solución aproximada al problema de eliminación de k aristas para obtener un grafo bipartito.")
