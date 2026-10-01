'''Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, 
cobrando R$ 0,50 por km para viagens de até de 200 km, e RS 0,45 para viagens mais longas.
'''

distancia = float(input("Qual a distância da sua viagem? "))

if distancia <= 200:
    preco = distancia * 0.5
    print(f"Você vai pagar R$ {preco:.2f}")

else:
    preco = distancia * 0.45
    print(f"Você vai pagar R$ {preco:.2f}")


