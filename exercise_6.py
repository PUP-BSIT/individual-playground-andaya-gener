
inputted_number = int(input("Please enter a number: "))

if inputted_number % 3 == 0 and inputted_number % 5 == 0:
  print("Bigyan ng jocket!\n")

elif inputted_number % 3 == 0:
  print("Hep! Hep!\n")

elif inputted_number % 5 == 0:
  print("Horaay!\n")

else:
  print(f"{inputted_number} Tawsan!\n")