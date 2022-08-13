import sys

import pygame

pygame.init()


def mouseDown():
    pygame.time.wait(10)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (69, 45, 45), rect, 0)
    rect.move_ip(4, 4)
    pygame.draw.rect(screen, (255, 0, 0), rect, 0)


def mouseUp():
    pygame.time.wait(10)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (69, 45, 45), rect, 0)
    rect.move_ip(4, -4)
    pygame.draw.rect(screen, (255, 0, 0), rect, 0)


screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 200, 20, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.draw.rect(screen, (255, 45, 45), rect, 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseDown()

    if event.type == pygame.MOUSEBUTTONUP:
        mouseUp()

    pygame.display.flip()
