import math

def isbalanced(node):
    return checkdepth != -1

def checkdepth(node):
    leftheight = checkdepth(node.left)
    if lefthieght == -1: return -1
    rightheight = checkdepth(node.right)
    if righthieght == -1: return -1

    if math.abs(leftheight - rightheight) > 1:
        return -1
    else:
        return 1 + max(leftheight,rightheight)
