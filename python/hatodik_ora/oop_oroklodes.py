class Ember:
    # self az más programnyelvekben 'this'-ként szerepel (pld. JS, Java, PHP-ban this->objektum
    # unix nyelveken is this->objektum, stb...)
    def __init__(self, nev, kor, magassag):
        self.nev = nev
        self.kor = kor
        if (magassag < 100):
            self.magassag = magassag*100
        else:
            self.magassag = magassag
        print(f"{self.nev} vagyok, {self.kor} éves és {self.magassag}cm magas")

    def alszik(self):
        print(f"{self.nev} alszik")
    def iszik(self):
        print(f"{self.nev} vizet iszik")

    def __del__(self):
        print(f"{self.nev} életciklusa lejárt")

class Kosarlabdazo(Ember):
    #supercharging - konskruktor túltöltés
    def __init__(self, nev, kor, magassag, pozicio ="center"):
        self.pozicio = pozicio
        super().__init__(nev,kor,magassag)
        print(f"Kosárlabdázó vagyok, {pozicio} pozícióban.")

    def kosarlabdazik(self):
        print(f"{self.nev} kosárlabdázik.")
    #overriding
    def iszik(self):
        print(f"{self.nev} sportitalt iszik")



ember = Ember("Gábor", 25, 178)
ember.iszik()
ember.alszik()

kosaras = Kosarlabdazo("Péter", 25, 198)
kosaras.iszik()

def osszehasonlit(ember1, ember2):
    return ember1.nev == ember2.nev

ugyanaz = osszehasonlit(ember, kosaras)
print(ugyanaz)