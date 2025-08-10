# Não consegui fazer
import pygame
pygame.init()
pygame.mixer.load('ex21.mp3')#chama a musica
pygame.mixer.music.play() #reproduz a musica
pygame.event.wait()#espera a musica tocar até o fim
