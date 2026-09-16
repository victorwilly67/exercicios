leituras = []
quantidade = int(input("Quantas Leituras? "))

for i in range(quantidade):
    valor = float(input(f"Leitura {i + 1}: "))
    leituras.append(valor)
    # print(f"Lista atualizada: {leituras}\n")

# print(len(leituras))

# for i in range(len(leituras)): 
    # print(leituras[i])

maior = leituras[0] 
menor = leituras[0]
soma = 0

for leitura in leituras: 
    soma = soma + leitura

    if leitura > maior:
        maior = leitura 
    if leitura < menor:
        menor = leitura

print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Soma: {soma}")

