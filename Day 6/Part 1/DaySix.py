def parse_input(file_path):
    """
    Reads the input file and returns the grid, guard's starting position, and direction.
    """
    grid = []
    start_pos = None
    start_dir = None

    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    with open(file_path, "r") as file:
        for y, line in enumerate(file.readlines()):
            row = list(line.strip())
            for x, char in enumerate(row):
                if char in directions:
                    start_pos = (x, y)
                    start_dir = directions[char]
                    row[x] = '.'  # Replace guard's position with empty space
            grid.append(row)

    return grid, start_pos, start_dir


def simulate_guard(grid, start_pos, start_dir):
    """
    Simulates the guard's movement and returns the number of unique positions visited.
    """
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left
    current_dir = directions.index(start_dir)
    x, y = start_pos
    visited = set()
    visited.add((x, y))  # Include the starting position

    rows, cols = len(grid), len(grid[0])

    while True:
        # Calculate next position
        dx, dy = directions[current_dir]
        nx, ny = x + dx, y + dy

        # Check if the next position is out of bounds
        if nx < 0 or ny < 0 or ny >= rows or nx >= cols:
            break

        # Check if the next position is an obstacle
        if grid[ny][nx] == '#':
            # Turn right 90 degrees
            current_dir = (current_dir + 1) % 4
        else:
            # Move forward
            x, y = nx, ny
            visited.add((x, y))

    return len(visited)


# Main Execution
if __name__ == "__main__":
    file_path = "input.txt"  # Replace with your input file path
    grid, start_pos, start_dir = parse_input(file_path)
    result = simulate_guard(grid, start_pos, start_dir)
    print("Number of distinct positions visited:", result)
