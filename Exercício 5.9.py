'''
Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. 
Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da 
divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 / 4 = 5, uma vez que 
podemos subtrair 4 cinco vezes de 20.
'''

dividendo = float(input("Digite um número: "))
divisor = float(input("Digite um número: "))

if dividendo == 0:
    print(f"Não tem como divide 0 por {divisor}")

else:
    quociente = 0
    resto = dividendo

while resto >= divisor:
    resto = resto -divisor
    quociente = quociente + 1 

# Exibindo os resultados solicitados
print(f"Divisão inteira (quociente): {quociente}")
print(f"Resto da divisão: {resto}")
''''
while contato >= 0: # vou repeti o numero 1 o até chegar em 4, o 4 não é = 20, então vou tentar 2...
    
    contato  = contato - n2
    resposta = resposta + 1
    

print(resposta)
print(resto)'''