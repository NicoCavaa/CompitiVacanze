class Node(object):
    def __init__(self, value, next_node=None):
        self.__value = value
        self.__next = next_node
    def value(self):
        return self.__value
    def next(self):
        return self.__next
class Unisci(object):
    def __init__(self, values=[]):
        self.__head = None
        self.__length = 0
        for value in values:
            self.push(value)
    def __len__(self):
        return self.__length
    def __iter__(self):
        current_node = self.__head
        while current_node:
            yield current_node.value()
            current_node = current_node.next()
    def head(self):
        if self.__head is None:
            raise Vuota("La lista è vuota")
        return self.__head
    def push(self, value):
        self.__head = Node(value, next_node=self.__head)
        self.__length += 1
    def pop(self):
        value = self.head().value()
        self.__head = self.head().next()
        self.__length -= 1
        return value
    def reversed(self):
        return Unisci(list(self))
class Vuota(Exception):
    pass