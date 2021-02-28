import pygame
import os
import time

# Variables to be used inside of functions.
global Turn
Turn = 0

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


# Determines if a board if full
def is_Full(Board):
    if any(None in sublist for sublist in Board):
        return False
    else:
        return True


# Checks the position of a mouse click and draws an X/O, Appends the Board matrix with a 1 in the correct spot to reflect an X, 0 to relfect O
def draw_X(x, y, Board):
    global Turn
    # Checks if turn is an even number (i.e x's turn)
    if Turn % 2 == 0:
        # Series of statements checking the x and y pos of the mouse. Each mouse click lies in a specific box, draw the X/O in the center of the box,
        # making sure there is nothing in the box, and not to overwrite if an X or O already exist.
        if x < WIDTH / 3 and y < HEIGHT/3:
            if Board[0][0] == None:
                Board[0][0] = 1
                WIN.blit(X, (60, 60))
                # Increases Turn after each executed x drawing
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


# Takes a tuple, intended to be the best move returned from the minimax algorithm. Converts the best move into x and y coordinates and draws the O
def draw_O(pos):
    global Turn

    j, i = pos

    # Converts board position into x and y coordiantes:
    if i == 0:
        x = (WIDTH / 3) - 1
    if j == 0:
        y = (HEIGHT / 3) - 1

    if i == 1:
        x = (WIDTH - WIDTH / 3) - 1

    if j == 1:
        y = (HEIGHT - HEIGHT / 3) - 1

    if i == 2:
        x = WIDTH - 1

    if j == 2:
        y = HEIGHT - 1

    if x < WIDTH / 3 and y < HEIGHT/3:
        WIN.blit(O, (60, 60))
        Turn += 1
    elif x < WIDTH - WIDTH / 3 and y < HEIGHT/3:

        WIN.blit(O, (WIDTH / 3 + 60, 60))
        Turn += 1
    elif x < WIDTH and y < HEIGHT/3:

        WIN.blit(O, (WIDTH - WIDTH / 3 + 60, 60))
        Turn += 1
    elif x < WIDTH / 3 and y < HEIGHT - HEIGHT/3:

        WIN.blit(O, (60, HEIGHT / 3 + 60))
        Turn += 1
    elif x < WIDTH - WIDTH / 3 and y < HEIGHT - HEIGHT/3:

        WIN.blit(O, (WIDTH / 3 + 60, HEIGHT / 3 + 60))
        Turn += 1
    elif x < WIDTH and y < HEIGHT - HEIGHT/3:

        WIN.blit(O, (WIDTH - WIDTH / 3 + 60, HEIGHT / 3 + 60))
        Turn += 1
    elif x < WIDTH / 3 and y < HEIGHT:

        WIN.blit(O, (60, HEIGHT - HEIGHT / 3 + 60))
        Turn += 1
    elif x < WIDTH - WIDTH / 3 and y < HEIGHT:

        WIN.blit(O, (WIDTH / 3 + 60, HEIGHT - HEIGHT / 3 + 60))
        Turn += 1
    elif x < WIDTH and y < HEIGHT:
        WIN.blit(O, (WIDTH - WIDTH / 3 + 60, HEIGHT - HEIGHT / 3 + 60))
        Turn += 1


# Algorithm used to determine the best possible move that can be made against a human player
def minimax(Board, Depth, Maxplayer):

    # Checks for wins, if no wins exists return 0
    if has_Won(Board) == False and is_Full(Board) == True:
        return 0

    # If O has won , return 1
    if who_Won(Board) == 0:
        return 1 * Depth

    # If X has won, return -1
    if who_Won(Board) == 1:
        return -1 * Depth

    if Maxplayer == True:
        maxscore = float("-inf")
        for x in range(3):
            for y in range(3):
                if Board[x][y] == None:
                    Board[x][y] = 0
                    score = minimax(Board, Depth + 1, False)
                    maxscore = max(maxscore, score)
                    Board[x][y] = None

        return maxscore

    else:
        minscore = float("inf")
        for x in range(3):
            for y in range(3):
                if Board[x][y] == None:
                    Board[x][y] = 1
                    score = minimax(Board, Depth + 1, True)
                    minscore = min(minscore, score)
                    Board[x][y] = None

        return minscore


