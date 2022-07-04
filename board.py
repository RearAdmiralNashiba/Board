import random

size = 10#int(input("What will be the size of our fair grid?"))

board = []
for i in range(size):
    board.append([])
    for j in range(size):
        board[i].append(j)

cards = ['w', 'a', 's', 'd']
rng_space = random.randrange(0, size)
enemies = []
items = []

class Piece():
    def __init__(self, x, y):
        self.location = [x, y]
        self.alive = True
        self.direction = random.choice(cards)

    def die(self):
        self.alive = False

    def move(self):
        self.path()
        if self.can_move():
            if self.direction == 'w':
                self.location[1] -= 1
            elif self.direction == 's':
                self.location[1] += 1
            elif self.direction == 'a':
                self.location[0] -= 1
            elif self.direction == 'd':
                self.location[0] += 1

    def can_move(self):
        return not ((self.direction == 'w' and self.location[1] == 0) or \
        (self.direction == 'a' and self.location[0] == 0) or \
        (self.direction == 's' and self.location[1] == size) or \
        (self.direction == 'd' and self.location[0] == size))

    # def turn(d):
    #     if not self.can_move():
    #         self.direction = d
    #         if not self.can_move():
    #             self.direction = random.choice(cards)

class Player(Piece):
    def __init__(self):
        self.inventory = []

    def path(self):
        self.direction = input("(Move) > ")

class Enemy(Piece):
    def kill_check(self):
        if self.location == Player.location:
            Player.die()

class Item(Piece):
    pass

class Key(Item):
    pass

class Shoe(Item):
    pass

class Blob(Enemy):
    def __str__(self):
        return "inscrutable blob, erratically plodding"

    def path(self):
        self.direction = random.choice(['w', 'a', 's', 'd'])

class Ball(Enemy):
    def __str__(self):
        return "loyal ball, steadliy oscillating"

    def path(self):
        if not self.can_move():
            if self.direction == 'w':
                self.direction = 's'
            elif self.direction == 'a':
                self.direction = 'd'
            elif self.direction == 's':
                self.direction = 'w'
            elif self.direction == 'd':
                self.direction = 'a'

class Walker(Enemy):
    def __str__(self):
        return "preoccupied walker, heedlessly lurching"

    def path(self):
        if not self.can_move():
            self.direction = random.choice(cards)

class Fireball(Enemy):
    def __str__(self):
        pass

    def path(self):
        self.turn()

def enemy_tick(e):
    for i in e:
        i.move()
        print(f"{i} is at {i.location()}")

a = Blob(0,0)
#a = Blob(rng_space, rng_space)
enemy_tick(enemies)
