"""
*******************************************************************************
Filename:       2_livehack_practice_solution2.py
Description:    Compute the destination of a student based on marks and earnings
Author:         Lin.O
Created On:     12/02/2021
*******************************************************************************
"""
#get mark and earnings before the summer 
mark = float(input("Mark: "))
earnings_before_the_summer = float(input("Earnings before the summer: "))

#compute and result 
if mark >= 80 and earnings_before_the_summer >= 500: 
  print("You can go to Europe!")
elif mark >= 80:
  print("You can go to California!")
else:
  print("You cannot go anywhere! ")