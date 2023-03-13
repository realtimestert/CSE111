from datetime import datetime
import math

#function to print current date and time
# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = ("Stuart")
# print(first_name)
# print_time("printed first name")

# for x in range(0,10):
#     print(x)
# print_time("completed for loop")

# def get_initial(name, force_uppercase=True):
#     if force_uppercase:
#         initial = name[0:1].upper() 
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input("Enter your first name: ")
# first_name_initial = get_initial(first_name)

# print("Your initial is: " + first_name_initial)

# def main():
#     # Get an odometer value in U.S. miles from the user.
#     start_miles = float(input("Enter the first odometer reading (miles): "))
#     # Get another odometer value in U.S. miles from the user.
#     end_miles = float(input("Enter the second odometer reading (miles): "))
#     # Get a fuel amount in U.S. gallons from the user.
#     amount_gallons = float(input("Enter the amount of fuel used (gallons): "))
#     # Call the miles_per_gallon function and store
#     # the result in a variable named mpg.
#     mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
#     # Call the lp100k_from_mpg function to convert the
#     # miles per gallon to liters per 100 kilometers and
#     # store the result in a variable named lp100k.
#     lp100k = lp100k_from_mpg(mpg)
#     # Display the results for the user to see.
#     print(f"{mpg:.1f} miles per gallon")
#     print(f"{lp100k:.2f} liters per 100 kilometers")


# def miles_per_gallon(start_miles, end_miles, amount_gallons):
#     """Compute and return the average number of miles
#     that a vehicle traveled per gallon of fuel.

#     Parameters
#         start_miles: An odometer value in miles.
#         end_miles: Another odometer value in miles.
#         amount_gallons: A fuel amount in U.S. gallons.
#     Return: Fuel efficiency in miles per gallon.
#     """
#     mpg = abs(end_miles - start_miles) / amount_gallons
#     return mpg


# def lp100k_from_mpg(mpg):
#     """Convert miles per gallon to liters per 100
#     kilometers and return the converted value.

#     Parameter mpg: A value in miles per gallon
#     Return: The converted value in liters per 100km.
#     """
#     lp100k = 235.215 / mpg
#     return lp100k

def main():
    len1 = arc_length(4.7)
    print(f"len1: {len1:.1f}")

    len2 = arc_length(4.7, 270)
    print(f"len2: {len2:.1f}")

def arc_length(radius, degrees = 360):
    circumference = 2 *math.pi * radius
    length = circumference * degrees / 360
    return length

# Call the main function so that
# this program will start executing.
main()