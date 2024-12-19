def total_similarity(left_list, right_list):
    left_list.sort()
    right_list.sort()

    similarity = 0 

    for l in left_list:
        temp = 0
        for r in right_list:
            if l < r:
                break
            if l == r:
                temp += 1
        similarity =  similarity + (l * temp) 
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

