def is_safe(report):
    increasing = decreasing = True  # Both flags start as True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        # Check if the difference is invalid
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        # Update flags
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False

    return increasing or decreasing

def can_be_safe_with_dampener(report):
    # Try removing each level one by one
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]  # Remove one level
        if is_safe(new_report):
            return True
    return False

def count_safe_reports_with_dampener(file_name):
    safe_count = 0

    with open(file_name, "r") as f:
        for line in f:
            report = list(map(int, line.split()))  # Convert line to list of integers

            if is_safe(report) or can_be_safe_with_dampener(report):
                safe_count += 1

    return safe_count

# Read the input file and compute results
file_name = "input.txt"  # Replace with your input file path
result = count_safe_reports_with_dampener(file_name)
print("Number of Safe Reports (with Dampener):", result)
