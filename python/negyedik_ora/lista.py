var1 = 5
var2 = 6
var3 = 7

#list1 = [5,6,7]
list1 = [var1,var2,var3]
print(type(list1))
print(list1)

list2 = []
list2.append(12)
list2.append(8)
list2.append(13)
list2.append(11)
print(f"A 2. lista elemei: {list2}")
list2.reverse()
print(f"A 2. lista reverse értéke: {list2}")
list2.sort()
print(f"A 2. lista rendezve: {list2}")
print(f"A 2. lista elemszáma: {len(list2)}")

#slicing -> elkapni egy allistát (subsetet) valamilyen irányból
print(list2[0]) # -> az értéke 8, mert a 0. index az első eleme a listának
list2.pop()
print(f"A 2. lista utolsó eleme nélkül: {list2}")
list2.pop(0)
print(f"A 2. lista első eleme nélkül: {list2}")

#for
list3 = [4,9,14,8,11,10,24,65]
lista3_meret = len(list3)
for index in range(0, lista3_meret):
    pass
    #print(f"A list3 {index}. indexén a {index+1}. elem: {list3[index]}")

#foreach
index = 0
for elem in list3:
    print(f"Az aktuális elem: {elem}, az indexe: {index}")
    index = index + 1

print("Töröljünk a list3-ból minden elemet, aminek az értéke 10, vagy nagyobb")
print("A törölt értékeket gyűjtsük külön listába")

lista3_meret = len(list3)
torolt_elem = []
for el in range(0, lista3_meret):
    ertek = list3[el]
    if ertek >= 10:
        torolt_elem.append(el)

for torolnivalo in torolt_elem:
    pass
    #list3.pop(torolnivalo)

list3.sort()
print(f"A lista3 elemei: {list3}")
elso_index = 0
for index in range(0, len(list3)):
    if (list3[index] >= 10):
        elso_index = index
        break
print(f"A számok, amik kisebbek, mint 10: {list3[:elso_index]}")
torolt_elem = list3[elso_index:]
print(f"A törölt elemek: {torolt_elem}")

print("többdimenziós lista: ")
tdlist = [
    [0,0], [0,1], [0,2],
    [1,0], [1,1], [1,2],
    [2,0], [2,1], [2,2],
]
print(tdlist)
print(tdlist[1])
print(tdlist[1][1])