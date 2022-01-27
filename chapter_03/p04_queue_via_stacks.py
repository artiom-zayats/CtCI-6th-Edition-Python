# 3.4 Queue Via Stacks
import unittest
from stack import Stack


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def _move(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())


    def add(self, value):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        self.stack1.append(value)

    def peek(self):
        self._move()
        if self.stack2:
            return self.stack2[-1]
        return None


    def remove(self):
        self._move()
        if self.stack2:
            return self.stack2.pop()
        return None

    def is_empty(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        return False


    def __len__(self):
        return len(self.stack1) + len(self.stack2)












class Tests(unittest.TestCase):
    test_cases = [([1,2,3,4,5,6])]

    def test_size(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for index, val in enumerate(sequence, start=1):
                q.add(val)
                assert len(q) == index
            for index, val in enumerate(sequence, start=1):
                q.remove()
                assert len(q) == len(sequence) - index

    def test_add(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            assert q.peek() == sequence[0]
            assert len(q) == len(sequence)

    def test_peek(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
                assert q.peek() == sequence[0]
            q.remove()
            assert q.peek() == sequence[1]

    def test_remove(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            for i in range(len(sequence)):  # noqa
                assert q.remove() == sequence[i]

    def test_peek_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4

    def test_add_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4
        q.add(101)
        assert q.peek() != 101

    def test_remove_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert len(q) == 2
        assert q.remove() == 4
        assert q.remove() == 6
        assert len(q) == 0
        assert not q.remove()
        

if __name__ == "__main__":
    unittest.main()