def find_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]

    def is_match(x, y, dx, dy):
        for k in range(len(word)):
            nx, ny = x + k * dx, y + k * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                return False  # Out of bounds
            if grid[nx][ny] != word[k]:
                return False  # Character doesn't match
        return True  # All characters matched

    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if is_match(i, j, dx, dy):
                    count += 1
    return count

def read_file_to_grid(file_path):
    grid = []
    with open(file_path, "r") as file:
        for line in file:
            # Clean the line and convert it to a list of characters
            grid.append(list(line.strip()))
    return grid

# Example Usage
file_path = "input.txt"  # Replace with your file path
grid = read_file_to_grid(file_path)
word = "XMAS"
result = find_word(grid, word)
print("Total occurrences of XMAS:", result)
