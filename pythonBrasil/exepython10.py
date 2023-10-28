'''Faça um programa que peça a temperatura em graus e Celsius, transforme e mostre a temperatura em graus Fahrenheit.'''
grausc = float(input('Digite a temperatura em graus celsius: '))
grausf = (grausc*9/5)+32
print('{}°C é igual a {}°F.'.format(grausc,grausf))