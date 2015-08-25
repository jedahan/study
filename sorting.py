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
