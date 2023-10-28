#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
aluno1=input('Digite o nome do aluno: ')
aluno2=input('Digite o nome do aluno: ')
aluno3=input('Digite o nome do aluno: ')
aluno4=input('Digite o nome do aluno: ')
alunos=[aluno1,aluno2,aluno3,aluno4]
sorteado=random.choice(alunos)
print('O aluno sorteado: {}'.format(sorteado))