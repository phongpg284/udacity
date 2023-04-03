def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    min = float("inf")
    max = float("-inf")
    for item in ints:
        if item > max:
            max = item
        if item < min:
            min = item
    return (min, max)
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print ("Pass" if ((1, 9) == get_min_max([1,1,1,2,2,9,8])) else "Fail")
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0, 0])) else "Fail")