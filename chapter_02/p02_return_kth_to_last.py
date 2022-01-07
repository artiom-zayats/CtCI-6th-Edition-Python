from linked_list import LinkedList



def mysol(ll,k):
    slow = ll.head
    fast = ll.head

    for _ in range(k):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next
    
    return slow



def mysol2(ll,k):
    
    counter = 0

    def helper(node,kk):
        nonlocal counter
        if not node:
            return None
        nxt = helper(node.next,k)
        counter += 1
        if counter == k:
            return node
        
        return nxt

    return helper(ll.head,k)




def kth_to_last(ll, k):
    runner = current = ll.head
    for _ in range(k):
        if not runner:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


# O(N) space
def kth_last_recursive(ll, k):
    head = ll.head
    counter = 0

    def helper(head, k):
        nonlocal counter
        if not head:
            return None
        helper_node = helper(head.next, k)
        counter = counter + 1
        if counter == k:
            return head
        return helper_node

    return helper(head, k)


test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
    ((10, 20, 30, 40, 50), 2, 40),
    ((10, 20, 30, 40, 50), 3, 30),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected
        assert kth_last_recursive(ll, k).value == expected
        assert mysol(ll,k).value == expected
        assert mysol2(ll,k).value == expected
    print("done")


if __name__ == "__main__":
    test_kth_to_last()
