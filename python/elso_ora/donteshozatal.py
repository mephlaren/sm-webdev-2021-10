#if-else elágazás
#if 1==1:
#    pass
#min_kor = 18
#max_kor = 40
#user_kor = int(input("Hány éves vagy?\n"))

#if min_kor <= user_kor and user_kor < max_kor:
#    print("Beléphetsz")
#elif user_kor>max_kor:
#    print("Túl idős vagy.")
#else:
#    print("Túl fiatal vagy.")
#print("Program vége.")

print("Szia, kérlek add meg a téglalap A és B oldalát és megmondom a tulajdonságait.")
a = float(input("Kérlek, add meg az A oldalt.\t"))
b = float(input("Kérlek, add meg a B oldalt.\t"))

if a == b:
    print("Dehát ez egy négyzet...")
else:
    t = a*b
    k = 2*(a+b)
    print(f"\nA terület: {t}\nA kerület: {k}")