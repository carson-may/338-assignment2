import json
import random
with open("Q2/ex2.json") as a:
        input = json.load(a)

for arr in input:
    arr = random.shuffle(arr)
jsonInput = json.dumps(input)
with open("Q2/ex2.5.json", "w") as outfile:
    outfile.write(jsonInput)
