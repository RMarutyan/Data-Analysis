'''
Homework Task:
1. Write a Python script to calculate the area of a rectangle given its length and
width as inputs.
2. Add a feature to check if the area is greater than or equal to 100. If the area is
less than 100, print a message, “The area is too small.”
3. Save the final script as rectangle_area.py.
'''

length=10
width=5
area = length * width
if area >= 100:
    print ("The area of the rectangle is", area, "and it is large enough.")
else:
    print ("The area of the rectangle is", area, "and the it is too small.")

#Version 2 with input

input_length = float(input("Enter the length of the rectangle: "))
input_width = float(input("Enter the width of the rectangle: "))    
area_with_input = input_length * input_width
if area_with_input >= 100:
    print ("The area of the rectangle is", area_with_input, "and it is large enough.")
else:
    print ("The area of the rectangle is", area_with_input, "and the it is too small.")

