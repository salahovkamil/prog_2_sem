class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.head = Node('head')

    def __str__(self):
        cur = self.head.next
        out = ''
        sep = '->'
        while cur:
            out += f'{cur.value} {sep} '
            cur = cur.next
        out = out[:-3]
        return out

    def push(self, value):
        new_element = Node(value)
        new_element.next = self.head.next
        self.head.next = new_element

    def pop(self):
        tmp = self.head.next.value
        # del self.head.next
        self.head.next = self.head.next.next
        return tmp


s = Stack()
for i in range(5):
    s.push(i)
print(f"Stack: {s}")
