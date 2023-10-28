'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus digitos separados
ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''
num=input('Digite um número: ')
c=[0,0,0,0]
sep=list(num)
ok=c+sep
tam=len(ok)
uni=ok[tam-1]
dez=ok[tam-2]
cen=ok[tam-3]
mil=ok[tam-4]
print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(uni,dez,cen,mil))
