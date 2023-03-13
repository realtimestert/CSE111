# # Import the sleep function from the time module, so
# # that the sleep function can be used in this program.
# from time import sleep

# # Prompt the user to enter her name.
# name = input("Hello! What is your name? ")

# # Print the numbers 3, 2, 1.
# for i in range(3, 0, -1):
#     print(i, flush=True)
#     sleep(0.5)  # Pause for 1/2 second

# # Use a Python f-string to format a greeting
# # for the user and then print the greeting.
# print(f"Welcome to CSE 111, {name}!")

# Example 7

# Get the cost of an item from the user.
cost = float(input("Please enter the cost: "))

# Determine a discount rate based on the cost.
if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20

# Compute the discount amount
# and the discounted cost.
discount = cost * rate
cost -= discount

# Print the discounted cost for the user to see.
print(f"After the discount, you will pay {cost:.2f}")