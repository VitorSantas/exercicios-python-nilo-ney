'''Escreva um programa que pergunte o depósito inicial e a taxa
de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros
meses. Escreva o total ganho com juros no período.
'''

contato = 1


deposito = float(input("Qual o valo do seu depósito? R$ ").replace(",","."))
juros = float(input("Quando de juros por mês? ").replace(",","."))
juros = juros / 100
juros_total = deposito * juros
total_mes = deposito + juros_total

while contato <= 24:
    
    print(f"{contato}° mês redeu R$ {juros_total:.2f}\nDo valor em conta de R$ {deposito}\nNo total ficou R$ {total_mes:.2f} ")
    print("")

    juros_total = juros_total * total_mes
    total_mes = total_mes + juros_total
    contato = contato + 1


'''
#1° mês redeu R$ 0.01 de R$ 1.0 
#Total de R$ 1.01 

tenho que pegar (total_do_mes do 1° mês = 1.01) * (juros_total = 0.01 = 1% ao mês) = (total_mes)

#2° mês redeu R$ 0.01 de R$ 1.0 
#Total de R$ 1.01 

'''