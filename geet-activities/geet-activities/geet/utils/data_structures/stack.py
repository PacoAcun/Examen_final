import utils.data_structures.linked_list as linked_list
from linked_list import Node

class Stack:
    '''
    Stack object, list-based implementation.

    Attributes:
        elements (List): list of elements
        top (int): pointer at topmost position
    '''

    def __init__(self):
        self.elements = []
        self.top = -1

    def push(self, node: Node) -> None:
        '''
        Pushes element into the stack.

        Args:
            node (Node): node to be inserted

        Returns:
            None
        '''
        self.elements.append(node)
        self.top += 1

    def pop(self) -> Node:
        '''
        Pops element out of stack.

        Returns:
            node (Node): node of element popped
        '''
        if self.is_empty():
            print('Stack underflow :(')
            return None

        node = self.elements.pop()
        self.top -= 1
        return node

    def peek(self) -> Node:
        '''
        Peeks topmost element.

        Returns:
            node (Node): node of element peeked
        '''
        if self.is_empty():
            print('Stack underflow :(')
            return None

        return self.elements[self.top]

    def is_empty(self) -> bool:
        '''
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise
        '''
        return self.top == -1

    def search(self, key: Node) -> int:
        '''
        Searches for the key in the stack.

        Args:
            key (Node): node to search for

        Returns:
            index (int): index of the key in the stack, -1 if not found
        '''
        for i in range(self.top, -1, -1):
            if self.elements[i] == key:
                return i

        return -1
