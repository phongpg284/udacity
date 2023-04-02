def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot_index = get_max_pivot_index(input_list)
    length = len(input_list)
    start = 0
    end = length - 1

    if number >= input_list[0] and number <= input_list[pivot_index]:
        end = pivot_index
    else:
        start = pivot_index + 1

    current = (start + end) // 2
    while start <= end:
        current = (start + end) // 2
        if input_list[current] == number:
            return current

        if input_list[current] > number:
            end = current - 1
        else: 
            start = current + 1
    return -1

def get_max_pivot_index(list):
    length = len(list)
    start = 0
    end = length - 1 
    current = (start + end) // 2
    if length == 1:
        return 0
    while list[current + 1] == list[current] + 1:
        current = (start + end) // 2
        if list[current] > list[length - 1]:
            start = current
        else: 
            end = current 
    return current

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

test_function([[2, 0], 0])
test_function([[2, 0, 1], 2])
test_function([[2, 0], 1000])
test_function([[0], 0])
test_function([[0], 100])
