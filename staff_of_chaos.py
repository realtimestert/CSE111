import random
import csv
from guizero import App, Text, PushButton

def main():
    app_window()

def app_window():
    
    # returns a random value from csv file and displays on the app window
    def change_message():
        with open("10000_random.txt") as f:
            words = f.readlines()
            my_pick = random.choice(words)
        message.value = my_pick

    #return a random value from a txt file
    def change_message_2():
        message.value = "Okay"      
    
    app = App(title="Staff of Chaos")
    message = Text(app, text = "Will you use the Staff of Chaos?")
    
    # Push the button to change the message
    button1 = PushButton(app, align = "left", text = "Use it", command = change_message)
    button2 = PushButton(app, align = "right", text = "Don't", command = change_message_2)
    
    app.display()

def rand_number(length, number=None):
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

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    #Opening CSV file
    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list

    return dictionary

def print_list(compound_list):
    for element in compound_list:
        print(element)
    print()

if __name__ == "__main__":
    main()