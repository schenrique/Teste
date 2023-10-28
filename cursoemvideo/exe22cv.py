''''Crie um programa que leia o nome completo de uma pessoa e mostre
o nome com todas as letras maiúsculas
o nome com todas as letras minúsculas
quantas letras ao todo(sem considerar espaços)
quantas letras tem o primeiro nome
'''
nome = input('Digite seu nome completo: ')
sespaco=nome.replace(' ','')
print(len(sespaco))
print(nome.upper())
print(nome.lower())
divido=nome.split()
print(len(divido[0]))