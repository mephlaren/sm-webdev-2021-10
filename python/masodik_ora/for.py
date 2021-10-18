#python ciklusok - for
start=0
stop=15
#i,j,k
#for i in range(start, stop+1):
#    print(f"{i+1} futás értéke: {i}")
string = "Szia, Gábor vagyok"
string_out = "";
for j in string:
    if (j != " "):
        if (j != "," and j!="." and j!="?" and j!="!"):
            string_out = string_out + j.lower()

#print(string_out)

#Nézzük meg egy szövegben mennyi ascii karakter van!
#Beágyazott ciklusok: A külső ciklusban léptetjük egyesével az ascii karaktereket
#A belső ciklusban pedig ellenörizzük, hogy a szöveg tartalmazza-e
#Ha igen, növeljük a találatot, ha a találat hossza == a bement hosszával,
#Akkor biztos, hogy csak ascii karakterek vannak benne
ascii_karakterek = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
bemenet = input("Kérlek, adj meg egy szöveget!\n")

talalat = 0
hossz = len(bemenet)

for ascii in ascii_karakterek:
    for karakter in bemenet:
        egyezoseg = ascii.lower() == karakter.lower()
        if egyezoseg == True and karakter != " ":
            talalat = talalat + 1

if hossz == talalat:
    print("\tCsak ascii karakter van a szövegben")
else:
    print("\tNem csak ascii karakter van a szövegben")


for i in range(1,10+1):
    for j in range(1,10+1):
        print(f"{i}*{j}: \t{i*j}")


