# komment

# Változó : INTEGER ( INT ) ( Teljes, egész szám )
# kor: változónév = 25: érték
kor = 25

#Változó: FLOAT ( Lebegőpontos szám )
magassag_meter = 1.78

#Változó: STRING ( Szöveg )
nev = "Gabor"
nev = 'Gabor'
kezdobetu = "G"
kezdobetu = 'G'

#Változó: BOOLEAN ( BOOL ) ( Logikai érték / Igaz-Hamis )
felnott = True
nyugdijas = False

#Változó: NONETYPE ( NONE ) (Nincs típus és üres )
lakas = None
#Változóműveletek
magassag_centi = magassag_meter * 100
magassag_kor_kulonbseg = magassag_centi - kor
#Szöveg-konkatenáció
szoveg = "Szia " + nev
#format-string: dinamikusan beformázzuk a változók értékeit
fstring_szoveg = f"Szia, {nev} vagyok, {kor} éves és {magassag_centi}cm magas"

#Függvény konzolra kiíráshoz
print(fstring_szoveg)