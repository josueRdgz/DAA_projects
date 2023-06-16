import tools

def backtrack_bipartite(G, k, removed=[]):
    if G.is_bipartite():
        return removed
    if len(removed) == k:
        return None
    for u, v in G.edges():
        G.remove_edge(u, v)
        result = backtrack_bipartite(G, k-1, removed + [(u, v)])
        if result is not None:
            return result
        G.add_edge(u, v)
    return None
