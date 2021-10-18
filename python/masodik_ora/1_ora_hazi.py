#adjunk meg egy titkos számot
#olvassunk be user bemenetet és nézzük meg, hogy a user eltalálta-e a számot.

secret_number = 7
guess = int(input("Tippeld meg a számot!"))

talalt = "Helyes válasz,  talált!"
hibas = "Sajnos ez nem nyert."

uzenet = f"A helyes válasz {secret_number} volt."

if (secret_number == guess):
    print(f"{talalt}")
else:
    print(f"{hibas} {uzenet}")