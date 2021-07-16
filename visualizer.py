import pygame
from pygame.locals import *
from queue import PriorityQueue

pygame.init()

#colours
red=(255,0,0) #Path Colour
yellow=(255,255,0) #Closed cells colour
orange=(255,165,0) #Open cells colour
black=(0,0,0) #Walls
white=(255,255,255) #Screen Colour
grey=(128,128,128) #Demarcations of rows and columns
green=(255,0,255) #Start Cell colour
blue=(0,0,128) #End cell Colour



#Screen Vars
height=700
width=700
rows=50
cell_dimension=height//rows
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Path Finding Visualizer')


class Cell:#The node/state class
    def __init__(self, row, col):
        self.row=row
        self.x=row*cell_dimension
        self.col=col
        self.y=col*cell_dimension
        self.colour=white
        self.adjacencyList=[]#Adjacent cells

    def build(self):
        pygame.draw.rect(screen,self.colour,(self.x,self.y,cell_dimension,cell_dimension))


    def adjacencyListBuild(self,matrix):
        #just lower
        if self.row+1<rows:
            if not matrix[self.row+1][self.col].colour==black:
                self.adjacencyList.append(matrix[self.row+1][self.col])
        #just right
        if self.col+1<rows:
            if not matrix[self.row][self.col+1].colour==black:
                self.adjacencyList.append(matrix[self.row][self.col+1])
        #just upper
        if self.row>0:
            if not matrix[self.row-1][self.col].colour==black:
                self.adjacencyList.append(matrix[self.row-1][self.col])
        #just left
        if self.col>0:
            if not matrix[self.row][self.col-1].colour==black:
                self.adjacencyList.append(matrix[self.row][self.col-1])


def h_value(pos1,pos2):# f(n)=g(n)+h(n), here h(n) is the manhattan distance. Its a heuristic approach
    x1,y1=pos1
    x2,y2=pos2

    return abs(x2-x1)+abs(y2-y1)

#Main Function
game=True # Primary variable

start=None
end=None

#Building the matrix
matrix=[]
for row in range(rows):
    matrix.append([])
    for col in range(rows):
        state=Cell(row,col)
        matrix[row].append(state)

while game:
    #main screen
    screen.fill(white)

    #Building the cells
    for row in matrix:
        for state in row:
            state.build() #Cell can also be called state



    #Drawing_the_grid
    for row in range(rows):
        x=row*cell_dimension
        pygame.draw.line(screen,grey,(0,x),(height,x))
    for col in range(rows):
        x=col*cell_dimension
        pygame.draw.line(screen,grey,(x, 0),(x,width))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:#For quitting
            game=False

        if pygame.mouse.get_pressed()[0]:#Left Mouse Button
            mouse_pos=pygame.mouse.get_pos()
            i,j=mouse_pos
            row=i//cell_dimension
            col=j//cell_dimension
            cell=matrix[row][col]
            if start==None and cell!=end:
                cell.colour=green#Making cell as starting cell
                start=cell
            if end==None and cell!=start:
                cell.colour=blue#Making cell as ending cell
                end=cell
            if not (cell==start or cell==end):
                cell.colour=black#Walls

        if pygame.mouse.get_pressed()[2]:#Right Mouse Button, used for resetting any cell
            mouse_pos=pygame.mouse.get_pos()
            i,j=mouse_pos
            row=i//cell_dimension
            col=j//cell_dimension
            cell=matrix[row][col]
            cell.colour=white
            if cell==start:
                start=None
            if cell==end:
                end=None

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:#Used for running the algorithm
                if start and end:
                    for row in matrix:
                        for cell in row:
                            cell.adjacencyListBuild(matrix)
                            #print(cell.adjacencyList)
                    #A-Star Algorithm
                    g_value={}# g(n) in f(n)=g(n)+h(n)
                    for row in matrix:
                        for spot in row:
                            g_value[spot]=float("inf")

                    g_value[start]=0
                    f_value={}# f(n) in f(n)=g(n)+h(n)
                    for row in matrix:
                        for spot in row:
                            f_value[spot]=float("inf")
                    f_value[start]=h_value((start.row,start.col),(end.row,end.col))
                    timer=0
                    open_cells_pq=PriorityQueue()
                    open_cells_hs={start}
                    parent={}
                    open_cells_pq.put((0,timer,start))

                    while not open_cells_pq.empty():
                        for event in pygame.event.get():
                            if event.type==pygame.QUIT:
                                pygame.quit()

                        cur_cell=open_cells_pq.get()[2]
                        open_cells_hs.remove(cur_cell)

                        if cur_cell==end:
                            #Retracing the path
                            while cur_cell in parent:
                                cur_cell=parent[cur_cell]
                                cur_cell.colour=red

                                screen.fill(white)

                                for row in matrix:
                                    for state in row:
                                        state.build()

                                for row in range(rows):
                                    x=row*cell_dimension
                                    pygame.draw.line(screen,grey,(0,x),(height,x))
                                for col in range(rows):
                                    x=col*cell_dimension
                                    pygame.draw.line(screen,grey,(x, 0),(x,width))
                                pygame.display.update()

                            end.colour=blue
                            start.colour=green
                            break

                        for state in cur_cell.adjacencyList:
                            tmp_g_value_state=g_value[cur_cell]+1
                            if g_value[state]>tmp_g_value_state:
                                g_value[state]=tmp_g_value_state
                                f_value[state]=g_value[state]+h_value((state.row,state.col),(end.row,end.col))
                                parent[state]=cur_cell
                                if state not in open_cells_hs:
                                    timer=timer+1
                                    open_cells_pq.put((f_value[state],timer,state))
                                    open_cells_hs.add(state)
                                    state.colour=orange #Cell in open state

                        screen.fill(white)
                        for row in matrix:
                            for state in row:
                                state.build() #Cell can also be called state
                        for row in range(rows):
                            x=row*cell_dimension
                            pygame.draw.line(screen,grey,(0,x),(height,x))
                        for col in range(rows):
                            x=col*cell_dimension
                            pygame.draw.line(screen,grey,(x, 0),(x,width))
                        pygame.display.update()

                        if cur_cell!=start:
                            cur_cell.colour=yellow #Cell closed

            if event.key==pygame.K_ESCAPE: #resetting the whole matrix
                start=None
                end=None
                #Building the new matrix
                matrix=[]
                for row in range(rows):
                    matrix.append([])
                    for col in range(rows):
                        state=Cell(row,col)
                        matrix[row].append(state)



pygame.quit()
