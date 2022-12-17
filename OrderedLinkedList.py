class Result:
  def __init__(self,value):
    self._value = value
  def __lt__(self,other):
      return self._value < other._value
  def __str__(self):
    return str(self._value)
  

class OrderedLinkedList:
  class Node:
    def __init__(self,cargo):
      self._cargo = cargo
      self._next = None
    def __lt__(self,other):
        return self._cargo < other._cargo
    def __str__(self):
        return str(self._cargo)

  def __init__(self):
    self._head = None

  def insert(self,cargo):
    node = OrderedLinkedList.Node(cargo)
    if self._head is None:
        self._head = node
    else:
        if node < self._head:
            node._next = self._head
            self._head = node
        else:
            itera = self._head
            while itera._next is not None:
                if node < itera._next:
                    node._next = itera._next
                    itera._next = node
                    return self
                itera = itera._next
            itera._next = node
    return self
  def __str__(self):           
    s = str(self._head)
    itera = self._head
    while itera._next is not None:
        s += '->' + str(itera._next)
        itera = itera._next
    return s

print (OrderedLinkedList().insert(Result(3)).insert(Result(1)).insert(Result(0)).insert(Result(2)).insert(Result(10)))
