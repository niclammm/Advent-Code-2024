def parse_input(file_path):
    """Parses the disk map from the input file into a list of blocks."""
    with open(file_path, "r") as file:
        disk_map = file.read().strip()  # Read the entire file as a single string

    blocks = []
    file_id = 0
    i = 0

    while i < len(disk_map):
        if i % 2 == 0:  # File length
            file_length = int(disk_map[i])
            blocks.extend([str(file_id)] * file_length)
            file_id += 1
        else:  # Free space length
            free_length = int(disk_map[i])
            blocks.extend(['.'] * free_length)
        i += 1

    return blocks

def compact_disk(blocks):
    """Compacts the disk by moving file blocks left into free spaces."""
    end_pointer = len(blocks) - 1

    while end_pointer >= 0 and blocks[end_pointer] == ".":
        end_pointer -= 1  # Find the last non-free-space block

    for n in range(len(blocks)):
        if n >= end_pointer:  # Stop if no more blocks to move
            break
        if blocks[n] == ".":  # Move file block into the free space
            while end_pointer > n and blocks[end_pointer] == ".":
                end_pointer -= 1  # Skip over free spaces at the end
            if end_pointer > n:  # Ensure there is still something to move
                blocks[n] = blocks[end_pointer]
                blocks[end_pointer] = "."
                end_pointer -= 1

    return blocks

def calculate_checksum(blocks):
    """Calculates the checksum for the compacted disk."""
    checksum = 0
    for i, block in enumerate(blocks):
        if block != ".":  # Skip free spaces
            checksum += i * int(block)
    return checksum

# Input file path
file_path = "input.txt"

# Parse the disk map, compact it, and calculate checksum
blocks = parse_input(file_path)
compacted_blocks = compact_disk(blocks)
checksum = calculate_checksum(compacted_blocks)

# Output the result
print("Checksum:", checksum)
