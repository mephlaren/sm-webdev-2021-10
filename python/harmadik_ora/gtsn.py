#FELADAT 3: mentsük ki a pontokat és a játék végén mutassuk meg a top 5 játékost
import random as r
#csak egy fgv. importálása
from random import randint


min = 1
max = 15
secret_number = randint(min,max)#r.randint(min,max)
tippek = 0
max_tippek = 5
pontfajl = "gtsn_pontok.sm"
jatekos = input("Kérlek add meg a neved")

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

vegso_pontok = 100 - ((100*tippek) / 33)
with open(pontfajl, 'a') as kimenet:
    kimenet.writelines(f"\n{jatekos} - {vegso_pontok}")

with open(pontfajl, 'r') as bemenet:
    print("################")
    pontok = bemenet.read().splitlines()
    for pont in pontok:
        if pont != "":
            print(f"### {pont} ###")
    print("################")
