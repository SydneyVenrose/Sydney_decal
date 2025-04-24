import numpy as np

# Problem 1: Prime Clusters
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
    return np.array([row for row in arr if any(is_prime(x) for x in row)])

# Problem 2: Checkerboard Creation
def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2] = 1
    board[::2, 1::2] = 0
    board[1::2, ::2] = 0
    board[1::2, 1::2] = 1
    return board

def reverse_checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2] = 0
    board[::2, 1::2] = 1
    board[1::2, ::2] = 1
    board[1::2, 1::2] = 0
    return board

# Problem 3: The Expanding Universe
def expansion(arr, spaces):
    return np.array([' '.join(list(word)).replace(' ', ' ' * spaces) for word in arr])

# Problem 4: Second-Dimmest Star
def secondDimmest(stars):
    return np.sort(stars, axis=0)[1]

# Example tests (optional to run for confirmation)
if __name__ == "__main__":
    arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
    print("Contains Primes:\n", containsPrimes(arr))

    print("\nCheckerboard:\n", checkerboard())
    print("\nReverse Checkerboard:\n", reverse_checkerboard())

    universe = np.array(['galaxy', 'clusters'])
    print("\nExpansion (1 space):\n", expansion(universe, 1))
    print("Expansion (2 spaces):\n", expansion(universe, 2))

    np.random.seed(123)
    stars = np.random.randint(500, 2000, (5, 5))
    print("\nStar Matrix:\n", stars)
    print("Second Dimmest:\n", secondDimmest(stars))
