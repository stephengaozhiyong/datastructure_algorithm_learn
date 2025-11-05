from turtle import *

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        colsInMaze = 0
        self.mazeList = []
        mazeFile = open(mazeFileName)
        for l in mazeFile:
            rowList = []
            col = 0
            for ch in l[:-1]:
                rowList.append(ch)
                if ch == "S":
                    self.startRow = rowsInMaze
                    self.startCol = col
                col += 1
            rowsInMaze += 1
            self.mazeList.append(rowList)
            colsInMaze = len(rowList)
        
        self.rowsInMaze = rowsInMaze
        self.colsInMaze = colsInMaze
        self.xTranslate = -colsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = Turtle(shape="turtle")
        setup(width=600, height=600)
        setworldcoordinates(-(colsInMaze-1)/2-.5,
                            -(rowsInMaze-1)/2-.5,
                            (colsInMaze-1)/2+.5,
                            (rowsInMaze-1)/2+.5)
    
    def drawMaze(self):
        for y in range(self.rowsInMaze):
            for x in range(self.colsInMaze):
                if self.mazeList[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,
                                         -y+self.yTranslate,
                                         'tan')
        self.t.color('black', 'blue')
    
    def drawCenteredBox(self, x, y, color):
        tracer(0)
        self.t.up()
        self.t.goto(x-.5, y-.5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        update()
        tracer(1)

    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,
                                        -y+self.yTranslate))
        self.t.goto(x+self.xTranslate, -y+self.yTranslate)

    def dropBreadcrumb(self, color):
        self.t.dot(color)

    def updatePosition(self, row, col, val=None):
        if val:
            self.mazeList[row][col] = val
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None
        
        if color:
            self.dropBreadcrumb(color)


    def isExit(self, row, col):
        return (row == 0 or
                row == self.rowsInMaze - 1 or
                col == 0 or
                col == self.colsInMaze-1)
    
    def __getitem__(self, idx):
        return self.mazeList[idx]


def searchFrom(maze: Maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)

    if maze[startRow][startColumn] == OBSTACLE:
        return False
    if maze[startRow][startColumn] == TRIED:
        return False
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)

    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found

if __name__ == '__main__':
    m = Maze("maze.txt")
    m.drawMaze()
    searchFrom(m, m.startRow, m.startCol)
    w = m.t.getscreen()
    w.exitonclick()