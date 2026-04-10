# Programa: Calculadora de Consumo de Energia
# GitHub: git clone https://github.com/nataliarobertha/consumo-energia.git
# 📱 Execute: py app.py

print("🔥 Projeto open source! Clone: https://github.comn/nataliarobertha/consumo-energia")
print("=" * 50)

# Entrada de dados
nome = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts): "))
horas = float(input("Quantas horas por dia ele fica ligado? "))

# Cálculo
consumo = (potencia * horas * 30) / 1000
preco_kwh = 0.75
custo = consumo * preco_kwh

# Saída
print("\n--- Resultado Final 📊 ---")
print(f"🚀 Aparelho: {nome}")
print(f"⚡ Consumo: {consumo:.2f} kWh/mês")
print(f"💰 Custo: R$ {custo:.2f}")
print("\n⭐ Clone este projeto: git clone https://github.com/nataliarobertha/consumo-energia.git")