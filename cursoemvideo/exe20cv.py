# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1=(input('Digite o nome do primeiro aluno: '))
n2=(input('Digite o nome do segundo aluno: '))
n3=(input('Digite o nome do terceiro aluno: '))
n4=(input('Digite o nome do quarto aluno: '))
alunos=[n1,n2,n3,n4]
#n~so consigo definir uma variavel com a função shuffle, apenas aplicar a funçaõ em si
#e printar na tela a lista já randomizada
random.shuffle(alunos)
print(alunos)