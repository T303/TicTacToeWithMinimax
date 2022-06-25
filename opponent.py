class Bot:
  def __init__(self, tiles):
    self.tiles = tiles
    self.scores = []
  
  def generateScoresList(self):
    """Assign values based on each move."""
    pass

  def printBoard(self, gameboard):
    for i in range(len(gameboard)):
        currentRow = ""
        for j in range(len(gameboard[i])):
            if(gameboard[i][j] == ""):
                currentRow += "-"
            else:
                currentRow += str(gameboard[i][j])
        print(currentRow)

  def generatePossibleMove(self, gameboard, row, col):
    newGameboard = [["", "", ""], ["", "", ""], ["", "", ""]]
    for i in range(3):
      #newCol = []
      for j in range(3):
        #newCol.append(gameboard[i][j])
        newGameboard[i][j] = gameboard[i][j]
      #newGameboard.append(newCol)
    print("Setting tile " + str(row) + ", " + str(col) + " to an X")
    newGameboard[row][col] = "x"
    return newGameboard

  def getListOfPossibleMoves(self, gameboard):
    listOfPossibleGameBoards = []
    for i in range(3):
      for j in range(3):
        if (gameboard[i][j] == ""):
          self.printBoard(self.generatePossibleMove(gameboard, i, j))
          listOfPossibleGameBoards.append(self.generatePossibleMove(gameboard, i, j))
          pass
    
    return listOfPossibleGameBoards

  def returnMaxScore(self):
    """Return maximum score from scores list."""
    pass

  def returnMinScore(self):
    """Return minimum score from scores list."""
    pass

  def scoreOfGameState(self, tiles):
    #Checking Columns
    if tiles[0][0] != "" and tiles[0][0] == tiles[0][1] and tiles[0][0] == tiles[0][2]:
      if(tiles[0][0] == 'X'):
        return 1
      else:
        return -1
    elif tiles[1][0] != "" and tiles[1][0] == tiles[1][1] and tiles[1][0] == tiles[1][2]:
      if(tiles[1][0] == 'X'):
        return 1
      else:
        return -1
    elif tiles[2][0] != "" and tiles[2][0] == tiles[2][1] and tiles[2][0] == tiles[2][2]:
      if(tiles[2][0] == 'X'):
        return 1
      else:
        return -1
    
    #Checking each row
    if tiles[0][0] != "" and tiles[0][0] == tiles[1][0] and tiles[0][0] == tiles[2][0]:
      if(tiles[0][0] == 'X'):
        return 1
      else:
        return -1
    elif tiles[0][1] != "" and tiles[0][1] == tiles[1][1] and tiles[0][1] == tiles[2][1]:
      if(tiles[0][1] == 'X'):
        return 1
      else:
        return -1
    elif tiles[0][2] != "" and tiles[0][2] == tiles[1][2] and tiles[0][2] == tiles[2][2]:
      if(tiles[0][2] == 'X'):
        return 1
      else:
        return -1

    # Checking Diagonals
    if tiles[0][0] != "" and tiles[0][0] == tiles[1][1] and tiles[0][0] == tiles [2][2]:
      if(tiles[0][0] == 'X'):
        return 1
      else:
        return -1
    elif tiles[0][2] != "" and tiles[0][2] == tiles[1][1] and tiles[0][2] == tiles[2][0]:
      if(tiles[0][2] == 'X'):
        return 1
      else:
        return -1

    return 0

  def minimax(self, gameboard):
    #This is the main minimax algorithm that makes use of the above functions
    #Hunter is still working on the above functions so have him work through some of the basic funcionlity like:
    #1. Generating a list of possible moves
    #2. Scoring the result of each possible move in the list using scoreOfGameState function
    #3. Test the functions and watch to see what the list of possible moves returns when you make moves (the gameboard if each possible move should print in the console)
    currentScore = self.scoreOfGameState(gameboard)
    if(not currentScore == 0):
      return currentScore
    
    scores = []
    moves = []

    possibleMoves = self.getListOfPossibleMoves(gameboard)
    #WORK IN PROGRESS
    for move in possibleMoves:
      scores.append(self.minimax(move))
      moves.append(move)
    
    