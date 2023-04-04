def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    digits_count = [0] * 11
    first_number = ""
    second_number = ""
    picked_number = 1

    if len(input_list) <= 1:
        return input_list

    for digit in input_list:
        digits_count[digit] += 1
    
    current_digit = 9
    while current_digit > -1:
        current_digit_count = digits_count[current_digit]
        if current_digit_count > 0:
            if picked_number == 1:
                first_number += str(current_digit)
            else:
                second_number += str(current_digit)
            
            picked_number = picked_number * -1
            digits_count[current_digit] -= 1
        else:
            current_digit -= 1
    return [int(first_number), int(second_number)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 1, 1, 1, 1, 1], [111, 111]])
test_function([[0, 1], [1, 0]])
test_function([[1, 1, 0], [10, 1]])
test_function([[], []])
test_function([[1], [1]])