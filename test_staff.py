import csv
import random

# with open ("10000_random.csv") as f:
#     reader = csv.reader(f)
#     chosen_row = random.choice(list(reader))

with open("10000_random.csv") as f:
    words = f.readlines()
    my_pick = random.choice(words)
    print(my_pick)