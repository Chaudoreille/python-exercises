import sys
from lawn_mower import InputFileLexer
from lawn_mower import Mower
from lawn_mower import error 

def main():
    if len(sys.argv) != 2:
        error("you need to provide the lawn mower input file")
    else:
        file_path = str(sys.argv[1])
        lexer = InputFileLexer()
        grid = [0, 0]

        for tokens in lexer.generateTokens(file_path):
            if tokens[0] == 'grid':
                grid = tokens[1]
            elif tokens[0] == 'mower':
                mower = Mower(grid, tokens[1])
            else:
                print(mower.execute(tokens[1]))

if __name__ == '__main__':
    main()