import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new
        self._size += 1

    def size(self):
        return self._size

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if not self._current:
            raise StopIteration
        val = self._current.value
        self._current = self._current.next
        return val

    def __str__(self):
        return " ".join(str(x) for x in self)

def main():
    ll = LinkedList()
    for _ in range(10):
        ll.append(random.randint(0, 100))
    print(ll)
    print(ll.size())

if __name__ == "__main__":
    main()