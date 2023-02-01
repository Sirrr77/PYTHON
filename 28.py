#แปลงค่าอุณหภูมิจากหน่วยฟาเรนไฮต์เป็นหน่วยเคลวิน

import sys

while True:
     pwd=input("input password  ")
     if pwd !="skw": #รหัสผ่าน
         print("Incorrect password try again pls: ") #ถ้ารหัสถูกจะรันโค้กให้
     else:
        print("Correct Password Ready to Execute \n") #ถ้ารหัสผิดจะให้ใส่ไหม่

        while True:
            Fahrenheit= float(input("Enter temperature in Fahrenheit: "))
            Kelvin = 5/9 * (Fahrenheit - 32) + 273.15
            print("The temperature in Kelvin is:",round(Kelvin,2))
            chk=input("Press E to Exit or Enter to continue:  ")
            if((chk=='E') or (chk=='e')):
                sys.exit()
