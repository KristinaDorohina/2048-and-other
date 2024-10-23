import pygame
from numpy.ma.core import empty

pygame.init()


def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)

def get_number_from_index(i, j):
    return i * 4 + j + 1

def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty

mas = [[0] * 4 for _ in range(4)]

mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)

#while True:
    #for event in pygame.event.get():
#


    #pygame.display.update()
