#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a
# quantidade de de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m2
a = float(input('digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
area = a * l
tn = area / 2
print('a quantidade de tinta necessária é de {} litros'.format(tn))