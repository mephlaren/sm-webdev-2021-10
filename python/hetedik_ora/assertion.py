import sys

def linux_fgv():
    assert('linux' in sys.platform), "Ez a függvény csak Linux alatt fut le"
    print("Linux függvény")
def windows_fgv():
    assert('win32' in sys.platform), "Ez a függvény csak Windows alatt fut le"
    print("Windows függvény")

def mac_fgv():
    assert('darwin' in sys.platform), "Ez a függvény csak Mac alatt fut le"
    print("Mac függvény")

def szamolas(szam):
    if szam < 15:
        raise Exception("A szám kisebb, mint 15")
    else:
        return szam

try:
    linux_fgv()
except AssertionError as error:
    print(error)
windows_fgv()
szam = 10
try:
    print(szamolas(szam))
except Exception as ex:
    print(f"{str(ex)}, de hozzáadok 15-öt hogy biztos működjön!")
    print(szamolas(szam+15))
