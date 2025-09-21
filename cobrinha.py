import pygame
import random

# Inicializar o Pygame
pygame.init()

# Dimensões da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cobrinha 🐍")

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
    msg = fonte.render(texto, True, cor)
    tela.blit(msg, [x, y])

def jogo():
    fim_de_jogo = False
    game_over = False
    x = largura // 2
    y = altura // 2
    x_mudanca = 0
    y_mudanca = 0

    corpo_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco

    while not fim_de_jogo:
        while game_over:
            tela.fill(preto)
            mensagem("Fim de Jogo! Pressione C para jogar novamente ou Q para sair", vermelho, largura / 6, altura / 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        fim_de_jogo = True
                        game_over = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_mudanca == 0:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif event.key == pygame.K_RIGHT and x_mudanca == 0:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif event.key == pygame.K_UP and y_mudanca == 0:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif event.key == pygame.K_DOWN and y_mudanca == 0:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        x += x_mudanca
        y += y_mudanca

        if x < 0 or x >= largura or y < 0 or y >= altura:
            game_over = True

        tela.fill(preto)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cobra_cabeca = []
        cobra_cabeca.append(x)
        cobra_cabeca.append(y)
        corpo_cobra.append(cobra_cabeca)
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        if cobra_cabeca in corpo_cobra[:-1]:
            game_over = True

        for bloco in corpo_cobra:
            pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])
        
        #Mostra Pontuação
        mensagem(f"Pontos: {comprimento_cobra - 1}", branco, 10, 10)
        pygame.display.update()
        clock.tick(velocidade)
        
        #Atualiza comida quando a cobra comer
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
            comprimento_cobra += 1


jogo()