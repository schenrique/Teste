#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
'''''
import pygame
pygame.init()
pygame.mixer.music.load('realiti.mp3') #aqui o modulos implesmente não fuc 
pygame.mixer.music.play()
pygame.event.wait()
'''
#nesse eu tive bastante dificuldade com o modulo, até que encontrei um que funcionasse
import playsound
playsound.playsound('realiti.mp3')
playsound.PlaysoundException