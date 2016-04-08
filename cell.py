class Cell ():
    def __init__(self, **kwargs):
        self.coord = kwargs.get('coord', [0,0])
        self.visited = kwargs.get('visited', 'false')
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__():
        return "Cell, coord: {}, visited: {}".format( coord, visited )