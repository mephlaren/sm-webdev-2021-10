#open(filepath, mode) -> paraméterként fogadja a fájlt, és annak megnyitási módját
#olvasási mód: 'r' -> read
#beolvassa a fájl TELJES tartalmát

#írási mód: 'w' -> write
#x------
#-------
#-------
#-------
#----|
#mindig egy adott pontot áll meg a kurzor, ezért olvasni nem tud
#minden fájlnyitásnál a kurzor a 0. biten fog megállni (a fájl legelején)

#hozzáfűzés: 'a' -> append
#-------
#-------
#-------
#-------
#----x
# ebben a módban a kurzor mindig a fájl legutolsó bitjénél kezdi az írást

#relatív útvonal:
fajlnev = "teszt.sm"

#a fájl abszolút útvonala:
import os
szkript_helye = os.path.abspath(__file__)
fajlhely = os.path.dirname(szkript_helye)
fajlhely = f"{fajlhely}\\{fajlnev}"

#megnyitom a fájlt
fajlhely = open(fajlhely, 'r')
#beolvasom a fájlt
beolvasott = fajlhely.read()
index = 0
#a sorokra bontott fájlon végigmegyek elemenként
for sor in beolvasott.splitlines():
    index = index + 1
    print(f"{index}. sor értéke: {sor}")
fajlhely.close()