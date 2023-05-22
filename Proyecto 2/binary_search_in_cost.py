def find_min_cost(n, edges):
    # edges is a list of tuples (u, v, w) representing an edge
    # from u to v with weight w
    max_weight = max(w for _, _, w in edges)
    lo, hi = 0, max_weight
    while lo < hi:
        mid = (lo + hi) // 2
        if is_reachable(n, edges, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def is_reachable(n, edges, cost):
    # We invert the edges that have a weight less than or equal to cost
    new_edges = []
    for u, v, w in edges:
        if w > cost:
            new_edges.append((u, v))
        else:
            new_edges.append((u, v))
            new_edges.append((v, u))
    # We create a directed graph with inverted edges
    graph = [[] for _ in range(n+1)]
    for u, v in new_edges:
        graph[v].append((v, u))
    # We check if there is at least one node that can be reached
    # from any other node with minimal cost
    for i in range(1, n+1):
        visited = [False] * (n+1)
        dfs(i, graph, visited)
        if all(visited[1:]):
            return True
    return False


def dfs(u, graph, visited):
    visited[u] = True
    for _, w in graph[u]:
        if not visited[w]:
            dfs(w, graph, visited)


# nodes start at 1
# n = 4
# edges = [(1, 2, 2), (4, 1, 4), (4, 3, 3), (1, 3, 5)]
# print(find_min_cost(n, edges))
