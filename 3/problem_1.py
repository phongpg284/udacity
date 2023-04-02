def sqrt(number):
    return sqrt_on_range(0, 0, 1, number)

# check if number is floor square of value number
def is_floor_sqrt(floor_value, value):
    return floor_value ** 2 <= value and (floor_value + 1) ** 2 > value

"""
    Calculate the floored square root of a number with range from off set to max_range
"""
def sqrt_on_range(offset, current, max_range, number):
    # Keep recursive until got max_range surpass square value need to find
    if max_range ** 2 < number:
        current = (offset + max_range) // 2
        return sqrt_on_range(max_range, current, max_range * 2, number)
    
    if is_floor_sqrt(current, number):
        return current
    
    # check if current value surpass or not square value need to find
    if  current ** 2 > number:
        return sqrt_on_range(offset, current - (current - offset + 1) // 2, current, number)
    else:
        return sqrt_on_range(current, current + (max_range - current + 1) // 2, max_range, number)

def test_function(value, expected_square_root_value):
    print ("Pass" if  expected_square_root_value == sqrt(value) else "Fail")

test_function(0, 0)
test_function(1, 1)
test_function(2, 1)
test_function(4, 2)
test_function(9, 3)
test_function(27, 5)
test_function(1000000, 1000)
test_function(1234 * 1234 + 2, 1234)
test_function(12346 * 12346 - 1, 12345)