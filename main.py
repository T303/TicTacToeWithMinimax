import pygame
from opponent import Bot
import pygame
import math

pygame.init()



screen = pygame.display.set_mode((480,480))

WHITE = (255,255,255)
BLACK = (0,0,0)
#This is my test game board for now
#This should normally just be a blank board like the one commented below
          #0   #1   #2
tiles = [["o", "", "x"], #1st row : index 0
         ["x", "", ""], #2nd row : index 1
         ["x", "o", "o"]] #3rd row : index 2

          #0   #1   #2
#tiles = [["", "", ""], #1st row : index 0
#         ["", "", ""], #2nd row : index 1
#         ["", "", ""]] #3rd row : index 2

bot = Bot(tiles)

Running = True

def printBoard(gameboard):
    for i in range(len(gameboard)):
        currentRow = ""
        for j in range(len(gameboard[i])):
            if(gameboard[i][j] == ""):
                currentRow += "-"
            else:
                currentRow += str(gameboard[i][j])
        print(currentRow)

font = pygame.font.Font('freesansbold.ttf', 128)

#Testing my list of possible moves function with the current game state
#It should print three possible game boards in the console with three seperate moves (an x in three unique positions)
bot.getListOfPossibleMoves(tiles)

def winCheck():
  global Running
  #Checking each column
  if tiles[0][0] != "" and tiles[0][0] == tiles[0][1] and tiles[0][0] == tiles[0][2]: #Checks top row
    print("Player " + tiles[0][0] + " wins!")
    Running = False
  elif tiles[1][0] != "" and tiles[1][0] == tiles[1][1] and tiles[1][0] == tiles[1][2]:
    print("Player " + tiles[1][0] + " wins!")
    Running = False
  elif tiles[2][0] != "" and tiles[2][0] == tiles[2][1] and tiles[2][0] == tiles[2][2]:
    print("Player", tiles[2][0], "wins!")
    Running = False
    
  #Checking each row
  if tiles[0][0] != "" and tiles[0][0] == tiles[1][0] and tiles[0][0] == tiles[2][0]:
    print("Player " + tiles[0][0] + " wins!")
    Running = False
  elif tiles[0][1] != "" and tiles[0][1] == tiles[1][1] and tiles[0][1] == tiles[2][1]:
    print("Player " + tiles[0][1] + " wins!")
    Running = False
  elif tiles[0][2] != "" and tiles[0][2] == tiles[1][2] and tiles[0][2] == tiles[2][2]:
    print("Player", tiles[0][2], "wins!")
    Running = False

  # Checking Diagonals
  if tiles[0][0] != "" and tiles[0][0] == tiles[1][1] and tiles[0][0] == tiles [2][2]:
    print("Player", tiles[0][0], "wins!")
    Running = False
  elif tiles[0][2] != "" and tiles[0][2] == tiles[1][1] and tiles[0][2] == tiles[2][0]:
    print("Player", tiles[0][2], "wins!")
    Running = False

playerTurn = 1    

while Running:
  screen.fill(WHITE)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      Running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        row = math.floor(x/160)
        column = math.floor(y/160)
        if tiles[column][row] == "":
            if playerTurn % 2 == 0:
                tiles[column][row] = "O"
                playerTurn = playerTurn + 1
            else:
                tiles[column][row] = "X"
                playerTurn = playerTurn + 1
        printBoard(tiles)
        winCheck()

        
        
  for i in range(0, len(tiles)):
    for j in range(0, len(tiles[i])):
      text = font.render(tiles[j][i], True, BLACK)
      screen.blit(text, (((i+.2)*160),((j+.15)*160)))


  pygame.draw.line(screen, BLACK, (160, 0),(160,480), 5)
  pygame.draw.line(screen, BLACK, (320, 0),(320,480), 5)
  pygame.draw.line(screen, BLACK, (0, 160),(480,160), 5)
  pygame.draw.line(screen, BLACK, (0, 320),(480,320), 5)
  pygame.display.flip()