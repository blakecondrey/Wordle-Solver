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
