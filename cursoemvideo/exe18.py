#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang=float(input('Digite um angulo: '))
tan=math.tan(ang)
sen=math.sin(ang)
cos=math.cos(ang)
print('A tangente de {} é de: {:.2f}\nO seno: {:.2f}\nE o coseno: {:.2f}'.format(ang,tan,sen,cos))