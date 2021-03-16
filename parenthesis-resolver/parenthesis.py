def parenthesis_match(str):
    opened_parenthesis = 0

    for character in str:
        if character == '(':
            opened_parenthesis += 1
        elif character == ')':
            opened_parenthesis -= 1

            if opened_parenthesis < 0:
                return False
    if opened_parenthesis == 0:
        return True
    return False

def longest_parenthesis(str):
    parenthesis_start = []
    longest = 0

    for index,character in enumerate(str):
        if character == '(':
            parenthesis_start.append(index)
        elif character == ')':
            if not parenthesis_start:
                return 0
            start = parenthesis_start.pop()
            longest = max(longest, index-start+1)
    if parenthesis_start:
        return 0
    return longest



