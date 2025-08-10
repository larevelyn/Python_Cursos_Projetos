vl = float(input('Digite o preço atual do produto: '))

# print('O preço atual do produto é {}, mas com desconto fica {:.2f}'.format(vl,(vl/1.05)))
# Correção
print('O preço atual do produto é {}, mas com desconto fica {:.2f}'.format(vl,(vl - (vl * 5 / 100))))