import json
countries = {}
with open("countries.json", "r") as cfile:
    tmp = cfile.read()
    countries = json.loads(tmp)

countries = countries["countries"]

correct = 0
incorrect = 0
for country in countries:
    secret = countries[country]
    guess = input(f"Tippeld meg a fővárosát {country}-nak!")

    if(guess == secret):
        correct = correct+1
        print("Eltaláltad!")
    else:
        incorrect = incorrect + 1
        print("Nem talált!")

print(f"{correct}/{correct+incorrect} helyes megoldás.")