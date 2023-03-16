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
        
        #sort list from olde4st to youngest
        sorted_birthday = sort_by_birthday(student_list)
        print("Ordered from Oldest to Youngest")
        print_list(sorted_birthday)
        
        
        #sorts the list by Given Name in alphabetical order
        print()
        sorted_list2 = sort_by_given_name(student_list)
        print("Ordered by Given Name")
        print_list(sorted_list2)

        #Sort list by birth month and day
        print()
        sorted_list3 = sort_by_birth_month_day(student_list)
        print("Ordered by Birth Month and Day")
        print_list(sorted_list3)

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

def sort_by_birthday(students_list):
    
    #lambda function to extract the birthdays
    birthday_sort = lambda student_list: f"{student_list[BIRTHDATE_INDEX]}"
    sorted_birthdays = sorted(students_list, key = birthday_sort)
    return sorted_birthdays

def sort_by_given_name(students_list):
    # lambda function to extract the given name
    sorted_list = lambda student_list: f"{student_list[GIVEN_NAME_INDEX]}"
    sorted_given_name = sorted(students_list, key = sorted_list)
    return sorted_given_name

def sort_by_birth_month_day(students_list):

    def extract_month_and_day(student):
        birthdate_string = student[BIRTHDATE_INDEX]
        # Begins the sort from BIRTHDAY_INDEX and then 5 spaces from that
        month_and_day = birthdate_string[5:]
        return month_and_day
    
    sorted_list = sorted(students_list, key=extract_month_and_day)
    return sorted_list

def print_list(compound_list):
    for element in compound_list:
        print(element)
    print()

if __name__ == "__main__":
    main()