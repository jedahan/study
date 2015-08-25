import random
import math

a = [random.randint(1,100) for i in range(16) ]
print(a)

def insertion_sort(l):
    for j in range(0,len(l)):
        key=l[j]
        i=j-1
        while i >= 0 and l[i] > key:
            l[i+1] = l[i]
            i = i - 1
        l[i+1] = key
    return l

def merge_sort(a):
    if len(a) == 1: return a
    mid = len(a)/2
    return merge(merge_sort(a[:mid]),merge_sort(a[mid:]))

def merge(l, r):
    m = []
    while len(l) > 0 and len(r) > 0:
        if l[0]<r[0]:
            m.append(l.pop(0))
        else:
            m.append(r.pop(0))
    m.extend(l)
    m.extend(r)
    return m

print(merge_sort(a))

b = merge_sort(a)

def binary(a, needle):
    if len(a)==0 or needle < a[0] or needle > a[len(a)-1]: return -1
    mid = len(a)/2
    if a[mid] > needle: return binary(a[:mid], needle)
    if a[mid] < needle: return mid + binary(a[mid:], needle)
    return mid

index = random.randint(0,len(b))
needle = b[index]

print(index, needle)
found = binary(b, needle)
print(found,b[found])

notfound = binary(b, 101)
print(notfound)
