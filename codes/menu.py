import pygame, sys

mainClock = pygame.time.Clock()
from pygame.locals import *
from game import Game

pygame.init()
pygame.display.set_caption('Projet RPG')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        draw_text('new_game', font, (255, 255, 255), screen, 20, 80)
        draw_text('credits', font, (255, 255, 255), screen, 20, 180)
        draw_text('quit', font, (255, 255, 255), screen, 20, 280)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                jeu = Game()
                jeu.run()

        if button_2.collidepoint((mx, my)):
            if click:
                credits()

        if button_3.collidepoint((mx, my)):
            if click:
                quit_the_game()

        pygame.draw.rect(screen, (150, 0, 205), button_1)
        pygame.draw.rect(screen, (164, 66, 220), button_2)
        pygame.draw.rect(screen, (181, 100, 227), button_3)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def new_game():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('new_game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def credits():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Raphaël LOUISON', font, (255, 255, 255), screen, 20, 20)
        draw_text('HUGO FESNIERE', font, (255, 255, 255), screen, 20, 50)
        draw_text('Gstave CONSTANS', font, (255, 255, 255), screen, 20, 80)
        draw_text('Phara MILLAURIAUX', font, (255, 255, 255), screen, 20, 110)
        draw_text('Maxime AIT ADDA', font, (255, 255, 255), screen, 20, 140)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def quit_the_game():
    pygame.quit()
    sys.exit