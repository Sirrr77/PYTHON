#1โปรแกรมคำนวณหาปริมาตรทรงสี่เหลี่ยมมุมฉาก

import sys

while True:
     pwd=input("input password")
     if pwd !="skw":
         print("Incorrect password. Enter again pls: ")
     else:
        print("Correct Password Ready to Execute \n")
        
        while True:
            height=float(input("input height :"))
            width=float(input("input width :"))
            length=float(input("input length :"))
            volume=height*width*length
            print(f'{height} * {width} * {length} = {volume} ')
            chk=input("Press E to Exit or Enter to continue:  ")
            if((chk=='E') or (chk=='e')):
                sys.exit()