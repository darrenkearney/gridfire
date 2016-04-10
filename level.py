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

print(level[1][1]   )
print('This is the cell coordinates from the cell at 1,1')
print("Level Cell: {}".format(level[1][1]))



# micheal tip 
# for index, item in enumerate([3,4,5]):

outer_array = []
for y in range(3):
     #print(y)
     #print(outer_array)
     inner_array = []
     for x in range(3):
             #print(x)
             #print(inner_array)
             cell = Cell(x=x, y=y)
             #obj = {'coord': [x, y]}
             #inner_array.append([]) #append empty array, this will be how we select the object
             inner_array.append(cell)
     outer_array.append(inner_array)
     print(outer_array)

print('Cell 0,0')
print( outer_array[0][1].x )

print( "Cell['coord'] = {}".format(outer_array[0][0].coord) )
# test =  outer_array[0][0] 
# for _ in test:
#     item.coord
# print('This is the cell coordinates from the cell at 1,1')
# print("Cell: {}".format(outer_array[1][1]))