# O(N)
import time
import unittest


def mysol(s1,s2):
    return len(s1) == len(s2) and s1 in s2+s2



def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False



class Test(unittest.TestCase):
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]
    testable_functions = [mysol,
        string_rotation,
    ]

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for [s1,s2, expected] in self.test_cases:
                    assert f(s1,s2) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
