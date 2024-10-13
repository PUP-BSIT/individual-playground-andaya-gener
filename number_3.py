# Write a program that takes 3 numbers and prints the highest number.

# Get first number from the user
number_1 = int(input("Please enter the first number: "))

# Get second number from the user
number_2 = int(input("Please enter the second number: "))

# Get third number from the user
number_3 = int(input("Please enter the third number: "))

# condition 1
if number_1 > number_2 and number_1 > number_3:
    print("The biggest number is first number!")

# condition 2
elif number_2 > number_1 and number_2 > number_3:
      print("The biggest number is second number!") 

# condition 3
else:
    print("The biggest number is third number!")