# 0. Utils
# 1. Linear Search
# 2. Binary Search
# 3. Jump Search

import random

def generate_random_unsorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    """
    Generate random and unsorted list with count n.
    
    n : List item count
    min_value : minimum random value
    max_value : maximum random value
    """
    new_list = []
    for i in range(n):
        new_list.append(random.randint(min_value,max_value))

    return new_list
def generate_random_sorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    
    new_list = []
    last_added = 0
    new_value = 0
    
    for i in range(n):
        # TODO Refine min/max value issue
        new_value = random.randint(last_added+1, max(last_added+10,max_value))
        new_list.append(new_value)
        last_added = new_value
    
    return new_list
    
def search_linear(source_list:list, target:int)->tuple:
    # index = 0
    # for i in source_list:
    #     if i==target:
    #         return True, index
    #     index += 1
    
    for index in range(len(source_list)):
        if source_list[index]==target:
            return True, index
    
    return False, -1
   
my_list = generate_random_unsorted_list()
print("List : ", my_list)

target = 100 #my_list[3]
print("Target : ", target)
search_result, index = search_linear(my_list, target)
print(f"Target ({target}) has been found at index {index}" if search_result else f"Target ({target}) has not been found")