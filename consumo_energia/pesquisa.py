# contador
excelente = 0
ruim = 0

print("--- Empresa de marketing TudoWeb, atividade - Pesquisa---")


for i in range(1, 13):
    print(f"\nEntrevistado nº {i}")
    
    # Pesquisa
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("O que achou do atendimento?")
    print("1: EXCELENTE | 2: BOM | 3: RUIM")
    opiniao = int(input("Sua resposta: "))

    
    if opiniao == 1:
        excelente = excelente + 1
    elif opiniao == 3:
        ruim = ruim + 1
    

# resultado
print("\n" + "="*30)
print("📊 RESULTADO FINAL DA PESQUISA")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
print("="*30)