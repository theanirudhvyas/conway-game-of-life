import random
import os
import math
import time

class board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for x in range(width)] for y in range(height)]
        self.neighbours = [[0 for x in range(width)] for y in range(height)]

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_board(self):
        return self.cells

    def print_board(self):
        for x in range(self.height):
            print "\n"
            for y in range(self.width):
                if self.cells[x][y] == 0:
                    print '.',
                else :
                    print 'O',


    def rand_init(self, instances):
        for r in range(instances):
            x = random.randint(0,self.height-1)
            y = random.randint(0,self.width-1)
            self.cells[x][y] = 1


    def calculate(self, x, y):
        if(x == 0 and y == 0):
            return (self.cells[x][y+1] + self.cells[x+1][y+1] + self.cells[x+1][y])
        elif(x == 0 and y < self.width-1):
            return (self.cells[x][y-1] + self.cells[x][y+1] + self.cells[x+1][y-1] + self.cells[x+1][y] + self.cells[x+1][y+1])
        elif(y==0 and x < self.height-1):
            return (self.cells[x-1][y] + self.cells[x+1][y] + self.cells[x-1][y+1] + self.cells[x][y+1] + self.cells[x+1][y+1])
        elif(x==self.height-1 and y == self.width-1):
            return (self.cells[x][y-1] + self.cells[x-1][y-1] + self.cells[x-1][y])
        elif(x==self.height-1):
            return (self.cells[x][y-1] + self.cells[x][y+1] + self.cells[x-1][y-1] + self.cells[x-1][y] + self.cells[x-1][y+1])
        elif(y==self.width-1):
            return (self.cells[x-1][y] + self.cells[x+1][y] + self.cells[x-1][y-1] + self.cells[x][y-1] + self.cells[x+1][y-1])
        else:
            return (self.cells[x-1][y-1] + self.cells[x-1][y] + self.cells[x-1][y+1] + self.cells[x][y-1] + self.cells[x][y+1] + self.cells[x+1][y-1] + self.cells[x+1][y] + self.cells[x+1][y+1])


    def print_mat(self, mat):
        for x in range(self.height):
            print "\n"
            for y in range(self.width):
                print mat[x][y],


    def cal_neighbors(self):

        for x in range(self.height):
            for y in range(self.width):
                self.neighbours[x][y] = self.calculate(x,y)
            #elf.print_mat(neighbours)


    def update(self):

        self.cal_neighbors()

        for x in range(self.height):
            for y in range(self.width):
                if self.cells[x][y] == 1:
                    if not(self.neighbours[x][y]>1 and self.neighbours[x][y] < 4):
                        self.cells[x][y] = 0
                else:
                    if self.neighbours[x][y] == 3:
                        self.cells[x][y] = 1

        os.system('clear')
        self.print_board()

    def init_pulsar(self):
        x = int(math.floor(self.height/4))
        y = int(math.floor(self.width/4))

        self.cells[x][y+1] = 1
        self.cells[x][y+2] = 1
        self.cells[x+1][y] = 1
        self.cells[x+1][y+1] = 1
        self.cells[x+2][y+1] = 1

    def init_blinker(self):
        x = int(math.floor(self.height/4))
        y = int(math.floor(self.width/4))

        self.cells[x][y] = 1
        self.cells[x][y+1] = 1
        self.cells[x][y+2] = 1



if __name__ == "__main__":
    mat = board(20,20)
    #mat.rand_init(3)
    mat.init_pulsar()
    mat.print_board()


    while 1:
        mat.update()
        time.sleep(1)
