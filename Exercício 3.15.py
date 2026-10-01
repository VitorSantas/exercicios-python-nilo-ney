'''Escreva um programa para calcular a redução do tempo de vida
de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante 
perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
'''

cigarros_fumados_por_dia = int(input("Quantos cigarros você cigarros por dia? "))
anos_fumando = int(input("Quantos que você fumar? "))

dias_fumando = anos_fumando * 365
horas_fumando = dias_fumando * 24
minutos_fumando = horas_fumando * 60

cigarros_fumando_por_ano = cigarros_fumados_por_dia * dias_fumando
minutos_de_vida_perdidos = cigarros_fumando_por_ano * 10
horas_de_vida_perdidos = minutos_de_vida_perdidos / 60
dias_de_vida_perdidos = horas_de_vida_perdidos / 24

#print(f"{dias_fumando:.2f}")
#print(f"{horas_fumando:.2f}")
#print(f"{minutos_fumando:.2f}")
print(f"Você perdeu {dias_de_vida_perdidos:.2f} dias de vida")
