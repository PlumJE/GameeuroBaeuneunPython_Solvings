""" Pygame의 기본 형식 """

import sys
import pygame
import random
from pygame.locals import QUIT, Rect

WIDTH = 800
HEIGHT = 600
SQSIZE = 50

pygame.init()
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()

class Player:
    def __init__(self, health, level):
        self.health = health
        self.level = level

    def move(self, key):
        if key == K_LEFT:
            xpos -= 1
        elif key == K_RIGHT:
            xpos += 1
        elif key == K_UP:
            ypos -= 1
        elif key == K_DOWN:
            ypos += 1

    def draw(self):
        pygame.draw.rect(SURFACE, (255, 0, 255), Rect(30, 30, 30, 30))

class Place:
    def __init__(self):
        pass
    
def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255, 255, 255))
        for index in range(0, WIDTH, SQSIZE):
            pygame.draw.line(SURFACE, (96, 96, 96), (index, 0), (index, HEIGHT))
        for index in range(0, HEIGHT, SQSIZE):
            pygame.draw.line(SURFACE, (96, 96, 96), (0, index), (WIDTH, index))

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == "__main__":
    main()
