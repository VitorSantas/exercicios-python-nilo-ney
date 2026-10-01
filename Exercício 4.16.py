'''
Corrija o programa a seguir:

media = input("Digite sua media:")

if media < 4:
    print("Infelizmente você reprovou")

if media < 7:
    print("Você ficou de recuperação")

if media > 7:
    print("Você passou de ano")'''

#------------------------------------------------------

media = float(input("Digite sua media: "))

if media < 0 or media > 10:
    print(f"{media:.2f} é um valor invalido: ")

elif media < 4:
    print("Infelizmente você reprovou")

elif media < 7:
    print("Você ficou de recuperação")

else:
    print("Você passou de ano")