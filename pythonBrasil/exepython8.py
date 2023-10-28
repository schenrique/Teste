#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora = input('Qual é o valor que você recebe por hora? ')
horatrab=input('Quantas horas você trabalhou este mês? ')
salario = int(horatrab)*int(valor_hora)
print('Esse é o seu salário esse mês',salario)