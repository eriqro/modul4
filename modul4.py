import os
os.system('cls')
import math
import time
import random
length=int(input("Hur lång är du?: "))
if length>=110:
    print("Du får åka!")
else:
    print("Du får inte åka")
a=True
while a:
    try:
        namn=input("Vad heter du?: ")
        age=int(input("Hur gammal är du?: "))
        print(f"Hej {namn} du är {age} år gammal")
        a=False
    except ValueError:
        print("Du måste använda nummer för din ålder")
a=True
while a:
    try:
        e=int(input("Hur mycket väger du i kg?: "))
        print(f" ")
        f=int(input("Hur lång är du i cm?: "))
        print(f" ")
        f=f/100
        g=e/f**2
        print(f"Ditt bmi är {g}")
        a=False
    except ValueError:
        print("Använd nummer och inte bokstäver för din längd och vikt snälla")
        print(f" ")

print("uträkning på cirkels area")
time.sleep(1)
r=int(input("Hur stor är radien på cirklen?: "))
area=r*r*math.pi
print(f"Arean på cirkeln är {area} ")


accepted = "*/+-"

a=True
while a:
    try:
        x=int(input(f"Välja x i   x räknesätt y: "))
        time.sleep(0.2)
        y=int(input(f"Välja y i   x räknesätt y: "))
        a=False
    except ValueError:
        print(f"\nAnvänd nummer\n")

a=True
while a:
    time.sleep(0.2)
    b=input(f"\nOlika räkna sätt \nAddition + \nSubtraction - \nMultiplication * \nDivition / \nVad vill du använda?: ")
    if b in accepted:
        if b=="+":
            
            print(f"Ditt svar blev {z+y}")
            a=False
        elif b=="-":
            z=x-y
            print(f"Ditt svar blev {z-y}")
            a=False
        elif b=="*":
            z=x*y
            print(f"Ditt svar blev {z*y}")
            a=False
        elif b=="/":
            z=x/y
            print(f"Ditt svar blev {z/y}")
            a=False
    else:
        print(f"\nSnälla använd någon av dem som visades\n")
        time.sleep(0.5)

time.sleep(0.5)
a=True
svar=input("Vill du använda tärning?: ")
while a:
    if svar=="ja":
        b=random.randint(1,6)
        print(f"Tärningen visa {b}")
        c=input("Vill du köra igen? ja/nej: ")
        if c=="nej":
            a=False

