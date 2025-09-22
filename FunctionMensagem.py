def mensagem(texto, cor, x, y, tela, fonte):
    msg = fonte.render(texto, True, cor)
    tela.blit(msg, [x, y])
