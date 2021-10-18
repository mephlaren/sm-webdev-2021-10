#PROGRAM: bekér egy számot és egy állatot és ellenörzi, hogy annyi van-e a farmon

szam = int(input("Állatok száma\n"))
allat = input("Állat fajtája?")

max_allat = 5

if szam <= max_allat and ( allat == "Kutya" or allat == "Ló" or allat == "Macska" ):
    print("Igen, ilyen állat van itt, legalább ilyen mennyiségben.")
elif szam > max_allat:
    print("Lehet, hogy van itt ilyen állat, de biztos nem ilyen mennyiségben")
else:
    print("Ilyen állatunk nincs ")
