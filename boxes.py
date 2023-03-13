import math

print("This is a packing calulation.")
items = int(input("Enter the number of items: "))
box = int(input("Enter the number of items per box: "))

box_num = math.ceil (items/box)

print(f"For {items} items, packing {box} items in each box, you will need {box_num} boxes.")