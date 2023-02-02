import sys

while True:
     pwd=input("input password  ")
     if pwd !="skw":
         print("Incorrect password try again pls: ")
     else:
        print("Correct Password Ready to Execute \n")
        while True:
            s = float(input("enter amount"))
            t = float(input("enter amount"))
            v = s / t
            print(v)
            sys.exit()