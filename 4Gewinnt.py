#4Gewinnt
def printLogo():
    print("""
     /$$   /$$        /$$$$$$                          /$$                       /$$
    | $$  | $$       /$$__  $$                        |__/                      | $$
    | $$  | $$      | $$  \__/  /$$$$$$  /$$  /$$  /$$ /$$ /$$$$$$$  /$$$$$$$  /$$$$$$
    | $$$$$$$$      | $$ /$$$$ /$$__  $$| $$ | $$ | $$| $$| $$__  $$| $$__  $$|_  $$_/
    |_____  $$      | $$|_  $$| $$$$$$$$| $$ | $$ | $$| $$| $$  \ $$| $$  \ $$  | $$
          | $$      | $$  \ $$| $$_____/| $$ | $$ | $$| $$| $$  | $$| $$  | $$  | $$ /$$
          | $$      |  $$$$$$/|  $$$$$$$|  $$$$$/$$$$/| $$| $$  | $$| $$  | $$  |  $$$$/
          |__/       \______/  \_______/ \_____/\___/ |__/|__/  |__/|__/  |__/   \___/
    """)

def printPlayer1():
    print("""
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      _____  _                         __            _           _
     |  __ \| |                       /_ |          (_)         | |
     | |__) | | __ _ _   _  ___ _ __   | | __      ___ _ __  ___| |
     |  ___/| |/ _` | | | |/ _ \ '__|  | | \ \ /\ / / | '_ \/ __| |
     | |    | | (_| | |_| |  __/ |     | |  \ V  V /| | | | \__ \_|
     |_|    |_|\__,_|\__, |\___|_|     |_|   \_/\_/ |_|_| |_|___(_)
                      __/ |
                     |___/
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    """)

def printPlayer2():
    print("""
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
      _____  _                         ___             _           _
     |  __ \| |                       |__ \           (_)         | |
     | |__) | | __ _ _   _  ___ _ __     ) | __      ___ _ __  ___| |
     |  ___/| |/ _` | | | |/ _ \ '__|   / /  \ \ /\ / / | '_ \/ __| |
     | |    | | (_| | |_| |  __/ |     / /_   \ V  V /| | | | \__ \_|
     |_|    |_|\__,_|\__, |\___|_|    |____|   \_/\_/ |_|_| |_|___(_)
                      __/ |
                     |___/
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    """)

printLogo()

#Field width
width = int(input("Breite des Spielfeldes eingeben: "))
while width < 4:
    print("Die Eingebene Zahl ist zu klein.")
    width = int(input("Breite des Spielfeldes eingeben: "))

#Field height
height = int(input("Höhe des Spielfeldes eingeben: "))
while height < 4:
    print("Die Eingebene Zahl ist zu klein.")
    height = int(input("Höhe des Spielfeldes eingeben: "))

#Initilize field
field = [[-1 for y in range(height)] for x in range(width)]

#Set up game
player1Turn = False

def wipe():
    global width
    global height
    global field

    printField(width, height)

    if(player1Turn):
        printPlayer2()
    else:
        printPlayer1()

    width = 0
    height = 0
    field = 0

    printLogo()

    width = int(input("Breite des Spielfeldes eingeben: "))
    while width < 4:
        print("Die Eingebene Zahl ist zu klein.")
        width = int(input("Breite des Spielfeldes eingeben: "))
    height = int(input("Höhe des Spielfeldes eingeben: "))
    while height < 4:
        print("Die Eingebene Zahl ist zu klein.")
        height = int(input("Höhe des Spielfeldes eingeben: "))

    field = [[-1 for y in range(height)] for x in range(width)]
    print(field)

def drop(player1Turn, width, height, field):
    #Input x
    print("It's Player "+str(int(player1Turn)+1)+"'s turn!")
    x = int(input("Spalte eingeben: "))-1
    while(x > width-1):
        print("Die Eingebene Zahl ist zu groß.")
        x = int(input("Spalte eingeben: "))-1
    while(x < 0):
        print("Die Eingebene Zahl ist zu klein.")
        x = int(input("Spalte eingeben: "))-1
    y = height-1
    #Check for empty field position
    while(field[x][y] != -1):
        if(y >= 1):
            y -= 1
        else:
            return(player1Turn)
    #Set field position to player
    field[x][y] = int(player1Turn)
    check(player1Turn, width, height, field)
    player1Turn = not player1Turn
    return(player1Turn)

def checkFull(field):
    #Check for empty field
    for x in range(width):
        for y in range(height):
            if field[x][y] == -1:
                return False
    return True

def check(player1Turn, width, height, field):
    if(checkFull(field)):
        wipe()

    streak = 0
    #Check verical
    for x in range(width):
        for y in range(height):
            if(field[x][y] == int(player1Turn)):
                streak += 1
            else:
                streak = 0
        #If 4 in vertical row, win
        if(streak >= 4):
            wipe()

    #Check horizontal
    for y in range(height):
        for x in range(width):
            if(field[x][y] == int(player1Turn)):
                streak += 1
            else:
                streak = 0
        #If 4 in horizontal row, win
        if(streak >= 4):
            wipe()

def printLine(width):
    line = "+"
    for i in range(0, width):
        line += "-----+"
    print(line)

def printTopLine(width):
    line = ""
    for i in range(0, width):
        line += "   " + str(i+1) + "  "
    print(line)

def printField(width, height):
    global field
    line = ""

    print("\n")
    printTopLine(width)

    for countY in range(height):
        for countX in range(width):
            if(str(field[countX][countY]) == "-1"):
                output = "     "
            elif(str(field[countX][countY]) == "0"):
                output = "  X  "
            else:
                output = "  O  "
            line += "|" + output
        printLine(width)
        print(line + "|")
        line = ""

    printLine(width)
    print("\n")

#Main game loop
while(True):
    player1Turn = drop(player1Turn, width, height, field)
    printField(width, height)
