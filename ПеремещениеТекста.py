import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('My first pygame programm')
pygame.display.set_icon(pygame.image.load('imege.jpg'))

font = pygame.font.SysFont('comicsans', 32)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
x, y = (0, 300)
direct_x = 1
direct_y = 1

clock = pygame.time.Clock()
follow = font.render("Подписывайся на канал", 1, RED, GREEN)
telegram = font.render("Вступай в чат в ТГ", 1, GREEN, BLUE)
width, height = telegram.get_size()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(60)
    screen.fill(BLACK)
    screen.blit(follow, (100, 10))
    screen.blit(telegram, (x, y))

    x+=direct_x
    if x+width >= 600 or x<0:
        direct_x = -direct_x

    y += direct_y
    if y + height >= 400 or y < 0:
        direct_y = -direct_y

    pygame.display.update()