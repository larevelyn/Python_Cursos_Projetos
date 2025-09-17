from statistics import median

n1 = int(input('Digite a nota do 1º Semestre: '))
n2 = int(input('Digite a nota do 2º Semestre: '))

# print('A média final é: {}'.format(median([n1, n2, 2]))) #Forma elaborada, que mostra o valor arredondado para baixo
print('A média final é: {:.1f}'.format(((n1 + n2)/2)))