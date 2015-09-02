class node:
    data = None
    left = None
    right = None
    color = "Black"

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "{} {} {}".format(self.left or "", self.data, self.right or "")

class rbtree:
    root = node(None)

    def __str__(self):
        return str(self.root)

    def add(self, data):
        print("adding {}".format(data))
        cursor = self.root
        if cursor.data == None:
            cursor.data = data
        else:
            while True:
                if data < cursor.data:
                    if cursor.left:
                        cursor = cursor.left
                    else:
                        cursor.left = node(data)
                        return
                else:
                    if cursor.right:
                        cursor = cursor.right
                    else:
                        cursor.right = node(data)
                        return
tree = rbtree()
for i in range(10):
    tree.add(int(15*random.random()))

print(tree)
