# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
m = int(input('Escreva a medida em metros: '))
c = m * 100
mili = c * 100
print('O valor de {} metros em centímetros é {} e em milímetros é {}'.format(m,c,mili))