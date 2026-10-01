'''Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias
pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''

km_rodados = float(input("Quantos km você rodou com esse carro? "))
dias_alugados = int(input("Você ficou por quantos dias com esse caro alugado? "))

preco_dos_dias = dias_alugados * 60

preco_dos_km_rodaods = km_rodados * 0.15

resposta = preco_dos_dias + preco_dos_km_rodaods

print(f"Você tem que pagar R$ {resposta:.2f}")