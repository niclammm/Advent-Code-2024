from collections import Counter
def total_similarity(left_list, right_list):
    right_count = Counter(right_list)
    similarity = 0 

    for l in left_list:
        similarity += (l * right_count[l]) 
        
    return similarity

with open("input.txt", "r") as f:
    left_list = []
    right_list = []

    for line in f:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    result = total_similarity(left_list, right_list)
    print("Total Similarity:", result)

