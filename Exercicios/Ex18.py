import math

ang = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print(' O SENO é: {:.2f} \n O COSSENO é {:.2f} \n A TANGENTE é: {:.2f}'.format(seno, cos,tang))
#correção: Tem que converter para radianos