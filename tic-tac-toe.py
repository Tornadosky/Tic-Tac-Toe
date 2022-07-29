import pygame
import numpy

# specify constants to avoid magic numbers
WIDTH, HEIGHT = (420, 420)
N = 3
SQUARE_SIZE = WIDTH // N
LINE_WIDTH = 11
# constants for colors
GREY = (160, 160, 160)
BLACK = (18, 18, 18)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
pygame.display.set_caption("Tic Tac Toe")

# establish width and height of window and add color
surface = pygame.display.set_mode((WIDTH, HEIGHT))
surface.fill(GREY)

# internal representation of board
# Empty fields have the value 0
# Fields taken by Player 1 have the value 1
# Fields taken by Player 2 have the value 2
board = numpy.zeros((N, N))


# helper functions to work with board
def change_square(row, col, player_num):
    board[row][col] = player_num


def is_empty_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(N):
        for col in range(N):
            if board[row][col] == 0:
                return False
    return True


def draw_lines():
    # draw horizontal lines
    pygame.draw.line(surface, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(surface, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # draw vertical lines
    pygame.draw.line(surface, BLACK, (SQUARE_SIZE, 0), (WIDTH // 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(surface, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def restart():
    surface.fill(GREY)
    draw_lines()
    for row in range(N):
        for col in range(N):
            board[row][col] = 0


def main():
    restart()
    running = True

    while running:
        for event in pygame.event.get():

            # restart the game if 'r' is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    running = True
                    is_game_over = False
                    player_num = 1

            # event handler to handle quitting the application
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()


if __name__ == '__main__':
    main()
