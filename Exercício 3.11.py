'''Faça um programa que solicite o preço de uma mercadoria e o
percentual de desconto. Exiba o valor do desconto e o preço a pagar.'''

dinheiro = float(input('Qual o preço dessa fruta? '))
porcentngem = float(input("Você tem quanto porcento de desconto? "))

valor_do_desconto = (dinheiro * porcentngem / 100)
valor_para_pagar = dinheiro - valor_do_desconto

print(f"VocÊ tem um desconto de R$ {valor_do_desconto:.2f}. Agora você vai pagar só R$ {valor_para_pagar:.2}")
