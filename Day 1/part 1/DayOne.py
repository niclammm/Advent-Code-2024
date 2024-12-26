def total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total = 0

    for l, r in zip(left_list, right_list):
        total += abs(l - r)

    return total

# Step 4: Read input from a file or manual input
with open("input.txt", "r") as f:
    left_list = []
    right_list = []
    
    for line in f:
        # Split each line into left and right values
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
result = total_distance(left_list, right_list)
print("Total Distance:", result)
