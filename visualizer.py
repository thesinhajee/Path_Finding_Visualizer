import pygame
from pygame.locals import *
from queue import PriorityQueue


pygame.init()


#colours
red=(255,0,0)
yellow=(255,255,0)
black=(0,0,0)
white=(255,255,255)
grey=(128,128,128)
green=(0,128,0)
blue=(0,0,128)
orange=(255,165,0)


#Screen Vars
height=700
width=700
rows=60
cell_dimension=height//rows
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Path Finding Visualizer')


class Cell:
    def __init__(self, row, col):
        self.row=row
        self.x=row*cell_dimension
        self.col=col
        self.y=col*cell_dimension
        self.colour=white
        self.adjacencyList=[]

    def build(self):
        pygame.draw.rect(screen,self.colour,(self.x,self.y,cell_dimension,cell_dimension))
#Main Function
game=True # Primary variable

start=None
end=None

#Building the grid
matrix=[]
for row in range(rows):
    matrix.append([])
    for col in range(rows):
        state=Cell(row,col)
        matrix[row].append(state)

while game:

    #main screen
    screen.fill(white)

    for row in matrix:
        for state in row:
            state.build()

    #Drawing_the_grid
    for row in range(rows):
        x=row*cell_dimension
        pygame.draw.line(screen,grey,(0,x),(height,x))
    for col in range(rows):
        x=col*cell_dimension
        pygame.draw.line(screen,grey,(x, 0),(x,width))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False


pygame.quit()
