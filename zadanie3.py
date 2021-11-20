from zadanie1 import LinkedList


class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def peek(self):
        first_elem = self.storage.node(0)
        return first_elem

    def enqueue(self, element):
        self.storage.append(element)

    def dequeue(self):
        first_elemt = self.storage.pop()
        return first_elemt

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        if self.storage.head is None:
            print("Kolejka jest pusta.")
            return

        iterator = self.storage.head
        elems = []
        while iterator:
            elems.append(iterator.value)
            iterator = iterator.next_n
        return ', '.join(elems)


def proposed_test():
    queue = Queue()
    assert len(queue) == 0

    queue.enqueue('klient1')
    queue.enqueue('klient2')
    queue.enqueue('klient3')

    assert str(queue) == 'klient1, klient2, klient3'

    client_first = queue.dequeue()

    assert client_first == 'klient1'
    assert str(queue) == 'klient2, klient3'
    assert len(queue) == 2


if __name__ == '__main__':
    proposed_test()