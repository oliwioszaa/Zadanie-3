#Zadanie 3
liczba_tablicy = int(input("Podaj liczbę tablicy: "))
max_liczba = int(input("Podaj maksymalną liczbę do wygenerowania: "))

tablica = list(range(1, max_liczba + 1))
roznica = max_liczba - liczba_tablicy

if max_liczba > liczba_tablicy:
    tablica = list(range(1, max_liczba))

if max_liczba > liczba_tablicy:
    print(f"Tablica {liczba_tablicy}: {tablica}")
else:
    print(f"Tablica {liczba_tablicy}: {tablica}")

with open("tablica.txt", "w") as file:
    print(f"Tablica {liczba_tablicy}: {tablica}", file=file)