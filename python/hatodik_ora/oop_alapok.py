#OOP -> Object-Oriented Programming : Objektumorientált Programozás
class Negyzet:
    def __init__(self, a_oldal, neve="Nincs"):
        print(f"Létrehozott négyzet neve: {neve}, {a_oldal}cm oldalmérettel!")
        self.a_oldal = a_oldal
        self.nev = neve
        self.terulet_szamitas()

    def terulet_szamitas(self):
        self.terulet = self.a_oldal * self.a_oldal

    #getter
    def get_terulet(self):
        return self.terulet
    def get_nev(self):
        return self.nev
    #setter
    def set_oldal(self, oldal):
        self.a_oldal = oldal
        self.terulet_szamitas()
    def set_nev(self, nev):
        self.nev = nev



negyzet1 = Negyzet(5, "négyzet_neve")
negyzet2 = Negyzet(9)

print(f"a {negyzet1.get_nev()} területe: {negyzet1.terulet}")
negyzet1.set_oldal(6)
print(f"a {negyzet1.get_nev()} új területe: {negyzet1.terulet}")