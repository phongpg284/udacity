"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

telephones = {}
def add_call_duration(phone, duration_string):
    duration = int(duration_string)
    if (telephones.get(phone) != None):
        telephones[phone] = telephones[phone] + duration
    else:
        telephones[phone] = duration

for call in calls:
    add_call_duration(call[0], call[3])
    add_call_duration(call[1], call[3])

max_call_length_phone = max(telephones, key= lambda x: telephones[x])
max_call_length = telephones.get(max_call_length_phone)

print(f"{max_call_length_phone} spent the longest time, {max_call_length} seconds, on the phone during September 2016.")
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

