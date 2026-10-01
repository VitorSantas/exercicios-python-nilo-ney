'''Escreva um programa que pergunte o depósito inicial e a taxa
de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros
meses. Escreva o total ganho com juros no período.
'''

deposito_inicial = float(input("Depósito inicial: R$ "))
taxa_juros = float(input("Taxa de juros (% ao mês): "))

saldo = deposito_inicial
mes = 1

print(f"\n{'Mês':>4} {'Saldo':>12} {'Juros do mês':>15}")
print("-" * 35)

while mes <= 24:
    juros_mes = saldo * (taxa_juros / 100)
    saldo = saldo + juros_mes
    
    print(f"{mes:>4} R$ {saldo:>9.2f} R$ {juros_mes:>10.2f}")
    
    mes = mes + 1

total_ganho = saldo - deposito_inicial

print("-" * 35)
print(f"Depósito inicial: R$ {deposito_inicial:.2f}")
print(f"Saldo após 24 meses: R$ {saldo:.2f}")
print(f"Total ganho com juros: R$ {total_ganho:.2f}")


'''
#1° mês redeu R$ 0.01 de R$ 1.0 
#Total de R$ 1.01 

tenho que pegar (total_do_mes do 1° mês = 1.01) * (juros_total = 0.01 = 1% ao mês) = (total_mes)

#2° mês redeu R$ 0.01 de R$ 1.0 
#Total de R$ 1.01 

'''