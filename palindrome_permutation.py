def palindrome_permutation(s):
    s = sorted(''.join(s.split()))
    odd = bool(len(s)%2)
    i = 0
    while i < len(s)-1:
        if s[i] != s[i+1]:
            if odd:
                odd = False
            else:
                return False
        i = i + 2
    return True

assert(palindrome_permutation("taco cat")==True)
assert(palindrome_permutation("t a con cat")==False)

hi = list()
for i in range(10):
    hi.append(i)
print(hi)
print(hi == [0,1,2,3,4,5,6,7,8,9])
print(hi.pop())

def palindrome_permutation(s):
    s = ''.join(s.split())
    odd = dict()
    for c in s:
        if odd.has_key(c):
            odd[c] = not odd[c]
        else:
            odd[c] = True
    for k in odd:
        if odd.get(k)%2 != 0:
            if odd:
                odd = False
            else:
                return False
    return True

assert(palindrome_permutation("taco cat")==True)
assert(palindrome_permutation("ta con cat")==False)
