def find_min_cost(n, m, edges):
    # edges es una lista de tuplas (u, v, w) que representan una arista de u a v con peso w
    max_weight = max(w for _, _, w in edges)
    lo, hi = 0, max_weight
    while lo < hi:
        mid = (lo + hi) // 2
        if is_reachable(n, m, edges, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

def is_reachable(n, m, edges, cost):
    # Invertimos las aristas que tienen un peso menor o igual a cost
    new_edges = [(u, v, w if w > cost else -w) for u, v, w in edges]
    # Creamos un grafo dirigido con las aristas invertidas
    graph = [[] for _ in range(n + 1)]
    for u, v, w in new_edges:
        graph[u].append((v, w))
    # Verificamos si hay al menos un nodo al que sea posible llegar desde cualquier otro nodo con costo mínimo
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        dfs(i, graph, visited)
        if not all(visited[1:]):
            return False
    return True

def dfs(u, graph, visited):
    visited[u] = True
    for v, w in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited)
            
n = 4
m = 4
edges = [(0, 1, 2), (3, 2, 3), (3, 0,4), (0, 2, 5)]
print(find_min_cost(n,m,edges))
