from typing import Any


class LinkedNode:
    def __init__(self, value: Any, next_: "LinkedNode | None" = None):
        self.value = value
        self.next_ = next_


class DoubleLinkedNode(LinkedNode):

    def __init__(self, value: Any, next_: LinkedNode | None = None, prev: LinkedNode | None = None):
        super().__init__(value)
        self.prev = prev


class LinkedList:

    def __init__(self, head: LinkedNode = None):
        self.head = head
        self.tail = None

        if self.head:
            t = self.head
            while t.next_:
                t = t.next_
            self.tail = t

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next_

    def __getitem__(self, item):
        return self.get_index(index=item)

    def __len__(self):
        if not self.head:
            return 0

        i = 1
        r = self.head
        while r.next_:
            i += 1
            r = r.next_

        return i

    def get_index(self, index: int) -> LinkedNode:

        if index < 0:
            raise ValueError("negative indexing not supported")

        i = 0
        r = self.head
        while i < index:
            r = r.next_
            if r is None:
                raise IndexError(f"Index {index} out of range")
            i += 1

        return r

    def append(self, item: LinkedNode, use_tail: bool = True):

        if self.head is None:
            self.head = item
            self.tail = item

        if item is self.head:
            if self.head.next_:
                self.head = self.head.next_

        if use_tail is True:
            self.tail.next_ = item
            self.tail = item
            item.next_ = None

        else:
            r = self.head
            while r.next_ is not None:
                r = r.next_

            r.next_ = item
            self.tail = item
            item.next_ = None

    def appendleft(self, item: LinkedNode):
        if item is self.head:
            return

        item.next_ = self.head
        self.head = item

    def insert(self, index: int, item: LinkedNode):
        if index == 0:
            item.next_ = self.head
            self.head = item

        else:
            item.next_ = self[index]
            self[index-1].next_ = item

    def delete_item(self, index: int):

        if index == 0:
            self.head = self.head.next_

            if self.head is None:
                self.tail = None

            if self.head.next_ is None:
                self.tail = self.head

        prev = self.get_index(index-1)
        prev.next_ = prev.next_.next_

        if prev.next_ is None:
            self.tail = prev


if __name__ == '__main__':

    C = LinkedNode("C")
    B = LinkedNode("B", next_=C)
    A = LinkedNode("A", next_=B)
    ll = LinkedList(A)

    ll2 = LinkedList(A, C)

    assert ll == ll2
