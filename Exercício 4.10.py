'''
Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.'''
print()
primeiro_numero = float(input("Digite um número: "))
segundo_numero = float(input("Digite um número: "))

print("\nVocê quer fazer qual? \n 1 - Soma (+) \n 2 - Subtração (-) \n 3 - Multiplicação (*) \n 4 - Divisão (/) \n")

operacao = int(input("\nDigite o número da opção que você quer: "))

if operacao == 1:
    resposta_soma = primeiro_numero + segundo_numero
    print(f"{primeiro_numero} + {segundo_numero} = {resposta_soma}")

elif operacao == 2:
    resposta_subtracao = primeiro_numero - segundo_numero
    print(f"{primeiro_numero} - {segundo_numero} = {resposta_subtracao}")

elif operacao == 3:
    resposta_multiplicacao = primeiro_numero * segundo_numero
    print(f"{primeiro_numero} * {segundo_numero} = {resposta_multiplicacao}")

elif operacao == 4:
    resposta_divisao = primeiro_numero / segundo_numero
    print(f"{primeiro_numero} / {segundo_numero} = {resposta_divisao}")

else:
    print("Não tem esse opção")