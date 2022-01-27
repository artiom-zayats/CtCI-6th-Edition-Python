# 3.5 Sort Stacks
import re
import unittest

from stack import Stack



class SortedStack(Stack):
    def __init__(self):
        self.stack = []
        self.temp = []
    def push(self,item):

        if not self.stack:
            self.stack.append(item)

        else:
            if self.stack[-1]>= item:
                self.stack.append(item)
            else:
                while self.stack:
                    if self.stack[-1] <= item:
                        self.temp.append(self.stack.pop())
                    else:
                        self.temp.append(item)
                        item = None
                if item:
                    self.temp.append(item)
                while self.temp:
                    self.stack.append(self.temp.pop())


    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        pass

    def __len__(self):
        return len(self.stack)


class Tests(unittest.TestCase):
    def test_push_one(self):
        queue = SortedStack()
        queue.push(1)
        assert len(queue) == 1

    def test_push_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert len(queue) == 2

    def test_push_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert len(queue) == 3

    def test_pop_one(self):
        queue = SortedStack()
        queue.push(1)
        assert queue.pop() == 1

    def test_pop_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        assert queue.pop() == 1
        assert queue.pop() == 2

    def test_pop_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3

    def test_push_mixed(self):
        queue = SortedStack()
        queue.push(3)
        queue.push(2)
        queue.push(1)
        queue.push(4)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3
        assert queue.pop() == 4


if __name__ == "__main__":
    unittest.main()
