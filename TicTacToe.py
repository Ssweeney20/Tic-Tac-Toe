import pygame
import os
import time

# Variables to be used inside of functions.
global Turn
global hasWon
Turn = 0
hasWon = 0

# Creates Window
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Import X and O Image
X = pygame.image.load(os.path.join("Assets", "X.png"))
O = pygame.image.load(os.path.join("Assets", "O.png"))

# 3x3 Matrix used for game logic
Board = [[None]*3, [None]*3, [None]*3]


# Draw lines to seperate the screen into specific rows/cols
def draw_Board():
    pygame.draw.line(WIN, (0, 0, 0), ((WIDTH / 3), 0), ((WIDTH / 3), HEIGHT))
    pygame.draw.line(WIN, (0, 0, 0), (600, 0), (600, HEIGHT))
    pygame.draw.line(WIN, (0, 0, 0), (0, (HEIGHT/3)), ((WIDTH), HEIGHT / 3))
    pygame.draw.line(WIN, (0, 0, 0), (0, 600), (WIDTH, 600))


# Checks the position of a mouse click and draws an X/O, Appends the Board matrix with a 1 in the correct spot to reflect an X, 0 to relfect O
def draw_X(x, y):
    global Turn
    # Checks if turn is an even number (i.e x's turn)
    if Turn % 2 == 0:
        # Series of statements checking the x and y pos of the mouse. Each mouse click lies in a specific box, draw the X/O in the center of the box,
        # making sure there is nothing in the box, and not to overwrite if an X or O already exist.
        if x < WIDTH / 3 and y < HEIGHT/3:
            if Board[0][0] == None:
                Board[0][0] = 1
                WIN.blit(X, (60, 60))
                # Increases Turn after each executed x or O drawing
                Turn += 1
        elif x < WIDTH - WIDTH / 3 and y < HEIGHT/3:
            if Board[0][1] == None:
                Board[0][1] = 1
                WIN.blit(X, (WIDTH / 3 + 60, 60))
                Turn += 1
        elif x < WIDTH and y < HEIGHT/3:
            if Board[0][2] == None:
                Board[0][2] = 1
                WIN.blit(X, (WIDTH - WIDTH / 3 + 60, 60))
                Turn += 1
        elif x < WIDTH / 3 and y < HEIGHT - HEIGHT/3:
            if Board[1][0] == None:
                Board[1][0] = 1
                WIN.blit(X, (60, HEIGHT / 3 + 60))
                Turn += 1
        elif x < WIDTH - WIDTH / 3 and y < HEIGHT - HEIGHT/3:
            if Board[1][1] == None:
                Board[1][1] = 1
                WIN.blit(X, (WIDTH / 3 + 60, HEIGHT / 3 + 60))
                Turn += 1
        elif x < WIDTH and y < HEIGHT - HEIGHT/3:
            if Board[1][2] == None:
                Board[1][2] = 1
                WIN.blit(X, (WIDTH - WIDTH / 3 + 60, HEIGHT / 3 + 60))
                Turn += 1
        elif x < WIDTH / 3 and y < HEIGHT:
            if Board[2][0] == None:
                Board[2][0] = 1
                WIN.blit(X, (60, HEIGHT - HEIGHT / 3 + 60))
                Turn += 1
        elif x < WIDTH - WIDTH / 3 and y < HEIGHT:
            if Board[2][1] == None:
                Board[2][1] = 1
                WIN.blit(X, (WIDTH / 3 + 60, HEIGHT - HEIGHT / 3 + 60))
                Turn += 1
        elif x < WIDTH and y < HEIGHT:
            if Board[2][2] == None:
                Board[2][2] = 1
                WIN.blit(X, (WIDTH - WIDTH / 3 + 60, HEIGHT - HEIGHT / 3 + 60))
                Turn += 1

    # On odd number turns, O will be drawn onto the board:
    else:
        if x < WIDTH / 3 and y < HEIGHT/3:
            if Board[0][0] == None:
                Board[0][0] = 0
                WIN.blit(O, (60, 60))
                Turn += 1
        elif x < WIDTH - WIDTH / 3 and y < HEIGHT/3:
            if Board[0][1] == None:
                Board[0][1] = 0
                WIN.blit(O, (WIDTH / 3 + 60, 60))
                Turn += 1
        elif x < WIDTH and y < HEIGHT/3:
            if Board[0][2] == None:
                Board[0][2] = 0
                WIN.blit(O, (WIDTH - WIDTH / 3 + 60, 60))
                Turn += 1
        elif x < WIDTH / 3 and y < HEIGHT - HEIGHT/3:
            if Board[1][0] == None:
                Board[1][0] = 0
                WIN.blit(O, (60, HEIGHT / 3 + 60))
                Turn += 1
        elif x < WIDTH - WIDTH / 3 and y < HEIGHT - HEIGHT/3:
            if Board[1][1] == None:
                Board[1][1] = 0
                WIN.blit(O, (WIDTH / 3 + 60, HEIGHT / 3 + 60))
                Turn += 1
        elif x < WIDTH and y < HEIGHT - HEIGHT/3:
            if Board[1][2] == None:
                Board[1][2] = 0
                WIN.blit(O, (WIDTH - WIDTH / 3 + 60, HEIGHT / 3 + 60))
                Turn += 1
        elif x < WIDTH / 3 and y < HEIGHT:
            if Board[2][0] == None:
                Board[2][0] = 0
                WIN.blit(O, (60, HEIGHT - HEIGHT / 3 + 60))
                Turn += 1
        elif x < WIDTH - WIDTH / 3 and y < HEIGHT:
            if Board[2][1] == None:
                Board[2][1] = 0
                WIN.blit(O, (WIDTH / 3 + 60, HEIGHT - HEIGHT / 3 + 60))
                Turn += 1
        elif x < WIDTH and y < HEIGHT:
            if Board[2][2] == None:
                Board[2][2] = 0
                WIN.blit(O, (WIDTH - WIDTH / 3 + 60, HEIGHT - HEIGHT / 3 + 60))
                Turn += 1


