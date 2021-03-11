import pygame
import os  

WHITE = (255, 255, 255)
WIDTH, HEIGHT = 960, 540


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(WHITE)
