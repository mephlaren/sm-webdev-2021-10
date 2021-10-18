#print(szoveg) -> kiírja az átadott szöveget a konzolra
#input(szoveg) -> kiírja az átadott szöveget a konzolra, és vár user inputra
#Az input függvény visszatérési értéke, az minding string
#usernev = "Szia, megkérdezhetem a neved?\n"
#nev_input = input(usernev)
#usermagassag = "És hány centi magas vagy?\n"
#magassag_input = int(input(usermagassag))
#print(f"\tSzia, {nev_input}, {magassag_input/100} méter magas vagy")

#Téglalap kerület/terület számláló
#T = a*b
#K = 2*(a+b)

print("Szia, kérlek add meg a téglalap A és B oldalát és megmondom a tulajdonságait.")
a = float(input("Kérlek, add meg az A oldalt.\t"))
b = float(input("Kérlek, add meg a B oldalt.\t"))

t = a*b
k = 2*(a+b)
print(f"\nA terület: {t}\nA kerület: {k}")