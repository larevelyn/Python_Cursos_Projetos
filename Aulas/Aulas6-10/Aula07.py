# nome = input('Seu nome: ')
# print('Olá {:20}!'.format(nome)) #:numero(:20) faz o nome aparecer em 20 espaços ou quanto precisar

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
# print('A soma vale {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}\n o produto é {}\n a divisão é {:.3f}'.format(s,m,d), end='>\n') #:.3 significa que aparecerão apenas 3 casas após o ponto(virgula) || end = '' faz que não haja quebra de linha entre esse e o próximo print
print('A divisão inteira é: {}, e potência {}'.format(di, e))