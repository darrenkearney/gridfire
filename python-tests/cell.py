class Cell ():
    """A Cell that contains cell specific data."""

    def __init__(self, **kwargs):
        self.x = kwargs.get( 'x', 0 )
        self.y = kwargs.get( 'y', 0 )
        self.coord = kwargs.get('coord', [ self.x, self.y ])
        self.visited = kwargs.get('visited', 'false')
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "Cell, coord: {}, visited: {}".format( self.coord, self.visited )