import json
import datetime

# open json file and read
infile = open('data.json')
data = json.load(infile)
# empty array to accept data from data.json file
words_list = []
# loop through each element and append to words_list
for words in data:
    words_list.append(words)
# close words.json reader
infile.close()

# empty array to build date ranges
days = []

# create delta day incrementer
day_delta = datetime.timedelta(days=1)
start_date = datetime.date.today()
# 2078 = extracted from item count in words_list
# end_date = start_date + 2078 * day_delta

# loop through range to step one day each loop and create a date string
for i in range(0, 2078):
    key_to_add = start_date + i * day_delta
    key_to_add = key_to_add.strftime("%Y-%m-%d")
    days.append(key_to_add)

# object to build key-value pair of matching correct word to applicable date
answer_key = dict(zip(days, words_list))

with open('words.json', 'w') as file:
    json.dump(answer_key, file)

print("Creating JSON file...")
