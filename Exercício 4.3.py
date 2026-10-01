'''Escreva um programa que leia três números e que imprima o maior e o menor.'''

primeiro_numero = float(input("Digite um número: "))
segundo_numero = float(input("Digite um número: "))
terceiro_numero = float(input("Digite um número: "))

maior = max(primeiro_numero, segundo_numero, terceiro_numero)
menor = min(primeiro_numero, segundo_numero, terceiro_numero)

print(f"Esse é o meno {menor}")
print(f"Esse é o maior {maior}")