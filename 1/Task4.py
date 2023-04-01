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

telemarketers = set()

for call in calls:
    called_number = call[0]
    telemarketers.add(called_number)

for call in calls:
    received_number = call[1]
    telemarketers.discard(received_number)

for text in texts:
    sended_number, received_number, *rest = call
    telemarketers.discard(sended_number)
    telemarketers.discard(received_number)

telemarketers = sorted(telemarketers)

print("These numbers could be telemarketers: ")
for phone in telemarketers:
    print(phone)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

