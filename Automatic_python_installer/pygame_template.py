import pygame
import sys
from math import *

# Initialize pygame
pygame.init()

# Get screen info for fullscreen
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# Create fullscreen window
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Pygame Template")

# Draw rectangle with (x, y) = top-left corner
def draw_rect(x, y, w, h, col):
    pygame.draw.rect(screen, col, (x, y, w, h))

# Draw rectangle with (x, y) = center of the rectangle
def draw_rect_centered(x, y, w, h, col):
    pygame.draw.rect(screen, col, (x - w / 2, y - h / 2, w, h))

def draw_line(p1, p2, col, thickness = 1):
    pygame.draw.line(screen, col, p1, p2, thickness)

# Draw triangle, if w == 0, then it gets filled, if w > 0, only the outline will be drawn with width = w
def draw_triangle(p1, p2, p3, col, w = 0):
    pygame.draw.polygon(screen, col, [p1, p2, p3], w)

def clear_screen(col):
    screen.fill(col)

# Draw text (top-left position)
def draw_text(text, x, y, size, col, font_name=None):
    font = pygame.font.SysFont(font_name, size)
    text_surface = font.render(text, True, col)
    screen.blit(text_surface, (x, y))

# Draw centered text
def draw_text_centered(text, x, y, size, col, font_name=None):
    font = pygame.font.SysFont(font_name, size)
    text_surface = font.render(text, True, col)
    rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, rect)

def update():
    pygame.display.flip()

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Square settings
square_size = 100
square_x = (screen_width - square_size) // 2
square_y = (screen_height - square_size) // 2
speed = 500

clock = pygame.time.Clock()


fps = 120
#delta = 1/fps

# Main loop
running = True
while running:
    delta = clock.tick(fps) / 1000

    # Just pressed keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Press ESC to quit fullscreen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Continuously pressed keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        square_x -= speed * delta
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        square_x += speed * delta
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        square_y -= speed * delta
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        square_y += speed * delta

    clear_screen(BLACK)

    draw_text("Press esc to quit", 0, 0, 128, WHITE)

    fps_real = clock.get_fps()
    draw_text(f"FPS: {fps_real:.2f}", 10, 100, 40, WHITE)

    draw_rect(square_x, square_y, square_size, square_size, RED)

    update()

# Quit pygame properly
pygame.quit()
sys.exit()