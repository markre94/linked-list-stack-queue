""" Zadanie 1."""


class Node:
    def __init__(self, value=None, next_n=None):
        self.value = value
        self.next_n = next_n

    def __str__(self):
        pointer = self.next_n.value if self.next_n else None
        return f"Element listy ma wartosc {self.value} wskazuje na element o wartosc {pointer}"


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data) -> None:
        node = Node(data, self.head)
        self.head = node

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        iterator = self.head
        while iterator.next_n:
            iterator = iterator.next_n

        iterator.next_n = Node(data, None)

    def node(self, at: int):
        """ Zwraca wartosc node'a bazujac na wartosci wskazanego indexu"""
        if at < 0 or at >= len(self):
            raise ValueError("Niepoprwany index")

        if at == 0:
            return self.head

        iterator = self.head
        count = 0
        while iterator:
            if count == at - 1:
                return iterator.next_n

            iterator = iterator.next_n
            count += 1

    def insert(self, value, after: Node):
        """ Umieszcza nowego Node'a listy bezpośrednio po wskazanym elemencie"""
        if after is None:
            raise ValueError("Bład danych")

        iterator = self.head
        while iterator:
            if iterator == after:
                node = Node(value, iterator.next_n)
                iterator.next_n = node
                break
            iterator = iterator.next_n

    def pop(self):
        """Usuwa i zwraca pierwszy element listy jednokierunkowej."""
        first = self.head
        self.head = self.head.next_n
        return first.value

    def remove_last(self):
        """ Usuwa i zwraca ostatni element listy jednokierunkowej."""
        iterator = self.head

        while iterator.next_n.next_n:
            iterator = iterator.next_n
        return_node = iterator.next_n
        iterator.next_n = None

        return return_node.value

    def remove(self, after: Node):
        """ Usuwa element z listy po podanym elemencie Node."""
        if after is None:
            raise ValueError("Bład danych. Podaj obiekt klasy Node")

        iterator = self.head

        while iterator.next_n:
            if iterator == after:
                return_node = iterator.next_n
                iterator.next_n = iterator.next_n.next_n
                return return_node

            iterator = iterator.next_n

    def print_list(self):
        """ Wyswietla liste wg. zadanego formatu"""
        if self.head is None:
            print("Lista jednokierunkowa jest pusta.")
            return

        iterator = self.head
        string_msg = ''
        while iterator:
            string_msg += str(iterator.value) + '-->'
            iterator = iterator.next_n
        print(string_msg)

    def __str__(self):
        """ Wyswietla liste wg. zadanego formatu"""
        if self.head is None:
            print("Lista jednokierunkowa jest pusta.")
            return

        iterator = self.head
        string_msg = ''
        while iterator:
            if iterator.next_n:
                string_msg += str(iterator.value) + ' -> '
            else:
                string_msg += str(iterator.value)
            iterator = iterator.next_n
        return string_msg

    def __len__(self) -> int:
        """Zwraca długość listy iterując po wszystkich elemtach listy jednokierunkowej"""
        counter_state = 0
        itr = self.head
        while itr:
            counter_state += 1
            itr = itr.next_n
        return counter_state


def main():
    ll = LinkedList()
    ll.append(5)
    ll.append(89)
    ll.append(101)
    ll.print_list()
    elem = ll.node(2)
    print(elem)
    ll.remove(elem)
    ll.print_list()


def proposed_test():
    list_ = LinkedList()

    assert list_.head == None

    list_.push(1)
    list_.push(0)

    assert str(list_) == '0 -> 1'

    list_.append(9)
    list_.append(10)

    assert str(list_) == '0 -> 1 -> 9 -> 10'

    middle_node = list_.node(at=1)
    list_.insert(5, after=middle_node)

    assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

    first_element = list_.node(at=0)
    returned_first_element = list_.pop()

    assert first_element.value == returned_first_element

    last_element = list_.node(at=3)
    returned_last_element = list_.remove_last()

    assert last_element.value == returned_last_element
    assert str(list_) == '1 -> 5 -> 9'

    second_node = list_.node(at=1)
    list_.remove(second_node)

    assert str(list_) == '1 -> 5'


if __name__ == '__main__':
    proposed_test()