# Checks for Wins
def game_Logic():
    global hasWon
    # Checks for three of a kind in first column
    if Board[0][0] == Board[1][0] and Board[0][0] != None:
        if Board[1][0] == Board[2][0]:
            hasWon = 1
    if Board[0][0] == Board[0][1] and Board[0][0] != None:
        if Board[0][1] == Board[0][2]:
            hasWon = 1
    # Checks for diag win top Left to bottom right
    if Board[0][0] == Board[1][1] and Board[0][0] != None:
        if Board[1][1] == Board[2][2]:
            hasWon = 1
    # Checks for diag win bottom left to top right
    if Board[0][2] == Board[1][1] and Board[0][2] != None:
        if Board[1][1] == Board[2][0]:
            hasWon = 1
    # Checks for center column win
    if Board[0][1] == Board[1][1] and Board[0][1] != None:
        if Board[1][1] == Board[2][1]:
            hasWon = 1
    # Checks for right column win:
    if Board[0][2] == Board[1][2] and Board[0][2] != None:
        if Board[1][2] == Board[2][2]:
            hasWon = 1
    # Checks for second row win:
    if Board[1][0] == Board[1][1] and Board[1][0] != None:
        if Board[1][1] == Board[1][2]:
            hasWon = 1
    # Checks for third row win:
    if Board[2][0] == Board[2][1] and Board[2][0] != None:
        if Board[2][1] == Board[2][2]:
            hasWon = 1


# Executes every frame, draws the board, checks for wins, and updates the display
def draw_Window():

    draw_Board()
    game_Logic()
    pygame.display.update()


# Main Event Loop
def main():
    FPS = 60
    run = True
    WIN.fill((255, 255, 255))
    clock = pygame.time.Clock()

    while run:

        clock.tick(FPS)
        draw_Window()
        # Checks for winner
        if hasWon == 1:
            print("Winner!")
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Checks if a mouse is clicked. When clicked, it records the x and y pos of the mouse and passes it through the draw_X function
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                draw_X(x, y)
        pygame.display.update()
    pygame.quit()


main()
