from unittest import TestCase
from linked_list import LinkedList, LinkedNode


class TestLinkedList(TestCase):

    def test_empty(self):
        ll = LinkedList()
        assert ll.head is None
        assert ll.tail is None
        assert len(ll) == 0

    def test_one(self):
        a = LinkedNode("A")
        ll = LinkedList(a)

        assert ll.head is a
        assert ll.tail is a
        assert len(ll) == 1

    def test_reappend_head(self):
        a = LinkedNode("A")
        ll = LinkedList(a)
        ll.append(a)

        assert ll.head is a
        assert ll.tail is a
        assert len(ll) == 1

    def test_two(self):
        a = LinkedNode("A")
        b = LinkedNode("B")
        ll = LinkedList(a)
        ll.append(b)

        assert ll.head is a
        assert ll.tail is b
        assert a.next_ is b
        assert b.next_ is None
        assert len(ll) == 2

    def test_append_left(self):
        a = LinkedNode("A")
        b = LinkedNode("B")
        ll = LinkedList(a)
        ll.appendleft(b)

        assert ll.head is b
        assert ll.tail is a
        assert b.next_ is a
        assert a.next_ is None
        assert len(ll) == 2

    def test_get_index(self):
        a = LinkedNode("A")
        b = LinkedNode("B")
        c = LinkedNode("C")
        ll = LinkedList(a)
        ll.append(b)
        ll.appendleft(c)

        assert ll[0] is c
        assert ll[1] is a
        assert ll[2] is b

    def test_delete(self):
        a = LinkedNode("A")
        b = LinkedNode("B")
        c = LinkedNode("C")
        d = LinkedNode("D")
        e = LinkedNode("E")
        f = LinkedNode("F")
        ll = LinkedList(a)
        ll.append(b)
        ll.append(c)
        ll.append(d)
        ll.append(e)
        ll.append(f)

        assert len(ll) == 6
        assert list(ll) == [a.value, b.value, c.value, d.value, e.value, f.value]

        ll.delete_item(1)
        assert len(ll) == 5
        assert list(ll) == [a.value, c.value, d.value, e.value, f.value]

        ll.delete_item(3)
        assert len(ll) == 4
        assert list(ll) == [a.value, c.value, d.value, f.value]

    def test_insert(self):
        a = LinkedNode("A")
        b = LinkedNode("B")
        c = LinkedNode("C")
        d = LinkedNode("D")
        e = LinkedNode("E")
        f = LinkedNode("F")
        ll = LinkedList(a)
        ll.append(b)
        ll.append(c)

        assert len(ll) == 3
        assert list(ll) == [a.value, b.value, c.value]

        ll.insert(0, d)
        assert len(ll) == 4
        assert list(ll) == [d.value, a.value, b.value, c.value]
        assert ll.head is d

        ll.insert(3, e)
        assert len(ll) == 5
        assert list(ll) == [d.value, a.value, b.value, e.value, c.value]
        assert ll.head is d
        assert ll.tail is c
