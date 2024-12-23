def find_xmas(grid):
    """
    Finds all occurrences of the X-MAS patterns in the grid.
    """
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':  # Center of the X-MAS pattern
                if is_xmas(i, j, grid):
                    count += 1
    return count


def is_xmas(x, y, grid):
    """
    Checks if an X-MAS pattern exists centered at (x, y) in the grid.
    """
    rows, cols = len(grid), len(grid[0])

    # Define patterns with offsets and expected characters
    patterns = [
        # Forward MAS on both diagonals
        [(-1, -1, 'M'), (1, 1, 'S'), (-1, 1, 'M'), (1, -1, 'S')], 
        # Backward SAM on both diagonals
        [(-1, -1, 'S'), (1, 1, 'M'), (-1, 1, 'M'), (1, -1, 'S')], 
        # Mixed: Forward MAS, Backward SAM
        [(-1, -1, 'S'), (1, 1, 'M'), (-1, 1, 'S'), (1, -1, 'M')], 
        # Mixed: Backward SAM, Forward MAS
        [(-1, -1, 'M'), (1, 1, 'S'), (-1, 1, 'S'), (1, -1, 'M')]
    ]

    # Check each pattern
    for pattern in patterns:
        valid = True
        for dx, dy, expected in pattern:
            nx, ny = x + dx, y + dy
            # Ensure within bounds
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                valid = False
                break
            # Check expected character
            if grid[nx][ny] != expected:
                valid = False
                break
        if valid:
            return True
    return False


def read_file_to_grid(file_path):
    """
    Reads the input file and converts it into a grid (list of lists).
    """
    grid = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                grid.append(list(line.strip()))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return grid


# Example Usage
file_path = "input.txt"  # Replace with your file path
grid = read_file_to_grid(file_path)

if grid:  # Ensure grid is not empty
    result = find_xmas(grid)
    print("Total X-MAS patterns found:", result)
else:
    print("No data in grid.")