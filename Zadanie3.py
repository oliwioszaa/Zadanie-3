#Zadanie 3
liczba_tablicy = int(input("Podaj liczbę tablicy: "))
max_liczba = int(input("Podaj maksymalną liczbę do wygenerowania: "))

tablica = list(range(1, max_liczba + 1))

print(f"Tablica {liczba_tablicy}: {tablica}")

with open("tablica.txt", "w") as file:
    print(f"Tablica {liczba_tablicy}: {tablica}", file=file)