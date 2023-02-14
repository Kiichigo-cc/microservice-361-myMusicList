import sys
import json

search_input = str(sys.argv[1])
database = str(sys.argv[2])

f = open(database)
data = json.load(f)
results = []

f.close()

for i in data:
    if search_input.lower() in i['albumName'].lower():
        results.append(i['albumName'])

f2 = open('output.txt', 'r+')

for i in results:
    f2.write(i + '\n')

f2.close