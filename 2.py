#โปรแกรมคำนวณหาค่าเฉลี่ยของเลขสองจำนวน

import sys
import os

while True:
     pwd=input("input password")
     if pwd !="skw":
         print("Incorrect password. Enter again pls: ")
     else:
        print("Correct Password Ready to Execute \n")
        while True:
              print("")
              print("average of numbers")
              num1 = float(input("Enter the amount:  "))
              num2 = float(input("Enter the amount:  "))
              avg = (num1 + num2) / 2
              print('The average of numbers = %0.2f' %avg)
              chk=input("Press E to Exit or Enter to continue:  ")
              if((chk=='E') or (chk=='e')):
                 sys.exit()