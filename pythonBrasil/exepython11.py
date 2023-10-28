'''Faça um programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    a. O produto do dobro do primeiro com a metade do segundo.
    b. A soma do triplo do primeiro com o terceiro.
    c. O terceiro elevado ao cubo'''
n = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um nùmero real: '))
a = (n*2)%(n2/2)
b = (n*3)+n3
c = n3**3
print('O produto do dobro do primeiro com a metade do segundo: {}'.format(a))
print('A soma do triplo do primeiro com o terceiro: {}'.format(b))
print('O terceiro elevado ao cubo: {}'.format(c))