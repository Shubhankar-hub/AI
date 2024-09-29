from collections import deque

# Define the goal state
goal_state = [
    [0, 2, 3],
    [1, 5, 6],
    [4, 7, 8]
]

# Define the possible moves (up, down, left, right)
moves = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

# Check if the current state is the goal state
def is_goal(state):
    return state == goal_state

# Find the position of the empty space (0) in the puzzle
def find_empty(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate the possible states from the current state by moving the empty space
def generate_states(state):
    empty_i, empty_j = find_empty(state)
    new_states = []

    for move in moves:
        new_i = empty_i + move[0]
        new_j = empty_j + move[1]

        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]  # Create a copy of the current state
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            new_states.append(new_state)

    return new_states

# BFS algorithm to solve the 8-puzzle
def bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(map(tuple, current_state)))

        if is_goal(current_state):
            return path

        for next_state in generate_states(current_state):
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# Function to print the state
def print_state(state):
    for row in state:
        print(row)
    print()

# Define the initial state
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

# Solve the puzzle
solution = bfs(initial_state)

# Print the solution
if solution:
    print("Solution found:")
    for state in solution:
        print_state(state)
else:
    print("No solution found")
