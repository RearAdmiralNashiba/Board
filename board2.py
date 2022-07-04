import random

size = 10#int(input("What will be the size of our fair grid?"))

# board = []
# for i in range(size):
#     board.append([])
#     for j in range(size):
#         board[i].append(j)

active = []

class Piece():
    def __init__(self, loc):
        self.loc = loc
        self.alive = True
        self.m_action = True
        active.append(self)

    def __str__(self):
        return("A generic piece")

    def die(self):
        self.alive = False
        active.remove(self)
        print(f"{self} has died!")

    def move_check(self, space):
        occupied = [i.loc for i in active]
        return adj_check(self.loc, space) and edge_check(space) \
        and space not in occupied

    def refresh(self):
        self.m_action = True

    def move(self, target):
        if self.move_check(target):
            self.loc = target

def adj_check(p1, p2):
    return (abs(p1[0] - p2[0]) == 1) or (abs(p1[1] - p2[1]) == 1)

def edge_check(space):
    return (space[0] in range(0, size + 1)) and (space[1] in range(0, size))

def report(cat):
    print("The state of the board:")
    for i in cat:
        print(f"{i} at {i.loc}")

def next_turn():
    for i in active:
        i.refresh
    report(active)

a = Piece([0, 0])
b = Piece([0, 1])

next_turn()

for i in active:
    i.move()
