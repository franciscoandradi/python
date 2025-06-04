numeros = []
pares = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print("Números pares:", pares)
