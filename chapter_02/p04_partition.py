from linked_list import LinkedList,LinkedListNode
import random


def mysol(ll,x):
    
    less = LinkedListNode(None)
    head_less = less 
    greater = LinkedListNode(None)
    head_greater = greater

    cur = ll.head

    while cur:
        nxt_val = cur.next
        if cur.value < x:
            less.next = cur
            less = less.next
        

        else:

            greater.next = cur
            greater = greater.next

        
        cur = nxt_val
    less.next = head_greater.next

    ll.head = head_less.next
    ll.tail = greater

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None


def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None


def example():

    ll = LinkedList.generate(10, 0, 99)
    print(ll)
    print("head",ll.head.value)
    partition(ll, ll.head.value)
    print(ll)


def example2():

    ll = LinkedList.generate(10, 0, 99)
    print(ll)
    print("head",ll.head.value)
    mysol(ll, ll.head.value)
    print(ll)


if __name__ == "__main__":
    example()
    print("done")
    example2()
