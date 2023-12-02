#Zadanie 5
ciag = input("Podaj losowy ciąg znaków: ")
tablice = []

for i in range(4, 8):
    tablica = [ciag[j:j+i] for j in range(0, len(ciag), i)]
    tablice.append(tablica)

for i, tablica in enumerate(tablice, start=4):
    print(f"Długość {i}:", tablica)

with open("ciag.txt", "w") as file:
    for i, tablica in enumerate(tablice, start=4):
        file.write(f"Długość {i}: {str(tablica)}\n")