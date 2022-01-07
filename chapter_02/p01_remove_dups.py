import time
import unittest
from unittest import runner

from linked_list import LinkedList


def mysol(ll):
    seen = set()
    cur = ll.head
    prev = None
    while cur:
        if cur.value not in seen:
            seen.add(cur.value)
            prev = cur
        else:
            prev.next = cur.next
        cur = cur.next
    ll.tail = prev
    return ll


def mysol2(ll):
    cur = ll.head
    run = ll.head

    while cur:
        run = cur
        while run.next:
            if cur.value == run.next.value:
                run.next = run.next.next
            else:
                run = run.next
        cur = cur.next

    ll.tail = run
    return ll


    

def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll


def remove_dups_followup(ll):
    runner = current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    ll.tail = runner
    return ll


class Test(unittest.TestCase):


    testable_functions = [mysol,mysol2,remove_dups,remove_dups_followup]
    test_cases = (
        ([], []),
        ([1, 1, 1, 1, 1, 1], [1]),
        ([1, 2, 3, 2], [1, 2, 3]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
    )


    def test_remove_dupes(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [values, expected] in self.test_cases:
                    expected = expected.copy()
                    deduped = f(LinkedList(values))
                    assert deduped.values() == expected

                    deduped.add(5)
                    expected.append(5)
                    assert deduped.values() == expected

            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")




if __name__ == "__main__":
    unittest.main()