from random import sample

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

ordem = sample([n1, n2, n3, n4], 4)
print('A ordem de apresentação é: ', ordem)