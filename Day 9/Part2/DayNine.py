def parse_input(file_path):
    """Parses the disk map from the input file into a list of blocks."""
    with open(file_path, "r") as file:
        disk_map = file.read().strip()

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

def find_leftmost_span(blocks, file_length):
    """Finds the leftmost span of free space that can fit a file."""
    n = len(blocks)
    free_start = -1
    free_count = 0

    for i in range(n):
        if blocks[i] == '.':
            if free_start == -1:
                free_start = i
            free_count += 1
            if free_count == file_length:
                return free_start
        else:
            free_start = -1
            free_count = 0

    return -1  # No valid span found

def move_whole_files(blocks):
    """Moves whole files to the leftmost span of free space."""
    file_lengths = {}
    for i, block in enumerate(blocks):
        if block != '.':
            file_lengths[block] = file_lengths.get(block, 0) + 1

    # Process files in descending order of file ID
    for file_id in sorted(file_lengths.keys(), reverse=True, key=int):
        file_length = file_lengths[file_id]
        free_start = find_leftmost_span(blocks, file_length)

        if free_start != -1:  # Move the file to the free span
            # Clear the current file blocks
            for i in range(len(blocks)):
                if blocks[i] == file_id:
                    blocks[i] = '.'
            # Place the file in the new span
            for i in range(free_start, free_start + file_length):
                blocks[i] = file_id

    return blocks

def calculate_checksum(blocks):
    """Calculates the checksum for the compacted disk."""
    checksum = 0
    for i, block in enumerate(blocks):
        if block != '.':
            checksum += i * int(block)
    return checksum

# Input file path
file_path = "input.txt"

# Parse the disk map, compact it, and calculate checksum
blocks = parse_input(file_path)
compacted_blocks = move_whole_files(blocks)
checksum = calculate_checksum(compacted_blocks)

# Output the result
print("Checksum:", checksum)
