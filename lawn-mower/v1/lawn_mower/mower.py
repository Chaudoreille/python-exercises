class Mower():
    """An auto-mower for square surfaces.

        The mower can be programmed to go throughout the whole surface. Mower's position is
        represented by coordinates (X,Y) and a characters indicate the orientation according to cardinal notations
        (N,E,W,S).

        The lawn is divided in grid to simplify navigation.
        For example, the position can be 0,0,N, meaning the mower is in the lower left of the lawn, and oriented to
        the north.

        To control the mower, we send a simple sequence of characters. Possible characters are
        L,R,F. L and R turn the mower at 90° on the left or right without moving the mower. F means the mower
        move forward from one space in the direction in which it faces and without changing the orientation.

        If the position after moving is outside the lawn, mower keep it's position. Retains its orientation and go to
        the next command.
        We assume the position directly to the north of (X,Y) is (X,Y+1).

        Class Attributes:
            - cardinals: a tuple containing all cardinal points in clockwise order

        Attributes:
            - grid: upper-right corner of grid
            - coordinates: [X,Y] current coordinates of the Mower
            - orientation: index of current oriention in the Mower.cardinals tuple
    """
    cardinals = ('N','E','S','W')

    def __init__(self, grid, coordinates):
        """Instantiates a Mower object.
        
            Args:
                grid: a 2 integer list representing the top-right corner of the lawn grid

                coordinates : [X,Y,O] list with:
                    X,Y: integers representing the starting point of the Mower in the grid
                    O: a character representing the starting orientation of the Mower
        """ 
        self.grid = grid
        self.coordinates = [coordinates[0], coordinates[1]]
        self.orientation = Mower.cardinals.index(coordinates[2])

    def __str__(self):
        """String representation for a Mower object.
        
            A Mower object's string representation uses the format 'X Y O' where:
                X and Y are the Mower's coordinates
                O is the Mower's orientation 
        """
        return f'{self.coordinates[0]} {self.coordinates[1]} {Mower.cardinals[self.orientation]}'

    def execute(self, directions):
        """executes a set of directions on the lawn mower.

            Args:
                directions: a string of instructions where every character is one of 3 instructions : L, R or F
                    standing respectively for Left, Right and Forward

            Returns:
                self
        """
        movements = {
            'N' : lambda mower: [mower.coordinates[0], mower.coordinates[1] + 1 if mower.coordinates[1] + 1 <= mower.grid[1] else mower.grid[1]],
            'S' : lambda mower: [mower.coordinates[0], mower.coordinates[1] - 1 if mower.coordinates[1] - 1 >= 0 else 0],
            'E' : lambda mower: [mower.coordinates[0] + 1 if mower.coordinates[0] + 1 <= mower.grid[0] else mower.grid[0], mower.coordinates[1]],
            'W' : lambda mower: [mower.coordinates[0] - 1 if mower.coordinates[0] - 1 >= 0 else 0, mower.coordinates[1]]
        }

        for instruction in directions:
            if (instruction == 'L'):
                self.orientation = (self.orientation - 1) % 4
            elif instruction == 'R':
                self.orientation = (self.orientation + 1) % 4
            elif instruction == 'F':
                self.coordinates = movements[Mower.cardinals[self.orientation]](self)
            else:
                pass

        return self
