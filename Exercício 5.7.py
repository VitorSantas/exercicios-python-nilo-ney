'''Modifique o programa anterior de forma que o usuário também
digite o início e o fim da tabuada, em vez de começar com 1 e 10'''

tabuada = float(input("Tabuada do: "))
n1 = float(input("Quer começar a tabuada a partir de qual número? "))
n2 = float(input("Quer terminar a tabuada a partir de qual número? ")) 

x = n1

while x <= n2:
    print(f"{tabuada} * {x} = {tabuada*x:.2f}")
    x = x + 1