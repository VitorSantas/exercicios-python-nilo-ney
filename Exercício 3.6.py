''' Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, 
todas as médias do aluno devem sermaiores ou iguais a 7. Considere que o aluno cursa apenas três matérias, e que
a nota de cada uma está armazenada nas seguintes variáveis: matéria l, matéria 2 e matéria 3. '''

materia1 = 7
materia2 = 7
materia3 = 7

media = materia1 >= 7 and materia2 >= 7 and  materia3 >= 7


#print(media)
a = "Vitor"
print(a[0])
print(f'Meu nomo é {a}')
print("R$ %.2f" % 7)
print('')

ano = int(input("Quantos anos de trabalho? "))
print(f"{ano} ano de trabalho")

print("")

valor_do_trabalho = float(input("Preço do serviço?"))
print(f"Preço do serviço {valor_do_trabalho}")

bonus = ano * valor_do_trabalho
print("")
print(f'O seu bonus é de R$ {bonus}')

