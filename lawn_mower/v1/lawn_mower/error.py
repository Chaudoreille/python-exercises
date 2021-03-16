import sys

def error(*args, **kwargs):
    """ prints an error message to stderr """
    print(*args, file=sys.stderr, **kwargs)