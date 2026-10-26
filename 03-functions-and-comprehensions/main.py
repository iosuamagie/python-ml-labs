# Exercitiul 1
def joaca_rps():
    while True:
        print("\n--- Rock, Paper, Scissors ---")
        j1 = input("Jucator 1 (piatra/hartie/foarfeca): ").lower()
        j2 = input("Jucator 2 (piatra/hartie/foarfeca): ").lower()

        optiuni_valide = ["piatra", "hartie", "foarfeca"]

        if j1 not in optiuni_valide or j2 not in optiuni_valide:
            print("Optiuni invalide! Incercati din nou.")
            continue

        if j1 == j2:
            print("Egalitate!")
        elif (j1 == "piatra" and j2 == "foarfeca") or \
                (j1 == "foarfeca" and j2 == "hartie") or \
                (j1 == "hartie" and j2 == "piatra"):
            print("Felicitari Jucator 1! Ai castigat.")
        else:
            print("Felicitari Jucator 2! Ai castigat.")

        nou_joc = input("Doriti sa incepeti un nou joc? (da/nu): ").lower()
        if nou_joc != "da":
            print("Joc incheiat. O zi buna!")
            break

# Exercitiul 2: Generare factura cu **kwargs
def genereaza_factura(nume_client, **kwargs):
    print(f"\nFactura pentru: {nume_client}")
    total = 0
    for produs, pret in kwargs.items():
        total += pret
        print(f"{produs}, pret: {pret}")
    return total


suma_totala = genereaza_factura("Ion", paine=10, chifle=3)
print(f"Total de plata: {suma_totala} RON")


# Exercitiul 3: Normalizare date
def normalize_data(data):
    if not data:
        return []
    min_val = min(data)
    max_val = max(data)
    if min_val == max_val:
        return [0.0 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]

data = [10, 20, 30, 40, 50]
normalized_data = normalize_data(data)
print(f"\nEx 3 Normalizare: {normalized_data}")

# Exercitiul 4: Expresie lambda ridicare la patrat
my_list_4 = [1, 2, 3]
rezultat_4 = list(map(lambda a: a * a, my_list_4))
print(f"\nEx 4 Ridicare la patrat: {rezultat_4}")

# Exercitiul 5: Sortare lista de tupluri
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
sorted_a = sorted(a, key=lambda x: x[1])
print(f"\nEx 5 Sortare tupluri: {sorted_a}")

# Exercitiul 6: Filtrare lista cu lambda si filter()
orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x % 2 == 0, orig_list))
odd_list = list(filter(lambda x: x % 2 != 0, orig_list))

print(f"\nEx 6 Numere pare: {even_list}")
print(f"Ex 6 Numere impare: {odd_list}")

# Exercitiul 7: Eliminare None si reducere 10%
preturi = [100, None, 50, None, 200, 10]
preturi_valide = filter(lambda x: x is not None, preturi)
preturi_reduse = list(map(lambda x: x * 0.9, preturi_valide))
print(f"\nEx 7 Preturi reduse (-10%): {preturi_reduse}")

# Exercitiul 8: Extragere data si ora cu Lambda
data_str = "2023-04-24 09:03:32.744178"
extrage_data = lambda s: (s[:4], s[5:7], s[8:10], s[11:])

an, luna, zi, ora = extrage_data(data_str)
print("\nEx 8 Extragere din string:")
print(f"{an}\n{luna}\n{zi}\n{ora}")

# Exercitiul 9: Suma elementelor a doua liste cu zip()
def sum_lists(l1, l2):
    return [x + y for x, y in zip(l1, l2)]

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
print(f"\nEx 9 Suma liste: {sum_lists(list1, list2)}")

# Exercitiul 10: List Comprehension
print("\n--- Ex 10: List Comprehension ---")
listPare = [i for i in range(0, 101, 2)]  # Numere pare de la 0 la 100
print(f"Pare: {listPare[:10]}")

listCubs = [i ** 3 for i in range(1, 11)]  # Cuburile primelor 10 numere intregi
print(f"Cuburi: {listCubs}")

lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
listComune = [x for x in lista_a if x in lista_b]  # Elementele comune
print(f"Elemente comune: {listComune}")

# Exercitiul 11: Set Comprehension
print("\n--- Ex 11: Set Comprehension ---")
set_pare = {x for x in range(0, 20, 2)}
print(f"Primele 10 pare: {set_pare}")

text_set = "laborator"
set_litere = {char for char in text_set}
print(f"Litere distincte: {set_litere}")

text_cuvinte = "Python este un limbaj usor dar kahootul este greu"
set_cuvinte = {cuvant for cuvant in text_cuvinte.split() if len(cuvant) >= 5}
print(f"Cuvinte >= 5 litere: {set_cuvinte}")

# Exercitiul 12: Dictionary Comprehension
print("\n--- Ex 12: Dictionary Comprehension ---")
dict_patrate = {x: x ** 2 for x in range(1, 11)}
print(f"Patrate: {dict_patrate}")

text_dict = "abracadabra"
dict_litere = {char: text_dict.count(char) for char in text_dict}
print(f"Aparitii litere: {dict_litere}")

dict_divizori = {x: [y for y in range(1, x + 1) if x % y == 0] for x in range(1, 11)}
print(f"Divizori: {dict_divizori}")