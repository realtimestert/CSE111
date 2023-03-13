import csv
from datetime import datetime
current_date_and_time = datetime.now(tz = None)

def main():

    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    #Show all products but without the first line
    product_dict = read_dictionary("products.csv", PRODUCT_INDEX)
    # print("All Products")
    # print(product_dict)
    # print()
    number_of_items = 0


    request_dict = read_dictionary("request.csv", PRODUCT_INDEX)
    #printing requested items, but without the product number
    # print("Requested Items")
    # print(request)

    print("Inkom Emporium")
    print()
    
    with open("request.csv", "rt") as csv_request:
        reader = csv.reader(csv_request)
        next(reader)
        for item in reader:
            key = item[0]
            quantity = item[1]
            number_of_items += int(quantity)
            #print(item)
            value = product_dict[key]
            #print(value)
            name = value[1]
            price =  value[2]
            print(f"{name} {quantity} {price}")
        print(number_of_items)


        try:            
            dictionary = {
                "W112":"2",
                "D083":"4",
                "W231":"1",
                "C013":"2",
                "D083":"3"
                }
            name = dictionary["W112"]
            
        except KeyError as key_err:
            print("Error: unknown product ID in the request.csv file")
            print(type(key_err).__name__, key_err)

        except FileNotFoundError as not_found_err:
            print(not_found_err)

    with open("products.csv", "rt") as csv_products:
        reader = csv.reader(csv_products)
        next(reader)
        for item in reader:
            key = item[0]
            price = item[2]
            value = request_dict[key] #I don't know how to fix the KeyError here
            
            number_of_items = sum(value[1]) 
            subtotal = sum(item[2]) 
            sales_tax = sum(item[2])*.165
            total = subtotal + sales_tax
            
            print(number_of_items) #12
            print(f"{subtotal:.2f}") #15.26
            print(f"{sales_tax:.2f}") #0.92
            print(f"{total:.2f}") #16.18

        # for items in reader:
        #     key = items[0]
        #     quantities = sum(item[1])
        
        #     print(f"Number of items: {quantities}") #12
        #     print(f"Subtotal: {price}") #15.26
        #     print(f"Sales tax: {price}") #0.92
        #     print(f"Total: {price}") #16.18

    print()
    print("Thank you for shopping at the Inkom Emporium.")
    
    #date format
    #Fri Mar 10 09:30:45 2023
    print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")

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

if __name__ == "__main__":
    main()
