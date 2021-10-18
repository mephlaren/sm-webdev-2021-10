hely = "teszt.sm"
# a with megfelelője : fajl = open(hely, 'r')
with open(hely, 'r') as fajl:
    index = 0
    for sor in fajl.read().splitlines():
        index = index + 1
        print(f"{index}. sor értéke: {sor}")

with open(hely, 'w') as fajl:
    fajl.write('hello\n')

with open(hely, 'a') as fajl:
    fajl.write('hello2\n')