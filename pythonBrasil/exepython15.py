'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:'''
valorhora=float(input('Digite o valor da hora trabalhada: '))
horatrab=float(input('Digite as horas trabalhadas neste mês: '))
salario= horatrab*valorhora
ir= (salario/100)*11
inss= (salario/100)*8
sind=(salario/100)*5
salarioliq= salario-ir-inss-sind
print('+ Salário Bruto : R${:.2f}\n- IR (11%) : R${:.2f}\n- INSS (8%) : R${:.2f}\n- Sindicato (5%) : R${:.2f}\n= Salário Liquido : R${:.2f}'.format(salario,ir,inss,sind,salarioliq))