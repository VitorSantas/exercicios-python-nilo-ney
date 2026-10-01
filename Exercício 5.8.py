'''Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os 
operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como
somas sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

resposta = 0
contato = 0

while contato < n1:
    resposta = resposta + n2
    contato = contato + 1

print(f"{resposta}")