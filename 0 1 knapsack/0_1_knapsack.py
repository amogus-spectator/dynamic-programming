# Given a bag which can only take certain weight W. Given list of items with their weights and price. How do you fill this bag to maximize value of items in the bag.

class item:
    def __init__(self, weight, value):
        self.weight = weight
        self.price = value
        
def weight(item):
    return item.weight
def knapsack(items, W):
    n = len(items)
    zero_matrix = [0*x for x in range(W)]
    matrix = [0]
    matrix.extend(zero_matrix)
    
    items_set = sorted(items, key=weight)
    for i in range(n):
        prev_matrix_state = matrix
        for j in range(W+1):
            if weight(items_set[i]) < j:
                matrix[j] = 0
                print(matrix)
            elif i == 0 and weight(items_set[i]) >= j:
                matrix[j] = weight(items_set[i])
                print(matrix)
            elif i > 0 and weight(items_set[i]) >= j:
                matrix[j] = max(matrix[j-1] + prev_matrix_state[j-i+1], prev_matrix_state[j])
        print(matrix)
    
    return matrix

items = [item(1, 1), item(3,4), item(4,5), item(5,7)]
print(knapsack(items, 7))
                