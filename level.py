import random
from cell import Cell
# todo
# choice stack
# random path through level

level = []

# Basic level with array of indexs at each index of the list representing coordinates
for y in range(3):

    levelx = []
    for x in range(3):
        levelx.append([x, y])
    level.append( levelx )
    print(level[y])

#print("cell list is: {}".format(cell_x_list))
#print("first cell is {}".format(level[0][0]))

# for y in level:
#     print('y = {}'.format(y))
#     print('level[y] = {}'.format(level[y]))

    #cell_list=[Cell( coord=[x, y], visited="true") for x,y in level ]
    #for cell in cell_list:
    #   levelx.append(cell)
    #cell_list[0].coord