import random

dim = 8
board = []
pieces = []
dead_pieces = []
teams = ['Red', 'Blue', 'Green', 'Yellow', 'Pink', 'Teal, maybe']
terrain = ['Farmland', 'Grassland', 'Coastline', 'Dryland']
names = ["Wang", "Smith", "Devi", "Ivanov", "Kim"]
types = ["Rock Infantry", "Scissors Cavalry", "Paper Skirmisher"]
moves = {"a" : [-1, 0], "d" : [1, 0], "w" : [0, 1], "s" : [0, -1]}
# moves = {"Left" : [-1, 0], "Right" : [0, 1], "Up" : [0, 1], "Down" : [0, -1]}
# moves = {K_LEFT : [-1, 0], K_RIGHT : [0, 1], K_UP : [0, 1], K_DOWN : [0, -1]}
turn_count = 0

class Space:
    def __init__(self, loc, type):
        self.loc = loc
        self.type = type

    def __str__(self):
        return f"A space at coordinates {self.loc}, terrain type {self.type}."

class Piece:  
    def __init__(self, name, team, loc, type, live=1):
        self.live = live
        self.name = name
        self.team = team
        self.loc = loc
        self.type = type

    def __str__(self):
        return f"A {self.team} {self.type} named {self.name} {self.loc}"

    def die(self):
        self.live = 0
        print(f"{self} has died")

    def move(self, target):#Reworking targeting
        x_lims = self.loc[0] + moves[target][0]
        y_lims = self.loc[1] + moves[target][1]
        if space_occ([x_lims, y_lims]):
            if self.fight(space_occ([x_lims, y_lims])):
                self.loc = [x_lims, y_lims]
                print(f"{self} has moved to {self.loc}.")
        else:
            self.loc = [x_lims, y_lims]
            print(f"{self} has moved to {self.loc}.")

    def fight(self, target):#RPS version
        if self.type == target.type:
            print("The combatants tie \n")
            pass
        elif ((self.type == types[0]) and (target.type == types[1])) \
        or ((self.type == types[1]) and (target.type == types[2])) \
        or ((self.type == types[2]) and (target.type == types[0])):
            print(f"{self} has defeated {target} \n")
            target.die()
            return True
        else:
            print(f"{self} has been defeated by {target} \n")
            self.die()
            return False

def create_board():
    for i in range(dim):
        board.append([])
        for j in range(dim):
            board[i].append(Space((i, j), random.choice(terrain)))
    return board

def new_game():
    create_board()
    turn_count = 0
    print("\n - - - New Game - - - \n")
    new_turn()

def space_check():
    for i in board:
        for j in i:
            print(j)

def piece_check():
    for d in pieces:
        if not d.live:
            pieces.remove(d)
            dead_pieces.append(d)
    print("Pieces on the board: \n")
    for i in pieces:
        print ((i), f"occupying space {i.loc} \n")
    if len(dead_pieces) > 0:
        print("Dead pieces: \n")
        for i in dead_pieces:
            print(i)
    else:
        print("No dead pieces. \n")

def spawn_piece_rand():
    target = [random.randrange(dim), random.randrange(dim)]
    if len(pieces) <= 1:
        for i in pieces:
            if i.loc == target:
                print ("The target spawn point was already occupied")
    pieces.append(Piece(random.choice(names), target, random.choice(types)))

def spawn_piece(x, y, team, type):
    target = [x, y]
    if len(pieces) <= 1:
        for i in pieces:
            if i.loc == target:
                print ("The target spawn point was already occupied")
    pieces.append(Piece(random.choice(names), team, target, type))

def new_turn():
    global turn_count
    turn_count += 1
    # space_check()
    piece_check()
    print("Fresh turn \n")
    for i in pieces:
        if i.live:
            turn_prompt(i)

def turn_prompt(piece):
    action = input("1. Move 2. Attack > ")
    if action == "1":
        move = input("Direction > ")
        piece.move(move)
    elif action == "2":
        target = moves[input("Direction > ")]
        if space_occ(target):
            piece.fight(space_occ(target))
        else:
            print("Space was not occupied \n")
        # piece.fight(target)
    else:
        print("Invalid entry, probably")
        turn_prompt(piece)

def space_occ(space):
    for i in pieces:
        if i.loc == space:
            return i

new_game()
spawn_piece(0, 0, teams[0], types[0])
spawn_piece(1, 0, teams[1], types[1])

# for i in range(3):
#     new_turn()
