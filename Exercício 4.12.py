'''Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o 
tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

  Preço por tipo e faixa de consumo

Tipo           Faixa (kWh)     Preço

Residencial    Até 500         R$ 0,40
               Acima de 500    R$ 0,65

Comercial      Até 1000        R$ 0,55
               Acima de 1000   R$ 0,60

Industrial     Até 5000        R$ 0,55
               Acima de 5000   RS 0,60

'''

KWH_consumindo = float(input("KWH consumindo por você: "))
tipo = int(input("Qual o seu tipo de conta? \n1 - Residencial \n2 - Conmercial \n3 - Industrial \nQual a sua opção? "))

if tipo == 1:
    if KWH_consumindo <= 500:
        valor_para_pagar = KWH_consumindo * 0.4
        print(f"Vocâ vai pagar R$ {valor_para_pagar:.2f}")
    else:
        valor_para_pagar = KWH_consumindo * 0.65
        print(f"você vai pagar R$ {valor_para_pagar:.2f}")

elif tipo == 2:
    if KWH_consumindo <= 1000:
        valor_para_pagar = KWH_consumindo * 0.55
        print(f"Vocâ vai pagar R$ {valor_para_pagar:.2f}")
    else:
        valor_para_pagar = KWH_consumindo * 0.60
        print(f"você vai pagar R$ {valor_para_pagar:.2f}")

elif tipo == 3:
    if KWH_consumindo <= 5000:
        valor_para_pagar = KWH_consumindo * 0.55
        print(f"Vocâ vai pagar R$ {valor_para_pagar:.2f}")
    else:
        valor_para_pagar = KWH_consumindo * 0.60
        print(f"você vai pagar R$ {valor_para_pagar:.2f}")

else: 
    print("Opção inválida!")