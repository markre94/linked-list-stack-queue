from zadanie1 import LinkedList


class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def push(self, elem):
        self.storage.append(elem)

    def pop(self):
        top_stack_value = self.storage.remove_last()
        return top_stack_value

    def __len__(self):
        return len(self.storage)

    def __repr__(self):
        if self.storage.head is None:
            print('Stack jest pusty')
            return
        iterator = self.storage.head
        elements = []
        while iterator:
            elements.append(iterator.value)
            iterator = iterator.next_n
        elems = ''
        for elem in reversed(elements):
            elems += str(elem) + '\n'
        return elems


def proposed_test():
    stack = Stack()
    assert len(stack) == 0
    stack.push(3)
    stack.push(10)
    stack.push(1)
    assert len(stack) == 3
    top_value = stack.pop()
    assert top_value == 1
    assert len(stack) == 2


if __name__ == '__main__':
    proposed_test()
