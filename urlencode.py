def urlencode(str, l):
    s = list(str)
    spaces = 0
    for i in range(l):
        if s[i]==" ":
            spaces = spaces + 1
    i = l-1

    while i > 0:
        print(''.join(s))
        ii = i+spaces*2
        i = i - 1
        if s[i]==" ":
            s[ii-2:ii] = list('%20')
            i = i - 2
            spaces = spaces - 1
        else:
            s[ii] = s[i]

    return ''.join(s)

print(urlencode("Hello there, partner    ", 20))

def urlencode(s):
    return '%20'.join(s.split())

print(urlencode("Hello there, partner    "))
