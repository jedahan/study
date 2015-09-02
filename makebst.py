import random

def bst(arr):
    if len(arr) == 1:
        return {"data": arr[0]}
    else:
        mid = int(len(arr)/2)
        root = {"data": arr[mid]}
        root["left"] = bst(arr[:mid])
        root["right"] = bst(arr[mid+1:])
        return root

def bst_str(root):
    if not root: return ""
    return "{} {} {}".format(bst_str(root.left),root.data,bst_str(root.right))

randlist = sorted([int(random.random()*15) for i in range(15)])
print(randlist)
tree = bst(randlist)
print(tree)

print(bst_str(tree))
