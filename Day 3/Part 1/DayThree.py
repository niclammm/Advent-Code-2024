import re

def extract_and_sum_multiplications(file_name):
    total_sum = 0

    # Define the regex pattern to match valid mul(X,Y)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Open and read the input file
    with open(file_name, "r") as file:
        for line in file:
            # Find all matches of the pattern in the current line
            matches = re.findall(pattern, line)

            # Process each match
            for x, y in matches:
                total_sum += int(x) * int(y)

    return total_sum

# Input file path
file_name = "input.txt"  # Replace with your input file path

# Run the function and print the result
result = extract_and_sum_multiplications(file_name)
print("Total Sum of Valid Multiplications:", result)
