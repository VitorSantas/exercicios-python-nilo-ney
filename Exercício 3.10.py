'''Faça um programa que calcule o aumento de um salário. Ele
deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor
do aumento e do novo salário.'''

salario = float(input("Qual o valor do salário? "))
porcentagem = float(input("Qual a porcentagem que vc quer dar nesse salário? "))

aumento = salario * (porcentagem / 100)
print(f"O seu salário de R$ {salario} teve um aumento de {porcentagem} porcento que te deu mais R${aumento} de aumento no tatal vc tem um salário de R${salario+aumento} ")