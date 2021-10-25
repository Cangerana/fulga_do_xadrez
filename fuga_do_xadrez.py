# https://github.com/sourabhv/FlapPyBird/blob/master/flappy.py
from models.interface import get_action
from utils.colision import is_coliding
import pygame
from random import randint
from pygame.locals import *

from time import sleep
import sys

SCREENWIDTH = 1280
SCREENHEIGHT = 720
SCORE = 0
TABY = 0
FPS = 30
ACTIONS = []
PLAYER = [644, 655]

IMAGES, SOUNDS, HITMASKS = {}, {}, {}

BACKGROUNDS_LIST = (
    'assets/sprites/cenario 1.jpg',
    'assets/sprites/cenario 2.jpg',
    'assets/sprites/cenario 3.jpg',
)


def main():
    global SCREEN, FPSCLOCK
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    pygame.display.set_caption('Fuga do Xadrez')

    IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[0]).convert()

    IMAGES['tabuleiro'] = pygame.image.load(
        'assets/sprites/tabuleiro.png').convert_alpha()

    IMAGES['rei'] = pygame.image.load(
        'assets/sprites/pieces/rei.png').convert_alpha()
    IMAGES['peao'] = pygame.image.load(
        'assets/sprites/pieces/peao.png').convert_alpha()
    IMAGES['cavalo'] = pygame.image.load(
        'assets/sprites/pieces/cavalo.png').convert_alpha()
    IMAGES['bispo'] = pygame.image.load(
        'assets/sprites/pieces/bispo.png').convert_alpha()
    IMAGES['torre'] = pygame.image.load(
        'assets/sprites/pieces/torre.png').convert_alpha()

    IMAGES['main'] = pygame.image.load('assets/sprites/menu.jpg').convert()

    IMAGES['coluna'] = pygame.image.load(
        'assets/sprites/bordas de coluna.png').convert_alpha()

    fase1()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # SCREEN.blit(IMAGES['main'], (0,0))
        # main
        run()  # game
        # end game

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def reset_background():
    SCREEN.blit(IMAGES['background'], (0, 0))
    SCREEN.blit(IMAGES['tabuleiro'], (0, TABY))
    SCREEN.blit(IMAGES['coluna'], (0, 0))

    SCREEN.blit(IMAGES['rei'], PLAYER)

    for i in range(len(torres)):
        SCREEN.blit(IMAGES['torre'], torres[i])

    for i in range(len(peoes)):
        SCREEN.blit(IMAGES['peao'], peoes[i])

    for i in range(len(bispos)):
        SCREEN.blit(IMAGES['bispo'], bispos[i])

    for i in range(len(cavalos)):
        SCREEN.blit(IMAGES['cavalo'], cavalos[i])


def run():
    global TABY
    global SCORE
    global ACTIONS

    flag = True
    base_time = pygame.time.get_ticks()

    while True:
        if is_coliding(PLAYER[0], get_state()): end_game()

        if pygame.time.get_ticks() - base_time >= 500:
            base_time = pygame.time.get_ticks()
            SCORE += 5
            if flag:
                flag = False
                TABY = 0
            else:
                flag = True
                TABY = -90

            for i in range(len(torres)):
                torres[i][1] += 90
            for i in range(len(peoes)):
                peoes[i][1] += 90
            for i in range(len(bispos)):
                bispos[i][1] += 90
            for i in range(len(cavalos)):
                cavalos[i][1] += 90

            if torres and torres[0][1] >= 800:
                torres.pop(0)
            if peoes and peoes[0][1] >= 800:
                peoes.pop(0)
            if bispos and bispos[0][1] >= 800:
                bispos.pop(0)
            if cavalos and cavalos[0][1] >= 800:
                cavalos.pop(0)

            # action = get_action({'player': PLAYER[0], 'state': state}, model='heuristica')
            if not ACTIONS:
                state = get_state()
                ACTIONS = get_action({'player': PLAYER[0], 'state': state}, model='GA')

            action = ACTIONS.pop(0)
            if action == 'FLIP':
                PLAYER[0] = flip()
                SCORE -= 5
            
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # if event.type == KEYDOWN:
                # if event.key == K_LEFT or event.key == K_a:
                #     PLAYER[0] = 560
                # elif event.key == K_RIGHT or event.key == K_d:
                #     PLAYER[0] = 644
                # SCORE -= 5
        reset_background()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def fase1():
    global torres
    global cavalos
    global bispos
    global peoes

    torre_left = 569
    torre_right = 653
    torres = [
        [torre_left, -245],
        [torre_left, -965],
        [torre_right, -1685],
        [torre_left, -1865],
        [torre_right, -2045],
        [torre_right, -2495],
        [torre_left, -3035],
        [torre_left, -3845],
        [torre_right, -4475],
        [torre_left, -5015],
        [torre_right, -5285],
        [torre_right, -7355],
        [torre_right, -8615]
    ]

    cavalo_left = 392
    cavalo_right = 812
    cavalos = [
        [cavalo_right, -515],
        [cavalo_right, -1415],
        [cavalo_left, -2405],
        [cavalo_left, -2765],
        [cavalo_left, -3215],
        [cavalo_right, -3395],
        [cavalo_left, -3575],
        [cavalo_right, -3755],
        [cavalo_right, -4925],
        [cavalo_right, -5285],
        [cavalo_right, -6185],
        [cavalo_left, -6455],
        [cavalo_right, -6635],
        [cavalo_left, -7265],
        [cavalo_left, -8165]
    ]

    bispo_left = 392
    bispo_right = 812
    bispos = [
        [bispo_left, -965],
        [bispo_right, -1775],
        [bispo_left, -3935],
        [bispo_right, -4475],
        [bispo_right, -4565],
        [bispo_right, -5735],
        [bispo_left, -5915],
        [bispo_right, -6095],
        [bispo_left, -6275],
        [bispo_right, -6995],
        [bispo_left, -7175],
        [bispo_right, -7895],
        [bispo_right, -7985],
        [bispo_left, -8525]
    ]

    peao_left = 485
    peao_right = 733
    peoes = [
        [peao_right, -65],
        [peao_right, -605],
        [peao_left, -1235],
        [peao_left, -2315],
        [peao_right, -2945],
        [peao_right, -4115],
        [peao_left, -4745],
        [peao_left, -6365],
        [peao_left, -7175],
        [peao_right, -7535],
        [peao_right, -7985],
        [peao_left, -8525]
    ]


def flip():
    return 560 if PLAYER[0] != 560 else 644


def get_state():
    state = {}
    tor = []
    pes = []
    bis = []
    cavs = []

    for i in range(len(torres)):
        if torres[i][1] >= 755:
            continue
        tor.append(torres[i].copy())

    for i in range(len(peoes)):
        if peoes[i][1] >= 755:
            continue
        pes.append(peoes[i].copy())

    for i in range(len(bispos)):
        if bispos[i][1] >= 755:
            continue
        bis.append(bispos[i].copy())

    for i in range(len(cavalos)):
        if cavalos[i][1] >= 755:
            continue
        cavs.append(cavalos[i].copy())

    state['torres'] = tor
    state['peoes'] = pes
    state['bispos'] = bis
    state['cavalos'] = cavs

    return state


def end_game():
    global SCORE
    SCORE -= 20
    print(SCORE)
    pygame.quit()
    sys.exit()


main()
