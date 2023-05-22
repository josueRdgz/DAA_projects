import random
import binary_search_in_cost
import binary_search_in_edges

n = random.randint(3, 10)
m = random.randint(3, n * (n - 1) / 2)
edges = []

for _ in range(m):
    start = random.randint(0, n - 1)
    end = random.randint(0, n - 1)
    w = random.randint(0, 50)
    if end == start:
        continue
    edges.append((start, end, w))

print(edges)
print(binary_search_in_cost.find_min_cost(n, edges))
print(binary_search_in_edges.find_min_cost(n, edges))
