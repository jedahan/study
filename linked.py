import random

class Node:
  data = None
  next = None

  def __init__(self,data):
      self.data = data

  def __str__(self):
      cursor = self
      s = "["
      while cursor.next != None:
          s = s + str(cursor.data) + ","
          cursor = cursor.next
      s = s + str(cursor.data)+"]"
      return s

  def append(self,data):
      temp = Node(data)
      tail = self
      while tail.next != None:
          tail = tail.next
      tail.next = temp

  def delete(self, data):
      if self.data == data: return self.next
      cursor = self
      while cursor.next != None:
          if cursor.next.data == data:
              cursor.next = cursor.next.next
              return
          cursor = cursor.next

head = Node(1)

for i in range(3):
    head.append(int(random.random()*25))

head.append(17)
head.append(9999)

print(head)

# k from the end
def get(head,k):
    window = [-1 for i in range(k+1)]

    i = 0
    cursor = head
    while cursor.next != None:
        window[i] = cursor.data
        i = ((i + 1) % len(window))
        cursor = cursor.next

    return window[i - k % len(window) + 1]

print(get(head,3))

def delete(node):
    node.data = node.next.data
    delete(node.next)
