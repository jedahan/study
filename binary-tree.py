class node:
    left = None
    right = None
    data = None
    parent = None

    def __init__(self, data):
        self.data = data

    def __str__(self):
        if self.data != None:
            s = " " * (self.height()+1) + str(self.data)
            if self.left != None and self.right != None:
                s = s + "\n" \
                      + " " * self.height() + "/ \\\n" \
                      + str(self.left) + str(self.right)
            return s
        else:
            return ""

    def walk(self):
        if self != None:
            if self.left: self.left.walk()
            print(self.data)
            if self.right: self.right.walk()

    def height(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None:
            return self.right.height()
        elif self.right == None:
            return self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    def add(self, data):
        if self.left == None:
            self.left = node(data)
        elif self.right == None:
            self.right = node(data)
        else:
            if(self.left.height()>self.right.height()):
                self.left.add(data)
            else:
                self.right.add(data)

root = node(None)

root.add(1)
root.add(3)
root.add(3)
root.add(3)
root.add(2)

print(root)
root.walk()
