

import time
import unittest


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, node):
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = node

    def pop_head(self):
        if self.head is not None:
            head_to_pop = self.head
            self.head = self.head.next_node
            return head_to_pop

        return None

    def size(self):
        current_node = self.head
        size = 0
        while current_node is not None:
            size += 1
            current_node = current_node.next_node
        return size


class Animal:
    def __init__(self,name):
        self.time = time.time()
        self.name = name

    def __str__(self) -> str:
        return str(self.name)

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter:

    def __init__(self):
        self.list = LinkedList()

    def enqueue(self,animal):
        self.list.insert(Node(animal))

    def DequeuCat(self):
        animal = None
        if self.list.size() != 0:
            current = self.list.head

            if isinstance(current.data, Cat):
                return self.list.pop_head()

            prev = Node(None)
            while current:
                if isinstance(current.data, Cat):
                    animal = current.data
                    prev.next_node = current.next_node
                    return animal
                else:
                    prev = current
                    current = current.next_node
        
        return animal


    def DequeuDog(self):
        animal = None
        if self.list.size() != 0:
            current = self.list.head
            prev = Node(None)

            if isinstance(current.data, Dog):
                return self.list.pop_head()

            while current:
                if isinstance(current.data, Dog):
                    animal = current.data
                    prev.next_node = current.next_node
                    return animal
                else:
                    prev = current
                    current = current.next_node
        
        return animal

    def DequeuAny(self):
        if self.list.size() != 0:
            animal = self.list.pop_head()
            return animal
        else:
            return None

    def size(self):
        return self.list.size()






def test_enqueue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("Fluffy"))
    animal_shelter.enqueue(Dog("Sparky"))
    animal_shelter.enqueue(Cat("Sneezy"))
    assert animal_shelter.size() == 3
    print("Done")


def test_dequeue_any():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("Fluffy"))
    animal_shelter.enqueue(Dog("Sparky"))
    animal_shelter.enqueue(Cat("Sneezy"))
    assert str(animal_shelter.DequeuAny()) == "Fluffy"
    assert str(animal_shelter.DequeuAny()) == "Sparky"
    assert str(animal_shelter.DequeuAny()) == "Sneezy"

def test_dequeu_dog():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("Fluffy"))
    animal_shelter.enqueue(Dog("Sparky"))
    animal_shelter.enqueue(Cat("Sneezy"))
    animal_shelter.enqueue(Dog("Bneezy"))
    assert str(animal_shelter.DequeuDog()) == "Sparky"
    assert str(animal_shelter.DequeuDog()) == "Bneezy"
    assert str(animal_shelter.DequeuDog()) == "None"

def test_dequeu_cat():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("Fluffy"))
    animal_shelter.enqueue(Dog("Sparky"))
    animal_shelter.enqueue(Cat("Sneezy"))
    assert str(animal_shelter.DequeuCat()) == "Fluffy"
    assert str(animal_shelter.DequeuCat()) == "Sneezy"
    assert str(animal_shelter.DequeuCat()) == "None"




if __name__ == "__main__":
    test_enqueue()
    test_dequeue_any()
    test_dequeu_dog()
    test_dequeu_cat()
