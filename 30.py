import sys

while True:
     pwd=input("input password  ")
     if pwd !="skw":
         print("Incorrect password try again pls: ")
     else:
        print("Correct Password Ready to Execute \n")
        while True:
            kj = float(input("enter"))
            result = kj * 0.948
            print(result)
            chk=input("Press E to Exit or Enter to continue:  ")
            if((chk=='E') or (chk=='e')):
                sys.exit()
