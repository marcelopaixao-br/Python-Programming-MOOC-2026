limite = int(input("Limite: "))
soma = 0
numero = 1
conta = ""

while soma < limite:
    soma += numero
    if conta == "":
        conta = f"{numero}"
    else:
        conta += f" + {numero}"
    numero += 1

print(f"The consecutive sum: {conta} = {soma}")