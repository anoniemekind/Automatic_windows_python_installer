import pygame
import numpy as np
import sys

#NumWorks resolution
W, H = 320, 222

pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()


#KANDINSKY (functions)
def fill_rect(x, y, w, h, color):
    pygame.draw.rect(screen, color, (x, y, w, h))

def set_pixel(x, y, color):
    screen.set_at((x, y), color)

def draw_string(text, x, y, text_color, bg_color):
    font = pygame.font.SysFont("Arial", 16)
    surf = font.render(text, True, text_color, bg_color)
    screen.blit(surf, (x, y))

#ION (constants + function)
KEY_LEFT = 0
KEY_UP = 1
KEY_DOWN = 2
KEY_RIGHT = 3
KEY_OK = 4
KEY_BACK = 5
KEY_SHIFT = 6
KEY_ALPHA = 7
KEY_HOME = 8

KEY_0 = 10
KEY_1 = 11
KEY_2 = 12
KEY_3 = 13
KEY_4 = 14
KEY_5 = 15
KEY_6 = 16
KEY_7 = 17
KEY_8 = 18
KEY_9 = 19

_keymap = {
    KEY_LEFT: pygame.K_LEFT,
    KEY_RIGHT: pygame.K_RIGHT,
    KEY_UP: pygame.K_UP,
    KEY_DOWN: pygame.K_DOWN,
    KEY_OK: pygame.K_RETURN,
    KEY_BACK: pygame.K_BACKSPACE,
    KEY_SHIFT: pygame.K_LSHIFT,
    KEY_ALPHA: pygame.K_LALT,
    KEY_HOME: pygame.K_ESCAPE,

    KEY_0: pygame.K_0,
    KEY_1: pygame.K_1,
    KEY_2: pygame.K_2,
    KEY_3: pygame.K_3,
    KEY_4: pygame.K_4,
    KEY_5: pygame.K_5,
    KEY_6: pygame.K_6,
    KEY_7: pygame.K_7,
    KEY_8: pygame.K_8,
    KEY_9: pygame.K_9,
}

def keydown(key):
    keys = pygame.key.get_pressed()
    return keys[_keymap.get(key, 0)]

#NUMWORKS INIT CODE STARTS HERE----------------------------------------

fps = 50
delta = 1 / fps

x = 150
y = 100

#NUMWORKS INIT CODE ENDS HERE----------------------------------------

while True:
    #be able to close pygame window on computer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #NUMWORKS FOREVER LOOP CODE STARTS HERE----------------------------------------

    screen.fill((0, 0, 0))

    # Example movement
    if keydown(KEY_LEFT):
        x -= 120 * delta
    if keydown(KEY_RIGHT):
        x += 120 * delta
    if keydown(KEY_UP):
        y -= 120 * delta
    if keydown(KEY_DOWN):
        y += 120 * delta

    fill_rect(int(x), int(y), 20, 20, (0, 255, 255))

    #NUMWORKS FOREVER LOOP CODE ENDS HERE----------------------------------------

    #update pygame frame not pastable in numworks
    pygame.display.flip()
    clock.tick(fps)
