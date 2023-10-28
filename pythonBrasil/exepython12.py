'''Tendo como dado de entrada a altura de uma pessoa, costrua um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
(72.7*altura)-58'''
a=float(input('Digite sua altura: '))
peso=(72.7*a)-58
print('O peso ideal para a altura de {}cm é de {:.2f}kgs.'.format(a,peso))