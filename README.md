#### Wordle Solver!

...well, more like a file reader, but.... you get it.

<p>I completed my daily <b>Wordle</b> challenge today, as always, to kill some time.<br>Having lived in Chrome DevTools and the <b>Components</b> application for my react apps the past several months, I decided to inspect the Wordle site to see what kind of technologies or methods were used.<br>As I was scrolling mindlessly, I noticed (rather unfortunately) that the asnwer key was stored in an array, and I quickly wondered how the program new which word to output simultaneously across the world; thinking there had to be some sort of <b>Date</b> object that it pointed to - which, it was. So I decided to flex some dystrophic <b>Python</b> muscles as they have been severely neglected.<br>Let's get to work!</p>
<br>
<p>I knew I was going to need the list of words from the site. Simple copypasta beginning at todays word.</p>

- Let's make a <b>data.json</b> file to hold this data.
<br>
<p>I want to load the data from <b>data.json</b> into a dictionary, then create a date object as value to the <b>word</b> key. I used the <b>datetime</b> module once for a web-scraping project, and it worked out well, so I think that's the move.</p>

```py
print(len(data))
# output = 2079
```

<br>
<p>
Loop through (0. 2078) range, create date at each iteration with the date incrementing by a delta of 1 day through each variable. Bind the variable's to the dictionary as the key-value pair to accompanying word
</p>

```py
import datetime

for i in range(0, 2078):
    value_to_add = start_date + i * day_delta
    value_to_add = value_to_add.strftime("%Y-%m-%d")
```

<br>
<p>
Okay, so, I can't figure out how to loop through both the list of words and create a date variable to store as the word's (key) value. I keep tying the last possible date based on the length of the words list to every word. I'm definitely over-thinking this.
</p>
<br>
<p>
Udemy to the rescue. I remember learning zip() in Colt Steele's Modern Python Course.
Way-ahead is to read from the json file and append each value to an empty list <b>words_list</b> and close the file, then open another empty list <b>days</b> where I'll iterate through the (0, 2078) range and append each date created to the <b>days</b> list.
After that, it's real simple. Declare a variable <b>answer_key</b> to build the dictionary of zipped arrays of equal length into key-value pairs.
I swapped the key-value pairs, as, if my memory serves correct, I think it will be easier to find a value match the days word with the dates as the key.
</p>

```py
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
```

```py
days = []

# create delta day incrementer
day_delta = datetime.timedelta(days=1)
start_date = datetime.date.today()
# 2078 = extracted from item count in words_list
end_date = start_date + 2078 * day_delta

# loop through range to step one day each loop and create a date string
for i in range(0, 2078):
    value_to_add = start_date + i * day_delta
    value_to_add = value_to_add.strftime("%Y-%m-%d")
    days.append(value_to_add)

# object to build key-value pair of matching correct word to applicable date
answer_key = dict(zip(days, words_list))
```

<br>
<p>
Last step in this file is to dump <b>answer_key</b> into a new json file, <b>words.json</b>
</p>

```py
with open('words.json', 'w') as file:
    json.dump(answer_key, file)
```

<p>
Now, just going to create a lightweight script to read the <b>words.json</b> file, and, using the same <b>datetime</b> module as before, I should be able to instantiate a datetime as "today", iterate through the file, and find a matching key to the <b>date_now</b> variable.
<br>

```py
import json
import datetime

date_now = datetime.date.today()
date_now = date_now.strftime("%Y-%m-%d")

with open('words.json') as readfile:
    data = json.loads(readfile.read())
    pairs = data.items()

    for key, value in pairs:
        if key == date_now:
            print("\n\n\n", value, "\n\n\n")
```

<p>And it works! Like I said, more a file-reading exercise than it is an "algorithm" or a sophisticated "solver". Hope you learned something!</p>
<p>Could there have been a better way to do this? I can almost guarantee it! Feel free to fork, clone, or copypasta this project and do better than I did.</p>
<br>
<p><strong>www.blakecondrey.com</p>
