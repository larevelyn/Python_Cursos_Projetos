from math import hypot
ctop = float(input('Digite o cateto oposto: '))
ctadj = float(input('Digite o cateto adjacente: '))

print('A hipotenusa é: {:.2f}'.format(hypot(ctop, ctadj)))
