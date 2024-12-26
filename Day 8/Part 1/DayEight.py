def parse_input(file_path):
    """Reads the input file and parses the map."""
    with open(file_path, "r") as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def find_antennas(grid):
    """Finds all antennas and their coordinates."""
    antennas = {}
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != '.':  # It's an antenna
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((r, c))
    return antennas

def calculate_antinode(a1, a2):
    """Calculates the potential antinode locations for two antennas."""
    r1, c1 = a1
    r2, c2 = a2
    dr = r2 - r1
    dc = c2 - c1

    # Potential antinode locations
    antinode1 = (r1 - dr, c1 - dc)  # Extend the line backward
    antinode2 = (r2 + dr, c2 + dc)  # Extend the line forward
    return antinode1, antinode2

def find_unique_antinodes(grid):
    """Finds all unique antinode locations within the grid bounds."""
    antennas = find_antennas(grid)
    unique_antinodes = set()

    for freq, positions in antennas.items():
        # Compare all pairs of antennas with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                a1, a2 = positions[i], positions[j]
                # Calculate potential antinodes
                antinode1, antinode2 = calculate_antinode(a1, a2)
                
                # Check if the potential antinodes are valid
                if 0 <= antinode1[0] < len(grid) and 0 <= antinode1[1] < len(grid[0]):
                    unique_antinodes.add(antinode1)
                if 0 <= antinode2[0] < len(grid) and 0 <= antinode2[1] < len(grid[0]):
                    unique_antinodes.add(antinode2)
    
    return unique_antinodes

def count_antinodes(file_path):
    """Counts the total number of unique antinode locations."""
    grid = parse_input(file_path)
    unique_antinodes = find_unique_antinodes(grid)
    return len(unique_antinodes)

# Input file path
file_path = "input.txt"  # Replace with your actual file path
result = count_antinodes(file_path)
print("Total Unique Antinode Locations:", result)
