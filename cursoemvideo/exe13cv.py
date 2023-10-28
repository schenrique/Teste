#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
sal = float(input('Digite o seu salário atual: '))
aumsal = (sal / 100)* 15
novosal = sal + aumsal
print('Este é o seu novo salário: {}'.format(novosal))
