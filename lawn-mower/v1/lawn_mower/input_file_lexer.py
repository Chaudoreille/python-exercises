import fileinput
from lawn_mower.error import error

class InputFileLexer():
    """ Lexes a Lawn Mower input file, using a generator that returns a list of tokens for each line of the file.
    
        To program the mower, the input file must be constructed as follows:

        The first line corresponds to the coordinate of the upper right corner of the lawn. the bottom left corner is
        assumed as (0,0).

        The rest of the file can control multiple mowers deployed on the lawn. Each mower has 2 next lines:

        The first line gives mower's starting position and orientation as "X Y O". X and Y being the
        position and O the orientation (one of [N,W,S,E] corresponding to cardinal points).

        The second line gives instructions to the mower to go throughout the lawn. Instructions are
        characters without spaces. Characters must be one of [L, R, F] (Left, Right, Forward)

        Attributes:
            - filePath : path to the input file
            - lineNumber : current line number
            - line : current line
            - tokenFunction : current lexing function

        Public methods:
            generateTokens() : returns a generator, each element being a tuple containing the token list type and the according token list
    """

    def __init__(self):
        """ instantiates an lexer for the lawn mower input file. """
        self.filePath = ''
        self.lineNumber = 0
        self.line = ''
        self.tokenFunction = '_gridTokens'

    def generateTokens(self, file_path):
        """
            this generator reads from an input file and returns tokens for each line

            Arguments:
                file_path: path of the lawn mower input file

            Return:
                a generator object where each element is a tuple containing (type, tokens) corresponding to:
                    type : the type of tokens returned ('grid'|'mower'|'instructions')
                    tokens : a list of tokens fit specific to each token type
        """
        self.filePath = file_path
        try:
            with open(self.filePath, "r") as file_object:
                for line_number, line in enumerate(file_object):
                    self.lineNumber = line_number
                    self.line = line
                    tokens = getattr(self, self.tokenFunction)()
                    yield tokens
                    self._switchState()
        except IOError:
            error(f'{file_path}: file doesn\'t exist')

        return False


    def _syntaxError(self, offset, message):
        """ generates a syntax error message on the stderr output """
        error(f'File "{self.filePath}", line {self.lineNumber}:')
        error(' ', self.line.strip())
        if (offset == 0):
            error('  ^')
        else:
            error(' ' * (offset + 1), '^')
        error(message)
        exit()

    def _splitWords(self, expected_word_count):
        """ 
            Splits the current line in a list of words (groups of characters separated by spaces)
        """
        words = self.line.split()
        word_count = len(words)
        error_message = f'Syntax Error: expecting {expected_word_count} entries, {word_count} provided'

        if word_count < expected_word_count:
            self._syntaxError(self._offset(word_count - 1), error_message)
        elif word_count > expected_word_count:
            self._syntaxError(self._offset(expected_word_count), error_message)

        return words

    def _offset(self, nth_word):
        """ returns the character offset of the first letter of a word in a given line 
        
            Arguments:
                nth_word: word index in the current line
        """
        word_count = 0

        for position, value in enumerate(self.line):
            if value != " " and position - 1 >= 0 and self.line[position - 1] == " ":
                word_count += 1
            if word_count == nth_word:
                return position
        return -1

    def _gridTokens(self):
        """ Lexer for the grid line (first line) in the input file 
        
            Returns a grid tuple, comprised of:
                the nature of the token list : 'grid'
                a list of tokens: [X,Y] representing the top-right coordinates of the lawn grid
        """
        tokens = []
        words = self._splitWords(2)

        for index, word in enumerate(words):
            try:
                tokens.append(int(word))
            except ValueError:
                self._syntaxError(self._offset(index), f'TypeError: {word} should be a number')
        return ('grid', tokens)

    def _initMowerTokens(self):
        """ Lexer for a lawn mower initialisation line (odd lines) in the input file 
        
            Returns a mower initialisation tuple, comprised of:
                the nature of the token list: 'mower'
                a list of tokens: [X,Y,O] representing:
                    X,Y -> initial position of the mower in the grid
                    O -> initial orientation of the mower in the grid (N|E|W|S)
        """
        tokens = []
        words = self._splitWords(3)
        
        for index, word in enumerate(words):
            if index == 2:
                if word in {'N', 'E', 'W', 'S'}:
                    tokens.append(words[2])
                else:
                    self._syntaxError(self._offset(3), f'ValueError: {word} should be cardinal point, one of ["N", "E", "W", "S"]')
            else:   
                try:
                    tokens.append(int(word))
                except ValueError:
                    self._syntaxError(self._offset(index), f'TypeError: {word} should be a number')

        return ('mower', tokens)

    def _mowerInstructionTokens(self):
        """ Lexer for a lawn mower instruction line (even lines) in the input file 
        
            Returns an instruction tuple, comprised of:
                the nature of the token list : 'instructions'
                a list of characters (L|R|F) representing each instruction for the mower
        """
        words = self._splitWords(1)
        tokens = list(words[0])

        for index, instruction in enumerate(tokens):
            if instruction not in {'L', 'R', 'F'}:
                self._syntaxError(index, f'ValueError: {words[0]} should be an instruction set. Accepted instrucions are ["L", "R", "F"]')

        return ('instructions', tokens)

    def _switchState(self):
        """ Switches the current lexing function based on the line number """
        if (self.lineNumber % 2 == 0):
            self.tokenFunction = '_initMowerTokens'
        else:
            self.tokenFunction = '_mowerInstructionTokens'
