consumo = float(input("Consumo em KwH: "))

custo_base = consumo * 0.60

resposta_verao = input("Estamos no período de verão? (sim/nao): ").strip().lower()

# A função strip() remove espaços em branco e a função lower() coloca tudo em minúsculo.

verao = not (resposta_verao == "nao")

if consumo > 300 and verao:
    taxa_bandeira = 15.00
    print("Bandeira: Vermelha (Consumo crítico no verão)")
elif consumo > 200 or (consumo > 150 and verao): 
    taxa_bandeira = 7.50
    print("Bnadeira: Amarela (Consumo elevado)")
else: 
    taxa_bandeira = 0.00
    print("Bandeira: Verde (Consumo sob controle)")

valor_total = custo_base + taxa_bandeira

print(f"Custo base do consumo: R$ {custo_base:.2f}")
print(f"Taxa de bandeira: R$ {taxa_bandeira:.2f}")
print(f"Valor total da conta: R$ {valor_total:.2f}")                    