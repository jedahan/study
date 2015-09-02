# speed: O(n n log(n))
# memory: n
def unique(string):
    sorted_string = sorted([c for c in string]) # n log n
    for i in range(len(string)): # n
        if sorted_string[i-1]==sorted_string[i]:
            return False
    return True

assert(unique("world")==True)
assert(unique("hello world")==False)

# speed: O(n)
# memory: 57 bytes
def unique(string):
    alpha = range(ord("A"),ord("z"))
    for character in string:
        index = ord(character)-65
        if index<0 or index > len(alpha)-1: next
        if alpha[index] == None: return False
        alpha[index] = None
    return True

assert(unique("world")==True)
assert(unique("hello world")==False)
