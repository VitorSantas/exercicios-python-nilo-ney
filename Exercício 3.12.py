'''Escreva um programa que calcule o tempo de uma viagem de
carro. Pergunte a distância a percorrer e a velocidade média esperada para a
viagem.'''

km = float(input("Quantos km? "))
velocidade_media = float(input("Qual a velocidade média? "))

tempo_de_viagem = km / velocidade_media
print(f"Essa viagem vai ter {tempo_de_viagem:.2f}h de viagem")