#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dia = int(input("A quantos dias eu estou aqui? "))
hora = int(input("A quantas horas eu estou aqui? "))
minuto = int(input("A quantos minutos eu estou aqui? "))
segundo = int(input("A quantos segundos eu estou aqui? "))

print(f"Eu estou aqui a {(dia*86400) + (hora*60*60) + (minuto*60) + segundo}s")
