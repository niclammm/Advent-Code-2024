def find_correct_updates(updates, rules):
    """
    Finds all correctly ordered updates and sums their middle pages.
    """
    total_middle_sum = 0

    for update in updates:
        if is_update_valid(update, rules):
            total_middle_sum += find_middle_page(update)

    return total_middle_sum


def is_update_valid(update, rules):
    """
    Checks if an update is valid based on the ordering rules.
    """
    # Map each page to its position in the update
    page_index = {page: i for i, page in enumerate(update)}

    # Check all rules
    for x, y in rules:
        if x in page_index and y in page_index:  # Both pages must exist in the update
            if page_index[x] > page_index[y]:  # x must come before y
                return False
    return True


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
            data = file.read().strip().split("\n\n")  # Split rules and updates sections
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
    result = find_correct_updates(updates, rules)
    print("Sum of middle pages from correctly ordered updates:", result)
else:
    print("No updates found.")
