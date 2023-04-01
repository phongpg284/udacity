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

telephone_set = set()
for text in texts:
    telephone_set.add(text[0])
    telephone_set.add(text[1])

for call in calls:
    telephone_set.add(call[0])
    telephone_set.add(call[1])

print(f"There are {len(telephone_set)} different telephone numbers in the records.")
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
