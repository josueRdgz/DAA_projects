import random

class AntColony:
    def __init__(self, G, k, num_ants, alpha, beta, evaporation_rate, Q):
        self.G = G
        self.k = k
        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.Q = Q
        self.pheromone = {(u, v): 1 for u, v in G.E}

    def run(self, max_iterations):
        best_solution = None
        for i in range(max_iterations):
            solutions = []
            for j in range(self.num_ants):
                solution = self.build_solution()
                solutions.append(solution)
                if best_solution is None or len(solution) < len(best_solution):
                    best_solution = solution
            self.update_pheromone(solutions)
        return best_solution

    def build_solution(self):
        solution = []
        visited = set()
        current_color = 0
        current_vertex = random.randint(0, self.G.V-1)
        visited.add(current_vertex)
        while len(solution) < self.k:
            neighbors = self.G.adj[current_vertex]
            valid_neighbors = [v for v in neighbors if (current_vertex, v) in self.pheromone and v not in visited]
            if not valid_neighbors:
                break
            probabilities = [self.pheromone[(current_vertex, v)]**self.alpha * (1 if self.G.color[v] == current_color else 1/self.pheromone[(current_vertex, v)]**self.beta) for v in valid_neighbors]
            total_prob = sum(probabilities)
            probabilities = [p/total_prob for p in probabilities]
            next_vertex = random.choices(valid_neighbors, probabilities)[0]
            if self.G.color[next_vertex] == current_color:
                solution.append((current_vertex, next_vertex))
            else:
                current_color = 1 - current_color
            visited.add(next_vertex)
            current_vertex = next_vertex
        return solution

    def update_pheromone(self, solutions):
        for u, v in self.G.E:
            delta_pheromone = sum(self.Q/len(solution) if (u, v) in solution or (v, u) in solution else 0 for solution in solutions)
            self.pheromone[(u, v)] = (1 - self.evaporation_rate) * self.pheromone[(u, v)] + delta_pheromone
