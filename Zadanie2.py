#Zadanie 2
wystapnienie_slow = {}

zdanie = input("Napisz zdanie minimum 5 wyrazowe:  ")

słowa = zdanie.split()
if len(słowa) <5:
    print("Zdanie jest za krótkie!!")
else:
    wystapnienie_slow = {}
    
    for słowo in słowa:
        słowo = słowo.strip('.,!?()[]{}"\'')

        wystapnienie_slow[słowo] = wystapnienie_slow.get(słowo, 0) + 1

print(f"{słowo}: {wystapnienie_slow} razy")

with open("Zdanie.txt", "w") as file:
    for słowo, wystapnienie in wystapnienie_slow.items():
        print(f"{słowo}: {wystapnienie} razy", file=file)