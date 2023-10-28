'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que que calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h)-58
b. para mulheres: (62.1*h) - 44.7'''
h= float(input('Digite a sua altura: '))
a= (72.7*h)-58
b= (62.1*h) - 44.7
print('De acordo com a altura, o peso ideal para homens de {}cm é de {:.2f}kgs.\nE para mulheres dessa mesma altura, o peso ideal é de {:.2f}kgs.'.format(h,a,b))