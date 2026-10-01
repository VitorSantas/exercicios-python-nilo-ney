'''
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a RS 1.250, 
calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
'''

salario = float(input("Qual é o seu salário? "))

if salario > 1250:
    salario_aumento10 = salario * 1.1
    print(f"Seu salário de R$ {salario:.2f} agora é R$ {salario_aumento10}")

else:
    salario_aumento15 = salario * 1.15
    print(f"eu salário de R$ {salario:.2f} agora é R$ {salario_aumento15}")