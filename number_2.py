# Write a program that takes a number and tell whether the number is odd, even, or zero.

# Get an integer number from the user
number_1 = int(input("Please enter a number: "))

# Used if-else-if statement
if number_1 == 0:
    # Print the statement below!
    print("The number inputted is Zero!")

elif number_1 % 2 == 0:
    # Print the statement below!
    print("The number inputted is even!")

else:
    # Print the statement below!
    print("The number inputted is odd!")