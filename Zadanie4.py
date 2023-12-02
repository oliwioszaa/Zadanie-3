#Zadanie 4
def palindrom(slowo):
    slowo = slowo.lower()
    return slowo == slowo[::-1]

dane = input("Podaj słowa aby sprawdzić czy to palindromy: ")

slowa = dane.split()

with open("palindromy.txt", "w") as file:
    for slowo in slowa:
        if palindrom(slowo):
            print(f"{slowo} to palindrom!")
        else:
            print(f"{slowo} to nie palindrom.")

with open("palindromy.txt", "w") as file:
    for slowo in slowa:
        if palindrom(slowo):
            file.write(f"{slowo} to palindrom, ")
        else:
            file.write(f"{slowo} to nie palindrom, ")
