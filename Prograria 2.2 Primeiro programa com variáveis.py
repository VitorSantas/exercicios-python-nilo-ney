import random

pontos = 0
repeticao = 10

tabuada = int(input("Qual número da tabuada você quer praticar? "))
operador = str(input("Qual operador da tabuada você quer praticar (+, -, *, /)? "))

contato = 0

while contato < repeticao:
    contato = contato + 1
    numero_random = random.randint(1, 999)
    
    # 1. Lê a resposta aceitando vírgula em todos os operadores
    resposta_str = input(f"{contato}ª pergunta: {tabuada} {operador} {numero_random} = ")
    resposta = float(resposta_str.replace(",", "."))
    
    # 2. Calcula a resposta certa dinamicamente baseada no operador escolhido
    if operador == "+":
        resposta_certa = tabuada + numero_random
    elif operador == "-":
        resposta_certa = tabuada - numero_random
    elif operador == "*":
        resposta_certa = tabuada * numero_random
    elif operador == "/":
        resposta_certa = tabuada / numero_random
    else:
        print("Operador inválido!")
        break

    # 3. Valida se o usuário acertou
    # Usamos 'round' ou margem de erro pequena para divisão com decimais
    if round(resposta, 2) == round(resposta_certa, 2):
        print("Você acertou! 🎉\n")
        pontos = pontos + 1
    else:
        print(f"Você errou. A resposta certa era: {resposta_certa:.2f}\n")
        pontos = pontos - 1

print(f"Fim de jogo! Você fez um total de {pontos} ponto(s).")