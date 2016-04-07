import random

# todo
# choice stack
# random path through level

# class Cell ():
#     __init__(self, *kwargs):
#         #stuff
#         # set coords
#         # set visited
#         self.coords = kwargs.coords
#         self.visited = kwargs.visited

#     __str__():
#         return "Cell, coords: {}, visited: {}".format( coords, visited )



level = []

for y in range(3):

    levelx = []
    
    for x in range(3):

        cell = {}
        cell['coords'] = [x, y]
        cell['visited'] = 'false'
        #cell = [x,y]
        levelx.append(cell)
        
    
    level.append( levelx )
    print(level[y])


