#FELADAT #1: Jött  egy kérés, hogy egyszerre 5x hibalehetőség legyen,
#         valamint,hogyha hibás a tipp, jelezzük a usernek, hogy a titkos szám
#         kisebb, vagy nagyobb, mint a tippje

#FELADAT #2: Legyen a secret number véletlenszerű szám.
#import:
#import random
#alias:
import random as r
#csak egy fgv. importálása
from random import randint


min = 1
max = 15
secret_number = randint(min,max)#r.randint(min,max)
tippek = 0
max_tippek = 5
while tippek < max_tippek:
    tippek = tippek + 1
    user_valasz = input(f"Tippelj egy számra {min} és {max} között!")

    if int(user_valasz) == secret_number:
        print(f"Talált, a helyes megfejtés {secret_number}")
        break
    elif int(user_valasz) < secret_number:
        print(f"Sajnos nem talált, a titkos szám nagyobb, mint {int(user_valasz)}")
    else:
        print(f"Sajnos nem talált, a titkos szám kisebb, mint {int(user_valasz)}")

    if max_tippek == tippek:
        print("Sajnos elvesztetted az összes próbálkozási lehetőséged.")
        print(f"A titkos szám {secret_number} volt.")
