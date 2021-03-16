import sys
import re

# @todo: create a better usage function 
def error(*args, **kwargs):
    """ prints an error message to stderr """
    print(*args, file=sys.stderr, **kwargs)

class MowerSyntaxError(Exception):
    def __init__(self, message="Syntax error"):
        self.message = message
        super().__init__(self.message)

forward = {
    # north : y += 1
    'N': lambda pos,grid: {
        'x': pos['x'],
        'y': pos['y'] + 1 if pos['y'] < grid['y'] else pos['y'],
        'o': pos['o']
    },
    # south : y -= 1
    'E': lambda pos,grid: {
        'x': pos['x'] + 1 if pos['x'] < grid['x'] else pos['x'],
        'y': pos['y'],
        'o': pos['o']
    },
    # east  : x += 1 
    'S': lambda pos,grid: {
        'x': pos['x'],
        'y': pos['y'] - 1 if pos['y'] > 0 else pos['y'],
        'o': pos['o']
    },
    # west  : x -= 1 
    'W': lambda pos,grid: {
        'x': pos['x'] - 1 if pos['x'] > 0 else pos['x'],
        'y': pos['y'],
        'o': pos['o']
    },
}

orientations = ('N','E','S','W')
move = {
    # using modulo on indexes allows to cycle on the tuple instead of overflowing
    # go left in the orientations list when rotating the mower counter-clockwise
    'L': lambda pos,grid: {
        'x': pos['x'],
        'y': pos['y'],
        'o': (pos['o'] - 1) % 4
    },
    # go right when rotating the mower clockwise
    'R': lambda pos,grid: {
        'x': pos['x'],
        'y': pos['y'],
        'o': (pos['o'] + 1) % 4
    },
    'F': lambda pos,grid: forward[orientations[pos['o']]](pos, grid),
}


def mow(lawn, mower_initial_position, instructions):
    grid = {
        'x': int(lawn[0]),
        'y': int(lawn[1])
    }
    # position['o'] stores the index of the orientation letter in the {orientations} tuple
    position = {
        'x': int(mower_initial_position[0]),
        'y': int(mower_initial_position[1]),
        'o': orientations.index(mower_initial_position[2]),
    }

    for step in instructions:
        position = move[step](position, grid)

    return '{0} {1} {2}'.format(position['x'], position['y'], orientations[position['o']])

def get_lawn_dimensions(line):
    if (not line):
        return
    if re.match(r'^ *\d+ +\d+ *$', line):
        return line.strip().split()
    else:
        raise MowerSyntaxError()

def get_mower_starting_position(line):
    if not line:
        raise(MowerSyntaxError(message='unexpected end of file: missing mower starting position'))
    if re.match(r'^ *\d+ +\d+ +[NEWS] *$', line):
        return line.strip().split()
    else:
        raise MowerSyntaxError()

def get_instruction_set(line):
    if not line:
        raise(MowerSyntaxError('unexpected end of file: missing mowing instructions'))
    if re.match(r'^ *[LRF]+ *$', line):
        return list(line.strip())
    else:
        raise MowerSyntaxError()

def get_mowing_parameters(file):
    line_number = 1

    while line_number > 0:
        lawn_line = file.readline()
        mower_line = file.readline()
        instructions_line = file.readline()

        if (not lawn_line):
            return
        try:
            lawn = get_lawn_dimensions(lawn_line)
            line_number += 1
            mower = get_mower_starting_position(mower_line)
            line_number += 1
            instructions = get_instruction_set(instructions_line)
            line_number += 1
        except MowerSyntaxError as exception:
            # @todo: proper error message
            error(f'{exception.message} on line {line_number}')
            return

        yield (lawn, mower, instructions)


## faire un double yield (un qui triple read puis yield les 3 tokens, puis une qui yield le retour de mow)
def mower_generator(filepath):
    try:
        with open(filepath) as file:
            for mowing_parameters in get_mowing_parameters(file):
                yield mow(*mowing_parameters)
  
    except IOError:
        print("file not found")

    return None

def main():
    if len(sys.argv) != 2:
        error('you need to provide an input file')
    else:
        filepath = sys.argv[1]
        for line in mower_generator(filepath):
            print(line)

if __name__ == '__main__':
    main()