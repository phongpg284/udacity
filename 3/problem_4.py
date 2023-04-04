def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    sorted_list = []
    middle_point = 0        #middle point to insert 1

    for item in input_list:
        if item == 0:
            sorted_list.insert(0, 0)
            middle_point += 1
        elif item == 1:
            sorted_list.insert(middle_point, 1)
        else:
            sorted_list.append(2)
    return sorted_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([0])
'''
Pass
[0]
'''

test_function([1, 1, 1, 1])
'''
Pass
[1, 1, 1, 1]
'''

test_function([])
'''
Pass
[]
'''