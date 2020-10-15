import sys
import re

# @todo: create a better usage function 
def error(*args, **kwargs):
    """ prints an error message to stderr """
    print(*args, file=sys.stderr, **kwargs)

def mower(lawn, initial_position, instructions):
    orientations = ('N','E','S','W')
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
    grid = {
        'x': int(lawn[0]),
        'y': int(lawn[1])
    }
    position = {
        'x': int(initial_position[0]),
        'y': int(initial_position[1]),
        'o': orientations.index(initial_position[2]),
    }

    # position['o'] stores the index of the orientation letter in the orientations tuple
    # using modulo on indexes allows to cycle on the tuple instead of overflowing
    for step in instructions:
        if (step == 'L'):
            # go left in the orientations list when rotating the mower counter-clockwise
            position['o'] = (position['o'] - 1) % 4
        elif step == 'R':
            # go right when rotating the mower clockwise
            position['o'] = (position['o'] + 1) % 4
        else:
            position = forward[orientations[position['o']]](position, grid)

    return '{0} {1} {2}'.format(position['x'], position['y'], orientations[position['o']])

def mower_generator(filepath):
    grid = None
    initial_position = None
    instructions = None

    try:
        with open(filepath) as file:
            for line_number, line in enumerate(file):
                if line_number == 0:
                    if re.match(r'^\d+ +\d+$', line):
                        grid = line.strip().split()
                    else:
                        # @todo: proper error message
                        error(f'parsing error line {line_number}')
                        exit()
                elif line_number % 2 == 1:
                    if re.match(r'^\d+ +\d+ +[NEWS]$', line):
                        initial_position = line.strip().split()
                    else:
                        # @todo: proper error message
                        error(f'parsing error line {line_number}')
                        exit()
                else:
                    if re.match(r'^[LRF]+$', line):
                        instructions = list(line.strip())

                        yield mower(grid, initial_position, instructions)
                    else:
                        # @todo: proper error message
                        error(f'parsing error line {line_number}')
                        exit()
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