###################################
#    A-Level Exercise Connect4    #
#        Author: 环球教育         #
#        沈老师 18362711321       #
###################################

# SetGlobalVariables:
CurrentPlayer = 'x' #A Player can be 'x' or 'o'
Board = [['b']*7 for i in range(6)] #A Token Slot can be 'x' or 'o' or 'b'
CurrentInputRow = -1
CurrentInputColumn = -1
Winner = 'b' #The winner can be 'x' or 'o' or 'b' or 'draw'

def PlayerMove():
    global Winner
    DisplayBoard()
    while Winner == 'b':
        PlayerInput()
        DisplayBoard()
        Winner = CheckWinner()
        SwapPlayer()
    print("The Winner is,",CurrentPlayer)
    
def SwapPlayer():
    global CurrentPlayer
    print("This is ",CurrentPlayer,"\'s turn.")
    if CurrentPlayer == 'x':
        CurrentPlayer = 'o'
    else:
        CurrentPlayer = 'x'
        
def PlayerInput():
    ValidationPass = False
    while ValidationPass == False:
        column = int(input("Please select a column to insert token:")) -1
        ValidationPass = ValidateInput(column)
        
def ValidateInput(column):
    global Board
    global CurrentInputRow
    global CurrentInputColumn
    global CurrentPlayer
    
    
    if(column<0 or column>6): return False
    for row in range(5,0,-1):
        if Board[row][column] == 'b':
            CurrentInputRow = row
            CurrentInputColumn = column
            Board[CurrentInputRow][CurrentInputColumn] = CurrentPlayer #Update Board
            return True
    return False

def DisplayBoard():
    global Board
    for x in range(6):
        for y in range(7):
            print(Board[x][y],end=" ")
        print()
        
def CheckWinner():
    global Board
    global CurrentInputRow
    global CurrentInputColumn
    global CurrentPlayer
    global Winner
    #check horizontal
    HorizontalSum = 0
    #check left
    for column in range(CurrentInputColumn,0,-1):
        if Board[CurrentInputRow][column] == CurrentPlayer:
            HorizontalSum += 1
    #check right
    for column in range(CurrentInputColumn,6,1):
        if Board[CurrentInputRow][column] == CurrentPlayer:
            HorizontalSum += 1
    
    if(HorizontalSum>=4) : return CurrentPlayer

    #check vertical
    VerticalSum = 0
    #check up
    for row in range(CurrentInputRow,0,-1):
        if Board[row][CurrentInputColumn] == CurrentPlayer:
            VerticalSum += 1
    #check down
    for row in range(CurrentInputRow,5,1):
        if Board[row][CurrentInputColumn] == CurrentPlayer:
            VerticalSum += 1
    
    if (VerticalSum >=4) : return CurrentPlayer

    #check diagonal [ToBeContine...]
    
    #check draw [ToBeContine...]
    
    return 'b'

#Main
PlayerMove()