"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def get_prefix(phone):
    if phone[0] == "(":
        close_bracket_position = phone.find(")");
        return phone[1:close_bracket_position]
    elif phone[0] == "1":
        return phone[:3]
    else:
        return phone[:4]

def is_matching_area_code(phone, city_code):
    return get_prefix(phone) == city_code

bangalore_receive_call_codes = set()
bangalore_two_side_call_amount = 0
total_bangalore_calling_amount = 0

for call in calls:
    called_number, received_number, record_time, record_duration = call
    if is_matching_area_code(called_number, '080'):
        bangalore_receive_call_codes.add(get_prefix(received_number))
        total_bangalore_calling_amount = total_bangalore_calling_amount + 1
        if is_matching_area_code(received_number, '080'):
            bangalore_two_side_call_amount = bangalore_two_side_call_amount + 1

bangalore_receive_call_codes = sorted(bangalore_receive_call_codes)

print("The numbers called by people in Bangalore have codes:")
for code in bangalore_receive_call_codes:
    print(code)

percentage = round(bangalore_two_side_call_amount / total_bangalore_calling_amount * 100, 2)
print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
