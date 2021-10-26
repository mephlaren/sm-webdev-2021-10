#a szótárban key-value párokat keresünk
dict1 = {
    'alma':'gyümölcs',
    'banán':'gyümölcs',
    'káposzta': 'zöldség',
    'répa': 'zöldség',
    'hagyma':'zöldség',
    'csirke':'hús'
}

print(dict1)
print(type(dict1))
print(len(dict1))

print(f"A \"répa\" kulcs értéke: {dict1['répa']}")
#print(f"Az 1. index értéke: {dict1['ötlet']}") #-> erre hibát dob, mert csak létező kulcsra kereshetek.

for i in dict1:
    kulcs = i
    #print(f"A következő kulcs: {kulcs}")
    #print(f"A kulcs értéke: {dict1[kulcs]}")

darabolas = dict1.items()
for key, value in darabolas: #a key az étel a value a tipus
    print(f"A {key} étel típusa: {value}")

#probléma: megkéne tudnom, hány értékem van és hányszor fordulnak elő a dict1 szótárban
#1. lépés: kigyűjtöm az adatok
#2. lépés: összeszámolom az adott értékek a szótárban hányszor fordulnak elő
#3. lépés: kiírom a megoldást

#print(dict1.keys()) -> nem jó, mert az értékek adják meg a kategóriát
ertekek = dict1.values()
kategoriak = []
eredmeny_dict = {}
tmp_index = 1
tmp_kategoria = None

for ertek in ertekek:
    if ertek == tmp_kategoria:
        if ertek not in kategoriak:
            kategoriak.append(ertek)
        tmp_index = tmp_index + 1
    else:
        tmp_index = 1
    tmp_kategoria = ertek
    eredmeny_dict[tmp_kategoria] = tmp_index

osszes_ertek = 0
legnagyobb_kategoria = ""
tmp_legnagyobb = -9999

for kulcs, ertek in eredmeny_dict.items():
    print(f"A {kulcs} kategória {ertek} alkalommal szerepel")
    osszes_ertek = osszes_ertek + ertek
    if ertek > tmp_legnagyobb:
        tmp_legnagyobb = ertek
        legnagyobb_kategoria = kulcs

szazalek = (tmp_legnagyobb/osszes_ertek)*100

print(f"Összessen {osszes_ertek} elemem van")
print(f"A legnagyobb értékű kategória: {legnagyobb_kategoria}"
      f" ({tmp_legnagyobb} eleme van, ami a totál {szazalek}%-a)")

import json
#dumps és loads -> a objektumot kirakja json objektummá, vagy vissza python objektummá
json_eredmeny = json.dumps(eredmeny_dict)
dict_json_eredmeny = json.loads(json_eredmeny)
print(f"JSON formátumban az eredmény: {json_eredmeny}")
print(f"Python szótárrá visszakonvertálva: {dict_json_eredmeny}")