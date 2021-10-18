a = 15
print(f"Az a értéke: {a}, típusa: {type(a)}, címzése: {id(a)}")
a = "szia"
print(f"Az a értéke: {a}, típusa: {type(a)}, címzése: {id(a)}")

a = 300
b = a
print(f"{id(a)}\n{id(b)}")
print("----")
a = 300
b = 300

print(f"{id(a)}\n{id(b)}")
