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

def depth_limited_dfs(initial_state, goal_state, limit):
    """Performs a DFS search up to a maximum depth limit."""
    stack = [(initial_state, [], {initial_state})]

    while stack:
        current_state, path, current_branch = stack.pop()

        if current_state == goal_state:
            return path

        if len(path) == limit:
            continue

        for next_state, move in get_successors(current_state):
            if next_state not in current_branch:
                new_path = path + [move]
                new_branch = current_branch.copy()
                new_branch.add(next_state)

                stack.append((next_state, new_path, new_branch))

    return None

def solve_8_puzzle_ids(initial_state, goal_state, max_depth=50):
    """Solves the 8-puzzle using Iterative Deepening Search (IDS)."""
    for limit in range(max_depth + 1):
        print(f"Searching with depth limit: {limit}...")
        result = depth_limited_dfs(initial_state, goal_state, limit)

        if result is not None:
            return result

    return None


start_node = (1, 2, 3, 0, 4, 6, 7, 5, 8)


goal_node  = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = solve_8_puzzle_ids(start_node, goal_node)

if solution is not None:
    print(f"\nSuccess! Goal reached in {len(solution)} moves.")
    print("Move sequence:", " -> ".join(solution))
else:
    print("\nCould not find a solution within the maximum depth limit.")
