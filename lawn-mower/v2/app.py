import sys
import re

# @todo: create a better usage function 
def error(*args, **kwargs):
    """ prints an error message to stderr """
    print(*args, file=sys.stderr, **kwargs)

def mower_algorithm(grid, initial_position, instructions):
    orientations = ('N','E','S','W')
    forward = {
        'N': lambda pos,grid: {
            'x': pos['x'],
            'y': pos['y'] + 1 if pos['y'] < grid['y'] else pos['y'],
            'o': pos['o']
        },
        'E': lambda pos,grid: {
            'x': pos['x'] + 1 if pos['x'] < grid['x'] else pos['x'],
            'y': pos['y'],
            'o': pos['o']
        },
        'S': lambda pos,grid: {
            'x': pos['x'],
            'y': pos['y'] - 1 if pos['y'] > 0 else pos['y'],
            'o': pos['o']
        },
        'W': lambda pos,grid: {
            'x': pos['x'] - 1 if pos['x'] > 0 else pos['x'],
            'y': pos['y'],
            'o': pos['o']
        },
    }
    grid_size = {
        'x': int(grid[0]),
        'y': int(grid[1])
    }
    position = {
        'x': int(initial_position[0]),
        'y': int(initial_position[1]),
        'o': orientations.index(initial_position[2]),
    }

    for step in instructions:
        if (step == 'L'):
            position['o'] = (position['o'] - 1) % 4
        elif step == 'R':
            position['o'] = (position['o'] + 1) % 4
        else:
            position = forward[orientations[position['o']]](position, grid_size)

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

                        yield mower_algorithm(grid, initial_position, instructions)
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