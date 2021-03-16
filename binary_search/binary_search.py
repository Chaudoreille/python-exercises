def bin_search(haystack, needle, start, end):
    if start >= end:
        return False

    middle = int((start+end)/2)
    if haystack[middle] == needle:
        return True
    else:
        return bin_search(haystack, needle, start, middle) or bin_search(haystack, needle, middle + 1, end)

def binary_search(haystack, needle):
    return bin_search(haystack, needle, 0, len(haystack))
