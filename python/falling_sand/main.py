import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1000, 1000
CELL_SIZE = 5
PILE_SIZE = 10
CHANCE = 70
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

colors = [RED, YELLOW]

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Sand Simulator")

grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
def color_sand():
    if random.randint(0, 100) < 1:
        return 0
    else:
        return 1

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)


def draw_filled_cells():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col] == 1:
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, colors[color_sand()], rect)


def fill_cell_with_mouse():
    x, y = pygame.mouse.get_pos()
    grid_x = x // CELL_SIZE
    grid_y = y // CELL_SIZE

    if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
        for i in range(20):
            rand_x_offset = random.randint(0, PILE_SIZE)
            rand_y_offset = random.randint(0, PILE_SIZE)

            new_x_pos_right = grid_x + rand_x_offset
            new_x_pos_left = grid_x - rand_x_offset
            new_y_pos = grid_y + rand_y_offset

            if 0 <= new_y_pos < GRID_HEIGHT:
                if 0 <= new_x_pos_right < GRID_WIDTH and random.randint(0, 100) < CHANCE:
                    grid[new_y_pos][new_x_pos_right] = 1
                elif 0 <= new_x_pos_left < GRID_WIDTH and random.randint(0, 100) < CHANCE:
                    grid[new_y_pos][new_x_pos_left] = 1

        grid[grid_y][grid_x] = 1


def check_falling():
    for row in range(GRID_HEIGHT - 2, -1, -1):
        for col in range(GRID_WIDTH):
            if grid[row][col] == 1 and grid[row + 1][col] == 0:
                grid[row][col] = 0
                grid[row + 1][col] = 1


            if grid[row][col] == 1 and grid[row + 1][col] == 1:
                if col + 1 < GRID_WIDTH and grid[row + 1][col + 1] == 0:
                    grid[row][col] = 0
                    grid[row + 1][col + 1] = 1


            if grid[row][col] == 1 and grid[row + 1][col] == 1:
                if col - 1 >= 0 and grid[row + 1][col - 1] == 0:
                    grid[row][col] = 0
                    grid[row + 1][col - 1] = 1


running = True
while running:
    screen.fill(BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        fill_cell_with_mouse()

    check_falling()

    draw_filled_cells()
    draw_grid()

    pygame.display.flip()
    clock.tick(60)
# Pygame beenden
pygame.quit()
sys.exit()
