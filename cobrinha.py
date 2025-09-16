import pygame
import random

# Inicializar o Pygame
pygame.init()

# Dimensões da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game 🐍")

# Cores
preto = (0, 0, 0)
verde = (0, 255 , 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

# Clock
clock = pygame.time.Clock()

# Configurações da cobra
tamanho_bloco = 20
velocidade = 10

# Fonte
fonte = pygame.font.SysFont("Arial", 25)

# Funções
def mensagem(texto, cor, x, y):

def jogo():