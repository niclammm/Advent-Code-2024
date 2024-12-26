from collections import defaultdict


def simulate_guard(grid, start_pos, start_dir, obstruction=None):
    """
    Simulates the guard's movement and returns whether they get stuck in a loop.
    """
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left
    current_dir = directions.index(start_dir)
    x, y = start_pos
    visited = set()
    history = set()

    rows, cols = len(grid), len(grid[0])

    while True:
        # Check for loop: same position and direction revisited
        state = (x, y, current_dir)
        if state in history:
            return True
        history.add(state)

        # Calculate next position
        dx, dy = directions[current_dir]
        nx, ny = x + dx, y + dy

        # Check if the next position is out of bounds
        if nx < 0 or ny < 0 or ny >= rows or nx >= cols:
            return False

        # Check if the next position is an obstacle
        if (nx, ny) == obstruction or grid[ny][nx] == '#':
            # Turn right 90 degrees
            current_dir = (current_dir + 1) % 4
        else:
            # Move forward
            x, y = nx, ny


def find_obstruction_positions(grid, start_pos, start_dir):
    """
    Finds all positions where adding an obstruction causes the guard to get stuck in a loop.
    """
    rows, cols = len(grid), len(grid[0])
    valid_positions = 0

    for y in range(rows):
        for x in range(cols):
            # Skip non-empty positions and the guard's starting position
            if grid[y][x] != '.' or (x, y) == start_pos:
                continue

            # Simulate with obstruction at (x, y)
            if simulate_guard(grid, start_pos, start_dir, obstruction=(x, y)):
                valid_positions += 1

    return valid_positions


def parse_input(file_path):
    """
    Parses the input file and returns the grid, starting position, and direction.
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
                    row[x] = '.'  # Replace the guard's starting position with empty space
            grid.append(row)

    return grid, start_pos, start_dir


# Main Execution
if __name__ == "__main__":
    file_path = "input.txt"  # Replace with your input file path
    grid, start_pos, start_dir = parse_input(file_path)
    result = find_obstruction_positions(grid, start_pos, start_dir)
    print("Number of valid obstruction positions:", result)
