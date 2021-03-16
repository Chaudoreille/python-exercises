def parentheses_match(str):
    opened_parentheses = 0

    for character in str:
        if character == '(':
            opened_parentheses += 1
        elif character == ')':
            opened_parentheses -= 1

            if opened_parentheses < 0:
                return False
    if opened_parentheses == 0:
        return True
    return False

def longest_parenthesis(str):
    parentheses_start = []
    longest = 0

    for index,character in enumerate(str):
        if character == '(':
            parentheses_start.append(index)
        elif character == ')':
            if not parentheses_start:
                return 0
            start = parentheses_start.pop()
            longest = max(longest, index-start+1)
    if parentheses_start:
        return 0
    return longest



