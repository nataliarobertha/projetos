#colocar cor
from colorama import Fore, Style, init
import time

# Inicializa
init(autoreset=True)

# Define cor e mensagem
def verificar_nivel(percentual):
    if percentual <= 20:
        return Fore.RED, "🚨 CRÍTICO - Muito baixo"
    elif percentual <= 40:
        return Fore.YELLOW, "⚠️ Baixo"
    elif percentual <= 70:
        return Fore.GREEN, "✅ Médio"
    elif percentual <= 90:
        return Fore.CYAN, "💧 Alto"
    else:
        return Fore.BLUE, "🔵 ALERTA - Muito alto"

# Barra com gotas
def barra_gotas(percentual):
    total = 10  # quantidade de "gotas"
    preenchido = int((percentual / 100) * total)
    
    return "💧" * preenchido + "▫️" * (total - preenchido)

# Simulação de leituras
leituras = [15, 25, 38, 55, 72, 88, 95, 60, 35, 10]

print("\n=== 💧 MONITORAMENTO DO RESERVATÓRIO ===\n")

for nivel in leituras:
    cor, mensagem = verificar_nivel(nivel)
    barra = barra_gotas(nivel)

    print(cor + f"Nível: {nivel}% | {barra} | {mensagem}")
    time.sleep(1)

print("\nSistema encerrado.\n")