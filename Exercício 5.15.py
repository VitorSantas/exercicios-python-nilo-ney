'''Escreva um programa para controlar uma pequena máquina
registradora. Você deve solicitar ao usuário que digite o código do produto e a
quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço
de cada produto:

Código Preço
1      0,50
2      1,00
3      4,00
5      7,00
9      8,00

Seu programa deve exibir o total das compras depois que o usuário digitar
0. Qualquer outro código deve gerar a mensagem de erro “Código inválido”.'''

total_de_produto = 0
total_de_preco = 0

while True:
    
    produto = int(input("Qual o código do produto? "))
    if produto == 0:
        break

    quantidade = int(input("Quantos produtos? "))

    if produto == 1:
        preco_unitario = 0.50

    elif produto == 2:
        preco_unitario = 1

    elif produto == 3:
        preco_unitario = 4

    elif produto == 5:
        preco_unitario = 7

    elif produto == 9:
        preco_unitario = 8

    else:
        print("Código inválido")
        continue


    total_de_preco += preco_unitario * quantidade
    total_de_produto += quantidade

print(f"Sua compra ficou no total de R$ {total_de_preco} \nVocê comprou o total de {total_de_produto} produtos")
