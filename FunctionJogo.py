import pygame
import random

def jogo(tela, fonte, largura, altura, preto, verde, vermelho, branco, clock, tamanho_bloco, velocidade, mensagem):
    jogando = True
    while jogando:
        fim_de_jogo = False
        game_over = False
        x = largura // 2
        y = altura // 2
        x_mudanca = 0
        y_mudanca = 0
        corpo_cobra = []
        comprimento_cobra = 1

        # Sorteia a posição da fruta sem sobrepor o corpo da cobra
        def nova_fruta():
            while True:
                fruta_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
                fruta_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
                if [fruta_x, fruta_y] not in corpo_cobra:
                    return fruta_x, fruta_y

        comida_x, comida_y = nova_fruta()

        while not fim_de_jogo:
            while game_over:
                tela.fill(preto)
                texto1 = "Fim de Jogo!"
                texto2 = "Pressione C para jogar novamente ou Q para sair"
                msg1 = fonte.render(texto1, True, vermelho)
                msg2 = fonte.render(texto2, True, vermelho)
                rect1 = msg1.get_rect(center=(largura // 2, altura // 2 - 20))
                rect2 = msg2.get_rect(center=(largura // 2, altura // 2 + 20))
                tela.blit(msg1, rect1)
                tela.blit(msg2, rect2)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        jogando = False
                        fim_de_jogo = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            jogando = False
                            fim_de_jogo = True
                            game_over = False
                        if event.key == pygame.K_c:
                            fim_de_jogo = True
                            game_over = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogando = False
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
            cobra_cabeca = [x, y]
            corpo_cobra.append(cobra_cabeca)
            if len(corpo_cobra) > comprimento_cobra:
                del corpo_cobra[0]

            if cobra_cabeca in corpo_cobra[:-1]:
                game_over = True

            for bloco in corpo_cobra:
                pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

            mensagem(f"Pontos: {comprimento_cobra - 1}", branco, 10, 10, tela, fonte)
            pygame.display.update()
            clock.tick(velocidade)

            if x == comida_x and y == comida_y:
                comida_x, comida_y = nova_fruta()
                comprimento_cobra += 1