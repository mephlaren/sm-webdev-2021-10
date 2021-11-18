def osztas(a,b):
    #try - catch
    try:
        return a / b
    except ZeroDivisionError:
        print("Nullával nem osztunk.")
        return 0
    except ValueError:
        print("Kérlek, számot adj meg!")
    #finally:
    #    print("Végzett a try-catch")

try:
    szam1 = input('Adj meg egy számot\n')
    szam2 = input('Adj meg még egy számot!\n')

    print(osztas(szam1, szam2))
