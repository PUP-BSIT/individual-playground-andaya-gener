#Write a program that takes a 2 digit number and returns the sum of the 2 digits.

# Input for 2 digit number
digit_number = int(input("Please enter 2 digit number: "))

# Extracting the digits
digit_1 = digit_number // 10
digit_2 = digit_number % 10

# Calculating the sum of the digits 
sum = digit_1 + digit_2

# Ouput the sum
print(f"The sum of 2 digits is: {sum}\n")