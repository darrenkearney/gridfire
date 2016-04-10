import random
from cell import Cell
# todo
# choice stack
# random path through grid


# 2 dimensional array of indexs
# Inner and outer arrays represent x-axis and y-axis respectively
# At each x index is an instance of Cell
grid = []
for y in range(3):
    grid_x = []
    for x in range(3):
        cell = Cell(x=x, y=y)
        grid_x.append(cell)
    grid.append( grid_x )
    #print(grid[y])

# DEBUG
# print( 'The grid')
# print( grid )
# print( 'Cell 0,0' )
# print( grid[0][0] )
# print( "grid Cell x: {}".format(grid[0][0].x))
# print( "grid Cell y: {}".format(grid[0][0].y))
# print( "grid[0][0].coord = {}".format(grid[0][0].coord) )
