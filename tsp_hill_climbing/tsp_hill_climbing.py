import numpy as np
import random

# Example: create a random symmetric adjacency matrix (20 cities)
np.random.seed(0)
n_cities = 20
matrix = np.random.randint(10, 100, size=(n_cities, n_cities))
matrix = (matrix + matrix.T) // 2  # symmetric
np.fill_diagonal(matrix, 0)

def random_solution(n):
    sol = list(range(n))
    random.shuffle(sol)
    return sol

def path_length(matrix, solution):
    length = 0
    for i in range(len(solution)):
        length += matrix[solution[i]][solution[i-1]]
    return length

def best_neighbor(matrix, solution):
    best = solution
    best_len = path_length(matrix, solution)
    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            val = path_length(matrix, neighbor)
            if val < best_len:
                best, best_len = neighbor, val
    return best, best_len

def hill_climbing(matrix, max_iter=500):
    current = random_solution(len(matrix))
    current_len = path_length(matrix, current)

    for _ in range(max_iter):
        neighbor, neighbor_len = best_neighbor(matrix, current)
        if neighbor_len < current_len:
            current, current_len = neighbor, neighbor_len
        else:
            break
    return current, current_len

if __name__ == "__main__":
    solution, best_len = hill_climbing(matrix, 500)
    print("Best route:", solution)
    print("Best distance:", best_len)
