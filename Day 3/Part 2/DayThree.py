import re

def extract_and_sum_with_conditions(file_name):
    total_sum = 0
    enabled = True  # mul is enabled by default

    # Regex patterns
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"  # Valid mul(X,Y)
    do_pattern = r"do\(\)"                     # do() instruction
    dont_pattern = r"don't\(\)"                # don't() instruction

    # Read input line by line
    with open(file_name, "r") as file:
        for line in file:
            i = 0  # Track position in the line
            while i < len(line):
                # Check for don't() and update enabled state
                if re.match(dont_pattern, line[i:]):
                    enabled = False
                    i += len("don't()")
                    continue
                
                # Check for do() and update enabled state
                elif re.match(do_pattern, line[i:]):
                    enabled = True
                    i += len("do()")
                    continue
                
                # Check for valid mul(X,Y) if enabled
                mul_match = re.match(mul_pattern, line[i:])
                if mul_match and enabled:
                    x, y = map(int, mul_match.groups())
                    total_sum += x * y
                    i += len(mul_match.group(0))  # Move past this instruction
                    continue
                
                # Move to the next character
                i += 1

    return total_sum

# Input file
file_name = "input.txt"  # Replace with your input file path
result = extract_and_sum_with_conditions(file_name)
print("Total Sum of Enabled Multiplications:", result)