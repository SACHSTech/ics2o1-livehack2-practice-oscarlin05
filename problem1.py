"""
*******************************************************************************
Filename:       2_livehack_practice_solution1.py
Description:    Determine if a triangle is a right angle triangle
Author:         Lin.O
Created On:     12/02/2021
*******************************************************************************
"""
#get 3 sides for the triangle 
side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

#compute and result 
if (side1**2) + (side2**2) == side3**2:
  print("The triangle with side lengths " + str(side1) + ", " + str(side2) + ", " + str(side3) + ", " + str("form a right-angled triangle. "))
else:
  print("The triangle with side lengths " + str(side1) + ", " + str(side2) + ", " + str(side3) + ", " + str("does not form a right-angled triangle. "))