import sys

while True:
     pwd=input("input password  ")
     if pwd !="skw":
         print("Incorrect password try again pls: ")
     else:
        print("Correct Password Ready to Execute \n")
        while True:
            karat = float(input("enter amount"))
            result = karat * 200
            print("result", result ,"milligram")