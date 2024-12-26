from itertools import product

# Function to parse input from a file
def parse_input(file_path):
    with open(file_path, "r") as file:
        parse_inputs = file.readlines()
    return parse_inputs

# Function to concatenate two numbers
def concatenate(a, b):
    return int(str(a) + str(b))

# Function to evaluate an expression given numbers and operators
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = concatenate(result, numbers[i + 1])
    return result

# Function to solve calibrations and compute the total result
def solve_calibrations(input_data):
    total_calibration_result = 0
    for line in input_data:
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        operator_combinations = product(['+', '*', '||'], repeat=len(numbers) - 1)
        
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == target:
                total_calibration_result += target
                break  # Only need one valid configuration per equation
    return total_calibration_result

# Input file path and solving the problem
file_path = "input.txt" 
result = solve_calibrations(parse_input(file_path))
print(result)
