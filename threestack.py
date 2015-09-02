class threestack:
    stacks = [i for i in range(9)]
    indices = [0, len(stacks)/3, len(stacks)*2/3]
    sizes = [0, 0, 0]

    def __str__(self):
        s = "["
        for d in self.stacks:
            s = s + str(d) + ","
        return s[:-1] + "]"

    def push(self, stack, data):
        end = self.indices[stack] + self.sizes[stack]
        if end == self.indices[stack+1 % len(self.indices)]:
            print("OH SHIT WE ARE OVERWRITING")
        else:
            self.stacks[end] = data
            self.sizes[stack] = self.sizes[stack] + 1

    def pop(self, stack):
        return stacks[self.indices[stack]]

stacks = threestack()
print(stacks)

stacks.push(0,1)
stacks.push(0,2)
stacks.push(0,3)
print(stack.pop(0))

stacks.push(1,"a")
stacks.push(1,"b")
stacks.push(1,"c")

stacks.push(2,True)
stacks.push(2,True)
stacks.push(2,False)

print(stacks)
