#โปรแกรมแปลงค่าน้ำหนักจากหน่วยตันเป็นหน่วยกิโลกรัม

import sys

while True:
     pwd=input("input password  ")
     if pwd !="skw":
         print("Incorrect password try again pls: ")
     else:
        print("Correct Password Ready to Execute \n")

        while True:
            kilo = float(input("Enter amount  "))
            result = kilo * 1000
            print("result = ", result, "kilo")
            chk=input("Press E to Exit or Enter to continue:  ")
            if((chk=='E') or (chk=='e')):
                sys.exit()