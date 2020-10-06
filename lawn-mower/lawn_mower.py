import sys
import fileinput

class MowerScriptSyntaxError(Exception):
    def __init__(self, filename, line, offset, error = ""):
        self.filename = filename
        self.line = line
        self.offset = offset
        self.message = error
        super().__init__(self.message)

    def __str__(self):
        pass

class LawnMowerInputFileParser():
    """Parses a Lawn Mower input file.
    
        To program the mower, the input file must be constructed as follows:

        The first line corresponds to the coordinate of the upper right corner of the lawn. the bottom left corner is
        assumed as (0,0).

        The rest of the file can control multiple mowers deployed on the lawn. Each mower has 2 next lines:

        The first line gives mower's starting position and orientation as "X Y O". X and Y being the
        position and O the orientation (one of [N,W,S,E] corresponding to cardinal points).

        The second line gives instructions to the mower to go throughout the lawn. Instructions are
        characters without spaces. Characters must be one of [L, R, F] (Left, Right, Forward)
    """

    def __init__(self, filename):
        """insantiates a Parser object.
        
        Args:
            filename : a Lawn Mower input file name (useful to raise Syntax Errors).
        """
        self.filename = filename

    def parse(self, line_number, line):
        """Checks the syntax for a given line and returns an array of values
        
            Args:
                line_number: an integer indicating the line number in the given file

                line: The actual line as read in the file

            Returns:
                an array of pertinent values for each line:
                    0 : [X,Y] with X,Y 2 integers representing the top right corner of the lawn grid
                    odd lines: [X,Y,O] with:
                        X,Y: 2 integers representing the initial position of the lawn mower in the grid
                        O : a character from (N,E,W,S) representing the initial orientation of the lawn mower
                    even lines: [A,B,C,...,N] a set of commands for the lawn mower
                        each entry is a character from (L,R,F) standing respectively for Left, Right and Forward

            Raises:
                MowerScriptSyntaxError: if there is a syntax error in the input file
        """
        if line_number == 0:
            # if len(grid) != 2:
            #     offset = 0 if len(grid) < 2 else 2
            #     raise MowerScriptSyntaxError(filename, line_number, offset)
            return line.split()
        elif line_number % 2 == 1:
            # if len(coordinates) != 3:
            #     offset = len(coordinates) * 2 if len(coordinates) < 3 else 3
            #     raise MowerScriptSyntaxError(filename, line_number, offset, '')
            return line.split()
        else:
            return line

class LawnMower():
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
            cardinals: a tuple containing all cardinal points in clockwise order

        Attributes:
            grid: upper-right corner of grid

            coordinates: [X,Y] current coordinates of the LawnMower

            orientation: index of current oriention in the LawnMower.cardinals tuple
    """
    cardinals = ('N','E','S','W')

    def __init__(self, grid, coordinates):
        """Instantiates a LawnMower object.
        
            Args:
                grid: a 2 integer list representing the top-right corner of the lawn grid

                coordinates : [X,Y,O] list with:
                    X,Y: integers representing the starting point of the LawnMower in the grid
                    O: a character representing the starting orientation of the LawnMower
        """ 
        self.grid = [int(grid[0]), int(grid[1])]
        self.coordinates = [int(coordinates[0]), int(coordinates[1])]
        self.orientation = LawnMower.cardinals.index(coordinates[2])

    def __str__(self):
        """String representation for a LawnMower object.
        
            A LawnMower object's string representation uses the format 'X Y O' where:
                X and Y are the LawnMower's coordinates
                O is the LawnMower's orientation 
        """
        return f'{self.coordinates[0]} {self.coordinates[1]} {LawnMower.cardinals[self.orientation]}'

    def mow(self, directions):
        """executes a set of directions on the lawn mower.

            Args:
                directions: a string of instructions where every character is one of 3 instructions : L, R or F
                    standing respectively for Left, Right and Forward

            Returns:
                self
        """
        movements = {
            'N' : lambda x: [x.coordinates[0], x.coordinates[1] + 1 if x.coordinates[1] + 1 <= x.grid[1] else x.grid[1]],
            'S' : lambda x: [x.coordinates[0], x.coordinates[1] - 1 if x.coordinates[1] - 1 >= 0 else 0],
            'E' : lambda x: [x.coordinates[0] + 1 if x.coordinates[0] + 1 <= x.grid[0] else x.grid[0], x.coordinates[1]],
            'W' : lambda x: [x.coordinates[0] - 1 if x.coordinates[0] - 1 >= 0 else 0, x.coordinates[1]]
        }

        for instruction in directions:
            if (instruction == 'L'):
                self.orientation = (self.orientation - 1) % 4
            elif instruction == 'R':
                self.orientation = (self.orientation + 1) % 4
            elif instruction == 'F':
                self.coordinates = movements[LawnMower.cardinals[self.orientation]](self)
            else:
                pass

        return self

def usage(msg):
    print(msg)
    

def main():
    if len(sys.argv) != 2:
        usage("you need to provide the lawn mower input file")
    else:
        filename = str(sys.argv[1])
        try:
            with open(filename, "r") as file_object:
                grid = [0,0]
                parser = LawnMowerInputFileParser(filename)
                mower = None

                for line_number, line in enumerate(file_object):
                    if line_number == 0:
                        grid = parser.parse(line_number, line)
                    elif line_number % 2 == 1:
                        coordinates = parser.parse(line_number, line)
                        mower = LawnMower(grid, coordinates)
                    else:
                        path = parser.parse(line_number, line)
                        print(mower.mow(path))
        except IOError:
            usage("file doesn't exist, please provide the path to an existing instructions file as input for the lawn mower")


if __name__ == '__main__':
    main()