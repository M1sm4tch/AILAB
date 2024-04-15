from queue import PriorityQueue

class PuzzleState:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0
        self.calculate_cost()

    def calculate_cost(self):
        # Manhattan distance heuristic calculation
        goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.cost = sum(
            abs(s % 3 - g % 3) + abs(s // 3 - g // 3) for s, g in
            ((self.state.index(i), goal_state.index(i)) for i in range(1, 9))
        )

    def __lt__(self, other):
        return self.cost < other.cost

def get_neighbors(state):
    neighbors = []
    zero_index = state.state.index(0)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible moves: right, down, left, up

    for dx, dy in moves:
        new_zero_index = zero_index + dx + 3 * dy
        if 0 <= new_zero_index < 9:
            new_state = state.state[:]
            new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
            neighbors.append(PuzzleState(new_state, state, (dx, dy)))
    return neighbors

def reconstruct_path(state):
    path = []
    while state.parent:
        path.append(state.move)
        state = state.parent
    return path[::-1]

def a_star(initial_state):
    open_set = PriorityQueue()
    open_set.put(initial_state)
    closed_set = set()

    while not open_set.empty():
        current_state = open_set.get()

        if current_state.state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            return reconstruct_path(current_state)

        closed_set.add(tuple(current_state.state))

        for neighbor in get_neighbors(current_state):
            if tuple(neighbor.state) not in closed_set:
                open_set.put(neighbor)

    return None  # No solution found

# Example usage:
initial_state = PuzzleState([1, 2, 3, 4, 5, 6, 7, 0, 8])
solution = a_star(initial_state)
if solution:
    print("Solution:", solution)
else:
    print("No solution found.")
