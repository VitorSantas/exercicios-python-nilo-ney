contato = 0
soma = 0
while True:
    
    v = int(input("Digite um número ou 0 para sair: "))
    
    
    
    if v == 0:
        break
    
    soma += v
    contato += 1

media = soma/contato 

print("Você saiu do chat :(")
print(f"soma {soma}")
print(f"Vc digitou {contato} vezes")
print(f"A média  {media:.2f}")

