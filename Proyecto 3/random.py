import random

def random_edge_deletion_bipartite(G, k):
    
    bipartite_G = {0: set(), 1: set()}
    num_deleted_edges = 0
    
    while num_deleted_edges < k:
        
        u, v = random.choice(list(G.edges()))
        
        if u in bipartite_G[0] and v in bipartite_G[0] or u in bipartite_G[1] and v in bipartite_G[1]:
            G.remove_edge(u, v)
            num_deleted_edges += 1
            
        elif u in bipartite_G[0] and v in bipartite_G[1] or u in bipartite_G[1] and v in bipartite_G[0]:
            bipartite_G[0].add(u)
            bipartite_G[1].add(v)
            
    return bipartite_G
