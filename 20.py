import sys

while True:
     pwd=input("input password  ")
     if pwd !="skw":
         print("Incorrect password try again pls: ")
     else:
        print("Correct Password Ready to Execute \n")
        while True:
            yard = float(input("enter amount  "))
            result = yard * 0.9144
            print("result", result ,"yard")