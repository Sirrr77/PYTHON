import sys

while True:
     pwd=input("input password  ")
     if pwd !="skw":
         print("Incorrect password try again pls: ")
     else:
        print("Correct Password Ready to Execute \n")
        while True:
            km = float(input("Enter amount:"))
            ac = km**2 * 247.105381
            print(ac)