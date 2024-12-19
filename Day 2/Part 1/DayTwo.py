def is_safe(report):
    increasing = decreasing = True
    for i in range(0, len(report) - 1):
        diff = report[i + 1] - report[i]

        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        if diff > 0:
            increasing = False
        if diff < 0:
            decreasing = False
        
    return increasing or decreasing
    
def count_safe_reports(file_name):
    safe_count = 0
    
    with open(file_name, "r") as f:
        for line in f:
            report = list(map(int, line.split()))  # Convert line to list of integers
            
            if is_safe(report):  # Check if the report is safe
                safe_count += 1
    
    return safe_count

file_name = "input.txt"  # Replace with your input file path
result = count_safe_reports(file_name)
print("Number of Safe Reports:", result)