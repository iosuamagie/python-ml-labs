#Exercitiul 2
import random
nota = int(input("Nota examen: "))
nota_valide=list(range(1,11))

while nota not in nota_valide:
    nota=int(input("Reintrodu nota examen: "))
if nota<5:
    print("Reexaminare")
elif nota <= 6:
    print("Suficient")
elif nota <=8:
    print("Bine")
else:
    print("Excelent")

#Exercitiul 3
import random
numar=random.randint(1, 50)

incercari=0
ghicit=False

while not ghicit:
    incercare=int(input("Ghiceste Numarul (1-50):"))
    incercari +=1
    if incercare < numar:
        print("numarul este mai mare")
    elif incercare > numar:
        print("numarul este mai mic")
    else:
        print(f"Felicitari! Ai ghicit numarul in {incercari} incercari")
        ghicit=True

#Exercitiul 4
orase = ["Bucuresti", "Cluj-Napoca", "Timisoara", "Iasi"]
for index, oras in enumerate(orase):
    print(f"{index+1}.{oras}")

#Exercitiul 5
import random
print("Alege 6 numere între 1 si 49")
numere_alese = []
for i in range(1, 7):
    numar_valid = False
    while not numar_valid:
        numar = int(input(f"Numărul {i}: "))
        if 1 <= numar <= 49:
            if numar not in numere_alese:
                numere_alese.append(numar)
                numar_valid = True
            else:
                print("Ai ales deja acest numar, alege altul")
        else:
            print("Introdu un numar intre 1 si 49")

numere_extrase = random.sample(range(1, 50), 6)
numere_ghicite = []

for numar in numere_alese:
    if numar in numere_extrase:
        numere_ghicite.append(numar)

print(f"\nNumere extrase: {numere_extrase}")

numar_de_ghicite = len(numere_ghicite)

if numar_de_ghicite > 0:
    print(f"Ai ghicit {numar_de_ghicite} numere: {numere_ghicite}")
    if numar_de_ghicite == 6:
        print("Ai ghicit toate numerele!")
    elif numar_de_ghicite >= 4:
        print("Felicitari! Ai castigat un premiu consistent!")
    elif numar_de_ghicite == 3:
        print("Felicităai! Ai castigat un premiu mic!")
    else:
        print("Trebuie sa ghicesti minim 3 numere pentru un premiu.")
else:
    print("Nu ai ghicit niciun numar. Mai mult noroc data viitoare!")

#Exercitiul 7
cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
cuvinte_negative = ["urat", "prost", "groaznic", "dezamagitor"]
comentariu = input("Introdu comentariul tău: ").lower()

este_pozitiv = False
este_negativ = False
for cuvant in cuvinte_pozitive:
    if cuvant in comentariu:
        este_pozitiv = True
        break
for cuvant in cuvinte_negative:
    if cuvant in comentariu:
        este_negativ = True
        break
if este_pozitiv and not este_negativ:
    print("Comentariu pozitiv!")
elif este_negativ and not este_pozitiv:
    print("Comentariu negativ!")
elif este_pozitiv and este_negativ:
    print("Comentariu mixt (conține atât cuvinte pozitive, cât și negative).")
else:
    print("Comentariu neutru.")
