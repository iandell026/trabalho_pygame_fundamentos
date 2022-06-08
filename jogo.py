import pygame
import time
import random


pygame.init()


######## Variáveis Globais ########
tela_largura = 800
tela_altura = 600
gameDisplay = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Mario 12")
icone = pygame.image.load("assets/marioicon.jpg")
pygame.display.set_icon(icone)
# explosao_sound = pygame.mixer.Sound("assets/perdeu.wav")




clock = pygame.time.Clock()
# RGB
black = (0, 0, 0)
white = (255, 255, 255)
mario = pygame.image.load("assets/mario.png")
mario_largura = 100
mario_altura = 120

doce = pygame.image.load("assets/doce.png")
doce_largura = 120
doce_altura = 108

algodao = pygame.image.load("assets/pirulito.png")
algodao_largura = 140
algodao_altura = 128

fundo = pygame.image.load("assets/fundo.png")

######## Funções Globais ########


def mostrarIron(x, y):
    gameDisplay.blit(mario, (x, y))


def mostraDoce(x, y):
    gameDisplay.blit(doce, (x, y))

def mostraAlgodao(x, y):
    gameDisplay.blit(algodao, (x, y))



def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (tela_largura/2, tela_altura/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def dead():
    # pygame.mixer.music.stop()
    # pygame.mixer.Sound.play(explosao_sound)
    message_display("Você Perdeu")


def escrePlacar(contador):
    font = pygame.font.SysFont(None, 22)
    text = font.render("Desvios: "+str(contador), True, white)
    gameDisplay.blit(text, (10, 30))

# Looping do Jogo


def game_loop():
    # pygame.mixer.music.load("assets/musica.mp3")
    # pygame.mixer.music.play(-1)

    iron_posicaoX = 350
    iron_posicaoY = 450
    movimentoX = 0
    doce_speed = 5
    doce_posicaoX = random.randrange(0, tela_largura)
    doce_posicaoY = -108
    algodao_speed = 3
    algodao_posicaoX = random.randrange(0, tela_largura)
    algodao_posicaoY = -128
    
    
    desvios = 0

    while True:
        # inicio - Interação do usuário
        # event.get do pygame, devolve uma lista de eventos da janela
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                # fecha tudo!
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    movimentoX = 0
        iron_posicaoX = iron_posicaoX + movimentoX
        # fim - Interação do usuário

        # Alterando a cor de fundo da tela
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))

        mostrarIron(iron_posicaoX, iron_posicaoY)

        mostraDoce(doce_posicaoX, doce_posicaoY)
        doce_posicaoY = doce_posicaoY + doce_speed

        mostraAlgodao(algodao_posicaoX, algodao_posicaoY)
        algodao_posicaoY = algodao_posicaoY + algodao_speed

        if doce_posicaoY > tela_altura:
            doce_posicaoY = 0 - doce_altura
            doce_speed += 1
            doce_posicaoX = random.randrange(0, tela_largura)
            desvios = desvios + 1

        if algodao_posicaoY > tela_altura:
            algodao_posicaoY = 0 - algodao_altura
            algodao_speed += 1
            algodao_posicaoX = random.randrange(0, tela_largura)
            desvios = desvios + 1

        escrePlacar(desvios)

        if iron_posicaoX > tela_largura - mario_largura:
            iron_posicaoX = tela_largura - mario_largura
        elif iron_posicaoX < 0:
            iron_posicaoX = 0


        if iron_posicaoY+140 < doce_posicaoY + doce_altura:
            if iron_posicaoX < doce_posicaoX and iron_posicaoX + mario_largura > doce_posicaoX or doce_posicaoX+doce_largura > iron_posicaoX and doce_posicaoX + doce_largura < iron_posicaoX + mario_largura:
                dead()

        if iron_posicaoY+140 < algodao_posicaoY + algodao_altura:
            if iron_posicaoX < algodao_posicaoX and iron_posicaoX + mario_largura > algodao_posicaoX or algodao_posicaoX+algodao_largura > iron_posicaoX and algodao_posicaoX + algodao_largura < iron_posicaoX + mario_largura:
                dead()
        pygame.display.update()
        clock.tick(60)


game_loop()
