
import time
import unittest
from collections import Counter,defaultdict


def mysol(s1,s2):
    return len(s1) == len(s2) and Counter(s1) == Counter(s2)
    
def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def check_permutation_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for c in str1:
        counter[ord(c)] += 1
    for c in str2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1
    return True


def check_permutation_pythonic(str1, str2):
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        mysol,
        check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic
    ]

    def test_cp(self):
        # true check

        num_runs = 1000000
        function_runtimes = defaultdict(float)
    
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                start = time.perf_counter()
                assert (check_permutation(str1,str2) == expected), f"{check_permutation.__name__} failed for value: {str1},{str2}"
                function_runtimes[check_permutation.__name__] += (
                    time.perf_counter() - start
                ) * num_runs

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
