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

def generate_positions_between(a1, a2):
    """Generates all positions between two points, inclusive."""
    r1, c1 = a1
    r2, c2 = a2
    dr = r2 - r1
    dc = c2 - c1
    gcd = abs(dr) if dc == 0 else abs(dc) if dr == 0 else abs(dr) if abs(dr) < abs(dc) else abs(dc)

    if gcd > 0:  # Normalize direction vector
        dr //= gcd
        dc //= gcd
    
    positions = []
    current_r, current_c = r1, c1
    while (current_r, current_c) != (r2 + dr, c2 + dc):
        positions.append((current_r, current_c))
        current_r += dr
        current_c += dc
    return positions

def find_unique_antinodes(grid):
    """Finds all unique antinode locations within the grid bounds."""
    antennas = find_antennas(grid)
    unique_antinodes = set()

    for freq, positions in antennas.items():
        # Compare all pairs of antennas with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                a1, a2 = positions[i], positions[j]
                # Generate all positions along the line connecting the two antennas
                antinodes = generate_positions_between(a1, a2)
                unique_antinodes.update(antinodes)
    
    return unique_antinodes

def count_antinodes(file_path):
    """Counts the total number of unique antinode locations."""
    grid = parse_input(file_path)
    unique_antinodes = find_unique_antinodes(grid)
    return len(unique_antinodes)

# Input file path and solving the problem
file_path = "input.txt"  # Replace with your actual file path
result = count_antinodes(file_path)
print("Total Unique Antinode Locations:", result)
