
class Jarmu:
    def __init__(self, kerekek, szin, max_sebesseg):
        self.kerekek = kerekek
        self.szin = szin
        self.sebesseg = max_sebesseg

    def halad(self,tavolsag):
        return round((tavolsag / self.sebesseg), 2)
    #getterek
    def get_kerekek(self):
        return self.kerekek
    def get_szin(self):
        return self.szin
    def get_sebesseg(self):
        return self.sebesseg
    #setterek
    def set_kerekek(self, kerekek):
        self.kerekek = kerekek
    def set_szin(self, szin):
        self.szin = szin
    def set_sebesseg(self, sebesseg):
        self.sebesseg = sebesseg

class Bicikli(Jarmu):
    def pumpal(self):
        print(f"A bicikli kerekét épp felpumpálják")
class Lovaskocsi(Jarmu):
    def etet(self):
        print(f"A lovakat épp etetik")

jarmu = Jarmu(4, "piros", 65)
print(f"5km ennyi idő alatt: {jarmu.halad(5)*60}")
print(f"32km ennyi idő alatt: {jarmu.halad(32)*60}")
print("--------------------")
b1 = Bicikli(2, "fekete", 15)
b1.pumpal()
print(f"40km-et ennyi idő alatt lehet vele lebiciklizni: {b1.halad(40)*60}")
b1.set_sebesseg(30)
print(f"Ha tudok menni {b1.get_sebesseg()}km/h sebességgel, akkor a 40km csak {b1.halad(40)*60}")
print("--------------------")
l1 = Lovaskocsi(4, "barna", 6)
l1.etet()

