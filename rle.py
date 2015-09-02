def run_length_encoding(string):
    prev = ''
    count = 0
    new = ""
    for character in string:
        if character == prev:
            count = count+1
        else:
            if count>0:
                new = new + prev + str(count)
            prev = character
            count = 1

    new = new + prev + str(count)
    if len(new) > len(string):
        return string
    else:
        return new

assert(run_length_encoding("abbbc")=="abbbc")
assert(run_length_encoding("abbbbbc")=="a1b5c1")
