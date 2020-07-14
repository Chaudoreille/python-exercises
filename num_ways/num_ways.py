import sys

def num_ways(steps, strides):
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
    print_num_ways(0, (1,2))
    print_num_ways(1, (1,2))
    print_num_ways(2, (1,2))
    print_num_ways(3, (1,2))
    print_num_ways(3, (1,2,3))
    print_num_ways(4, (1,2))

if __name__ == "__main__":
    main()

