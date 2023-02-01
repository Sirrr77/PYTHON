import sys

while True:
     pwd=input("input password  ")
     if pwd !="skw":
         print("Incorrect password try again pls: ")
     else:
        print("Correct Password Ready to Execute \n")
        while True:
            num1 = float(input("enter num1 "))
            num2 = float(input("enter num2 "))
            term = num1-num2+1
            result = (num1+num2)*term/2
            print(result)
            chk=input("Press E to Exit or Enter to continue:  ")
            if((chk=='E') or (chk=='e')):
                sys.exit()