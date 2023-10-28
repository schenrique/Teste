#escreva um programa que converta uma temperatura digitando em graus celsius e converta para graus fahrenheit
grausc = float(input('Digite a temperatura em graus celsius: '))
grausf = (grausc*9/5)+32
print('{}°C é igual a {}°F.'.format(grausc,grausf))