print("Hello stranger, care to convert some metric to imperial? (kgs to lbs)")

while True:
    user_amount = int(input("Enter amount to be converted:"))
    kg_to_lb = 2.20462262
    result = user_amount * kg_to_lb
    print(f"\t Thanks for your input. {user_amount} kgs equals {result} lbs")

    choice = input("Convert something else for you, m'lord? (yes/no)")

    if choice != "yes":
        print("Thank you m'lord. Safe travels!")
        break
    # else:
    #
    # else:
    #    print("Afraid you need to be more specific...")