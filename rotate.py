import math

arr = ["a","b","c","d","e","f","g","h","i"]
rot = ["g","d","a","h","e","b","i","f","c"]

i -> int(n/i) + n*(i%n)

def rotate(arr):
    rot = arr[:]
    n = int(math.sqrt(len(arr)))-1
    for y in range(0,n+1):
        for x in range(0,n+1):
            old_index = (n+1) * y + x
            new_index = (n - y) + x * (n+1)
            rot[new_index] = arr[old_index]

    return rot

assert(rotate(arr)==rot)

def rotate(arr):
    old_i = 1
    n = math.sqrt(len(arr))-1

    for count in range(len(arr)-1):
        x = 
        new_i = int(n/old_i) + n*(old_i%n))
        arr[new_i] = arr[old_i]
        old_i = new_i

print(arr)
rotate(arr)
print(arr)
