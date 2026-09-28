print("=== DESCONTO PROGRESSIVO ===")

valor = float(input("Digite o valor total da compra: R$ "))

# Verifica qual desconto deve ser aplicado

# Se a compra for menor que R$ 200 → 5%
# Senão, se for menor que R$ 300 → 10%
# Senão → 15%

if valor < 200:
    desconto = 0.05
elif valor < 300:
    desconto = 0.10
else:
    desconto = 0.15

# Calcula o desconto e o valor final
valor_desconto = valor * desconto
valor_final = valor - valor_desconto

# Exibe os resultados
print("\n=== RESULTADO DA COMPRA ===")
print(f"Valor da compra: R$ {valor:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")