import sys
import doctest

def num_ways(steps, strides):
    """
    returns the number of ways you can climb a set of stairs using different strides
    Parameters:
        steps (int): number of steps in the stairs
        strides (tuple): different strides you can take to climb the stairs. A stride represents how many steps you can jump at once.

        >>> num_ways(0, (1,2))
        1
        >>> num_ways(1, (1,2))
        1
        >>> num_ways(2, (1,2))
        2
        >>> num_ways(3, (1,2,3))
        4
        >>> num_ways(4, (1,2))
        5
        >>> num_ways(7, (1, 2, 6))
        23
    """
    if steps == 0:
        return 1

    total = 0
    for option in strides:
        if (option <= steps):
            total += num_ways(steps - option, strides)
    return total
    
def print_num_ways(steps, strides):
    print('num_ways({0}, {1}) = {2}'.format(steps, strides, num_ways(steps, strides)))

def main():
    doctest.testmod()

if __name__ == "__main__":
    main()

