def sqrt(number):
    start = 0
    current = 1
    end = 1
    while end ** 2 <= number:
        start = end
        end = end * 2
    while start <= end:
        current = (start + end) // 2
        if current ** 2 <= number and (current + 1) ** 2 > number:
            return current
        elif current ** 2 < number:
            start = current
        else:
            end = current
    return current


def test_function(value, expected_square_root_value):
    print("Pass" if expected_square_root_value == sqrt(value) else "Fail")


test_function(0, 0)
test_function(1, 1)
test_function(2, 1)
test_function(4, 2)
test_function(9, 3)
test_function(27, 5)
test_function(1000000, 1000)
test_function(1234 * 1234 + 2, 1234)
test_function(12346 * 12346 - 1, 12345)
