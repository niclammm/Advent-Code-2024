def count_p2_patterns(grid):
    """
    Counts occurrences of the second set of patterns (p2) in the grid.
    Args:
        grid (list of str): The 2D grid of characters.
    Returns:
        int: Count of p2 patterns.
    """
    p2 = 0  # Count for the second set of patterns

    R = len(grid)      # Number of rows
    C = len(grid[0])   # Number of columns

    # Loop through the grid
    for r in range(R):
        for c in range(C):
            # Second set of patterns (p2)
            if r + 2 < R and c + 2 < C and grid[r][c] == 'M' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'S' and grid[r + 2][c] == 'M' and grid[r][c + 2] == 'S':
                p2 += 1
            if r + 2 < R and c + 2 < C and grid[r][c] == 'M' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'S' and grid[r + 2][c] == 'S' and grid[r][c + 2] == 'M':
                p2 += 1
            if r + 2 < R and c + 2 < C and grid[r][c] == 'S' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'M' and grid[r + 2][c] == 'M' and grid[r][c + 2] == 'S':
                p2 += 1
            if r + 2 < R and c + 2 < C and grid[r][c] == 'S' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'M' and grid[r + 2][c] == 'S' and grid[r][c + 2] == 'M':
                p2 += 1

    return p2


if __name__ == "__main__":
    # Read the grid from input.txt
    file_path = "input.txt"
    try:
        with open(file_path, "r") as f:
            grid = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)

    # Count patterns for p2
    p2 = count_p2_patterns(grid)

    # Print result
    print(p2)
