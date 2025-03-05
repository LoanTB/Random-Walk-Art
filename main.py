import random
import pygame
pygame.init()
resolution = (300,300)
screen = pygame.display.set_mode(resolution)
screen.fill([255,255,255])

info = list([resolution[0]/2, resolution[1]/2, list([random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)])])
timer = pygame.time.Clock()
while True:
    info[0] += random.randint(-1, 1)
    info[1] += random.randint(-1, 1)
    if (info[0] > resolution[0]) or (info[0] < 0) or (info[1] > resolution[1]) or (info[1] < 0):
        info = list([resolution[0]/2, resolution[1]/2, [random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)]])
    screen.set_at((int(info[0]),int(info[1])), info[2])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            exit()