# Excuted during the computers turn
def AI_Logic():
    global Turn
    bestVal = float("-inf")

    for x in range(3):
        for y in range(3):
            if Board[x][y] == None:
                Board[x][y] = 0
                score = minimax(Board, 0, False)
                Board[x][y] = None

                if (score > bestVal):
                    bestMove = (x, y)
                    bestVal = score

    x, y = bestMove
    Board[x][y] = 0
    draw_O(bestMove)


def who_Won(Board):
    global hasWon
    # Checks for three of a kind in first column
    if Board[0][0] == Board[1][0] and Board[0][0] != None:
        if Board[1][0] == Board[2][0]:
            hasWon = 1
            return Board[2][0]
    if Board[0][0] == Board[0][1] and Board[0][0] != None:
        if Board[0][1] == Board[0][2]:
            hasWon = 1
            return Board[0][2]
    # Checks for diag win top Left to bottom right
    if Board[0][0] == Board[1][1] and Board[0][0] != None:
        if Board[1][1] == Board[2][2]:
            hasWon = 1
            return Board[2][2]
    # Checks for diag win bottom left to top right
    if Board[0][2] == Board[1][1] and Board[0][2] != None:
        if Board[1][1] == Board[2][0]:
            hasWon = 1
            return Board[2][0]
    # Checks for center column win
    if Board[0][1] == Board[1][1] and Board[0][1] != None:
        if Board[1][1] == Board[2][1]:
            hasWon = 1
            return Board[2][1]
    # Checks for right column win:
    if Board[0][2] == Board[1][2] and Board[0][2] != None:
        if Board[1][2] == Board[2][2]:
            hasWon = 1
            return Board[2][2]
    # Checks for second row win:
    if Board[1][0] == Board[1][1] and Board[1][0] != None:
        if Board[1][1] == Board[1][2]:
            hasWon = 1
            return Board[1][2]
    # Checks for third row win:
    if Board[2][0] == Board[2][1] and Board[2][0] != None:
        if Board[2][1] == Board[2][2]:
            hasWon = 1
            return Board[2][2]
    else:
        return -1


def has_Won(Board):

    # Checks for three of a kind in first column
    if Board[0][0] == Board[1][0] and Board[0][0] != None:
        if Board[1][0] == Board[2][0]:
            return True
    if Board[0][0] == Board[0][1] and Board[0][0] != None:
        if Board[0][1] == Board[0][2]:
            return True
    # Checks for diag win top Left to bottom right
    if Board[0][0] == Board[1][1] and Board[0][0] != None:
        if Board[1][1] == Board[2][2]:
            return True
    # Checks for diag win bottom left to top right
    if Board[0][2] == Board[1][1] and Board[0][2] != None:
        if Board[1][1] == Board[2][0]:
            return True
    # Checks for center column win
    if Board[0][1] == Board[1][1] and Board[0][1] != None:
        if Board[1][1] == Board[2][1]:
            return True
    # Checks for right column win:
    if Board[0][2] == Board[1][2] and Board[0][2] != None:
        if Board[1][2] == Board[2][2]:
            return True
    # Checks for second row win:
    if Board[1][0] == Board[1][1] and Board[1][0] != None:
        if Board[1][1] == Board[1][2]:
            return True
    # Checks for third row win:
    if Board[2][0] == Board[2][1] and Board[2][0] != None:
        if Board[2][1] == Board[2][2]:
            return True

    return False


# Executes every frame, draws the board and updates the display
def draw_Window():
    draw_Board()
    pygame.display.update()


# Main Event Loop
def main():
    global Turn
    FPS = 20
    run = True
    WIN.fill((255, 255, 255))
    clock = pygame.time.Clock()

    while run:

        clock.tick(FPS)
        draw_Window()
        # Runs the AI turn on odd numbered turns, and if board is not full
        if Turn % 2 != 0 and is_Full(Board) == False:
            while x:
                AI_Logic()
                x = False
        # Checks for winner
        if has_Won(Board) == True:
            if who_Won(Board) == 0:
                print("O Wins!")

            run = False

        # Checks for Tie
        if has_Won(Board) == False and is_Full(Board) == True:
            print("Tie!")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Checks if a mouse is clicked. When clicked, it records the x and y pos of the mouse and passes it through the draw_X function
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                draw_X(x, y, Board)
        pygame.display.update()
    pygame.quit()


main()
