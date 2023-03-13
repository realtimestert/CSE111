import math
import random
import csv
from students import read_dictionary

# def main():
#     x=random.randint(0,100)
#     y=random.randint(0,100)

#     try:
#         print(f"{(x/y):.2f}")
#     except ZeroDivisionError as e:
#         print("Not allowed to divide by zero")
#     except:
#         print("Something else went wrong")
#     finally: 
#         print ("This always runs on success or failure")

#     if x>y:
#         print(str(x) + " is greater than " + str(y))
#     elif y>x: 
#         print(str(x) + " is less than " + str(y))

#     print()

# if __name__ == "__main__":
#     main()

# Example 2

def main():
    try:
        text = float(input("Please enter a number: "))
        integer = round(text)
        print(integer)

    except TypeError as type_err:
        print(type_err)
    except ValueError as val_err:
        print(val_err)

if __name__ == "__main__":
    main()