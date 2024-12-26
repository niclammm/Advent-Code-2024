from itertools import product


def parse_input(file_path):
    with open (file_path,"r") as file:
        parse_inputs = file.readlines()
    return parse_inputs

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i]    == '*':
            result *= numbers[i + 1]
    return result

def solve_calibrations(input_data):
    total_calibration_result = 0
    for line in input_data:
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        operator_combinations = product(['+', '*'], repeat=len(numbers) - 1)
        
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == target:
                total_calibration_result += target
                break  # Only need one valid configuration per equation
    return total_calibration_result

file_path = "input.txt" 
result = solve_calibrations(parse_input(file_path))
print(result)