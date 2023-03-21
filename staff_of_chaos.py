import random
import csv
import pytest
from guizero import App

app = App(title="Staff of Chaos")
app.display()

def main():
    #choice = input("Will you use the staff of Chaos? Y/N? ")

    random_magic = read_compound_list("10000_random.csv")
    
    #Prints out a list of all the magical effects.
    #print_list(random_magic)
    
    print(random_number (4))

def random_number(length, number=None):
    if number == None:
        number = "0123456789"

    rand = ""
    for i in range(length):
        rand += random.choice(number)

    return rand

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(compound_list):
    for element in compound_list:
        print(element)
    print()

if __name__ == "__main__":
    main()