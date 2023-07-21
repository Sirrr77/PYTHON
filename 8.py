import sys

while True:
     pwd=input("input password  ")
     if pwd !="skw":
         print("Incorrect password try again pls: ")
     else:
        print("Correct Password Ready to Execute \n")
        while True:
             num1=float(input("โปรดป้อนค่าเอเคอร์:")
                        result=num1*2.529285
             print(f'{num1}*{2.529285}={result}')
             print("ผลลัพธ์ค่าของไร่: %s"%(result))
             chk=input("Press E to Exit or Enter to continue: ")
             if((chk=='E')or(chk=='e')):
                  sys.exit()
