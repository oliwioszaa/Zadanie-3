#Zadanie 1
num = int(input("Podaj długość ciągu liczb Fibonacciego: "))
a, b = 0, 1
fib = [a, b]
while len(fib) < num:
    a, b = b, a + b
    fib.append(b)

print(fib[:num])

with open("fibonacci.txt", "w") as file:
    file.write(str(fib[:num]))