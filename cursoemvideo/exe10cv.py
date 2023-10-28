#crie um progarama que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = R$3,27
r = float(input('Digite o valor em real:'))
d = float(3.27)
conv = r / d
print('O valor em dólar disponível para compra é de {}'.format(conv))