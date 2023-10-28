#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num=float(input("Digite um número: "))
math.floor(num)
print('O número {} tem a parte inteira'.format(num),math.floor(num))
