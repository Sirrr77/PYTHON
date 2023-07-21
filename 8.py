import sys

while True:
     pwd=input("Enter password  ")
     if pwd !="รหัสตั้งตามใจ":
         print("Invaild password pls try again  ")
     else:
        printSlow("Correct Password \n")
num1=float(input("โปรดป้อนค่าเอเคอร์:")
result=num1*2.529285
print(f'{num1}*{2.529285}={result}')
print("ผลลัพธ์ค่าของไร่: %s"%(result))
chk=input("Press E to Exit or Enter to continue: ")
if((chk=='E')or(chk=='e')):
sys.exit()
