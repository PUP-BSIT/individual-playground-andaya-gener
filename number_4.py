# Write a program that takes a coordinate and tell which quadrant the coordinate falls.

# Get the x-coordinate and y-coordinate from the user
coordinate_1 = float(input("Enter the x-coordinate: "))
coordinate_2 = float(input("Enter the y-coordinate: "))

# condition 1
if coordinate_1 > 0 and coordinate_2 > 0:
    print("first quadrant")

# condition 2
elif coordinate_1 < 0 and coordinate_2 > 0:
    print("second quadrant")

# condition 3
elif coordinate_1 < 0 and coordinate_2 < 0:
    print("third quadrant")

# condition 4 
elif coordinate_1 > 0 and coordinate_2 < 0:
    print("forth quadrant")

# condition 5
else:
     print("The coordinate is at the origin")