'''Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar,
o salário e a quantidade de anos a pagar. O valor da prestação mensal não
pode ser superior a 30% do salário. Calcule o valor da prestação como sendo
o valor da casa a comprar dividido pelo número de meses a pagar.'''

preco_da_casa = float(input("Qual o preço da casa que você quer? R$ "))
salario = float(input("Qual é o seu salário? R$"))
anos = int(input("Vai pagar por quantos anos? "))

meses = anos * 12
limite = salario * 0.3
prestacao_mensal = preco_da_casa / meses


if prestacao_mensal <= limite:
    print(f"Seu crédito foi aprovado, vão ser {meses} meses com prestações de R$ {prestacao_mensal:.2f} vez por mês")

else:
    print(f"Seu credito não foi aprovado, vão ser R$ {prestacao_mensal:.2f} por mês e R$ {limite:.2f} é 30% do seu salário")