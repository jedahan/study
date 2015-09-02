import math

class unbalanced:
    tree = list()

    def add(self,data):
        self.tree.append(data)

    def __str__(self):
        s = ""
        max_depth = math.log(len(self.tree),2)
        i = 0
        while i < max_depth:
            for j in math.log(i,2):
                s = s + " "*2*(max_depth - j)
                s = s + self.tree[i]
            i = i+1

tree = unbalanced()

tree.add(1)
tree.add(2)
tree.add(3)

print(tree)
