from collections import defaultdict, deque


def find_incorrect_updates(updates, rules):
    """
    Finds and corrects incorrectly-ordered updates, then sums their middle pages.
    """
    total_middle_sum = 0

    for update in updates:
        if not is_update_valid(update, rules):  # Identify incorrect updates
            corrected = correct_update(update, rules)  # Correct the order
            total_middle_sum += find_middle_page(corrected)  # Add middle page of corrected update

    return total_middle_sum


def is_update_valid(update, rules):
    """
    Checks if an update is valid based on the ordering rules.
    """
    page_index = {page: i for i, page in enumerate(update)}

    for x, y in rules:
        if x in page_index and y in page_index:
            if page_index[x] > page_index[y]:
                return False
    return True


def correct_update(update, rules):
    """
    Corrects the order of an update using the ordering rules.
    """
    # Build a graph of dependencies
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_in_update = set(update)

    # Add directed edges based on rules
    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1

    # Perform topological sort (Kahn's algorithm)
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order


def find_middle_page(update):
    """
    Finds the middle page of an update.
    """
    return update[len(update) // 2]


def read_file(file_path):
    """
    Reads the input file and returns the rules and updates.
    """
    rules = []
    updates = []

    try:
        with open(file_path, "r") as file:
            data = file.read().strip().split("\n\n")
            rules_section = data[0]
            updates_section = data[1]

            # Parse rules
            for line in rules_section.splitlines():
                x, y = map(int, line.split("|"))
                rules.append((x, y))

            # Parse updates
            for line in updates_section.splitlines():
                updates.append(list(map(int, line.split(","))))

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    
    return rules, updates


# Example Usage
file_path = "input.txt"  # Replace with your file path
rules, updates = read_file(file_path)

if updates:  # Ensure updates are not empty
    result = find_incorrect_updates(updates, rules)
    print("Sum of middle pages from corrected updates:", result)
else:
    print("No updates found.")
