import csv

# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():

    try:
        #opening the csv file into memory
        student_list = read_compound_list("pupils.csv")

        #lambda function to extract the birthdays
        birthday_sort = lambda student_list: f"{student_list[BIRTHDATE_INDEX]}"
        sorted_birthdays = sorted(student_list, key = birthday_sort)

        #sorts birthdays from Oldest to Youngest
        print("Ordered from Oldest to Youngest")
        for birthday in sorted_birthdays:
            print(birthday)
        
        # lambda function to extract the given name
        sorted_list = lambda student_list: f"{student_list[GIVEN_NAME_INDEX]}"
        sorted_given_name = sorted(student_list, key = sorted_list)

        #sorts the list by Given Name in alphabetical order
        print()
        print("Ordered by Given Name")
        for given_name in sorted_given_name:       
            print(given_name)

        #lol not even going to try to order by birthday month and day

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep="; ")

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
