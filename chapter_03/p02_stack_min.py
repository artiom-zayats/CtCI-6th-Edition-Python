from stack import Stack


class MinStack2(Stack):
    def __init__(self):
        super().__init__()
        self.minvals = Stack()

    def push(self, value):
        super().push(value)
        if not self.minvals or value <= self.minimum():
            self.minvals.push(value)

    def pop(self):
        value = super().pop()
        if value == self.minimum():
            self.minvals.pop()
        return value

    def minimum(self):
        return self.minvals.peek()


class MinStack():

    def __init__(self):
        self.stack = []
    
    def push(self,val):
        if self.stack:
            new_min = min(self.stack[-1][1],val)
        else:
            new_min = val
        self.stack.append([val,new_min])

    def pop(self):
        if self.stack:
            val,_ = self.stack.pop()
            return val
        return None

    def minimum(self):
        if self.stack:
            mn = self.stack[-1][1]
            return mn
        return None



def test_min_stack():
    newstack = MinStack()
    assert newstack.minimum() is None

    newstack.push(5)
    assert newstack.minimum() == 5

    newstack.push(6)
    assert newstack.minimum() == 5

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.push(7)
    assert newstack.minimum() == 3

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 5

    newstack.push(1)
    assert newstack.minimum() == 1

    print("Done")


if __name__ == "__main__":
    test_min_stack()
