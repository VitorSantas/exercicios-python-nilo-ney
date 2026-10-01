'''Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, 
exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km
acima de 80 km/h.'''

velocidade = float(input("Qual a velocidade do carro em km/h? "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"{velocidade:.1f} km/h é maior que 80 km/h.")
    print(f"Você foi multado! Sua multa é de R$ {multa:.2f}")
elif velocidade < 80:
    print(f"{velocidade:.1f} km/h é menor que 80 km/h. Dirija com segurança!")
else:
    print(f"{velocidade:.1f} km/h — está no limite. Mais um pouco e você seria multado!")