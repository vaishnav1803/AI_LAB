def find_blank(state):
    """Finds the index of the blank space (0) in the puzzle."""
    return state.index(0)

def get_successors(state):
    """Generates all valid next states from the current state."""
    successors = []
    idx = find_blank(state)
    row, col = idx // 3, idx % 3

    moves = [
        (-1, 0, 'Up'),
        (1, 0, 'Down'),
        (0, -1, 'Left'),
        (0, 1, 'Right')
    ]

    for dr, dc, move_name in moves:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col

            state_list = list(state)
            state_list[idx], state_list[new_idx] = state_list[new_idx], state_list[idx]
            next_state = tuple(state_list)

            successors.append((next_state, move_name))

    return successors

def solve_8_puzzle_dfs(initial_state, goal_state):
    """Solves the 8-puzzle using Depth-First Search (DFS)."""
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()

        if current_state == goal_state:
            return path

        if current_state not in visited:
            visited.add(current_state)

            for next_state, move in get_successors(current_state):
                if next_state not in visited:
                    new_path = path + [move]
                    stack.append((next_state, new_path))

    return None


start_node = (1, 2, 3, 4, 5,  6, 0, 7, 8)


goal_node  = (1, 2, 3, 4, 5, 6, 7, 8, 0)

print("Searching for a solution using DFS...")
solution = solve_8_puzzle_dfs(start_node, goal_node)

if solution:
    print(f"Goal reached in {len(solution)} moves!")
    print("Move sequence:", " -> ".join(solution))
else:
    print("No solution found or state limit exceeded.")
