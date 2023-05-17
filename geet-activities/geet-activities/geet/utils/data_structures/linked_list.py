'''
[Data Structure] Linked List implementation.
'''


class Node:
    '''
    Node object.

    Attributes:
        hash (str): commit's hash
        message (str): commit's message
        author (str): user's name
        email (str): user's email
        next (Node): pointer to next node in list

    ⬇ Your code starts here:
    '''
    def __init__(self, commit_hash=None, message=None, author=None, email=None):
        self.commit_hash = commit_hash
        self.message = message
        self.author = author
        self.email = email
        self.next_node = None
    '''
    ⬆ Your code ends here.
    '''

class LinkedList:
    '''
    Linked List object.

    Attributes:
        start (Node): pointer to first node in list

    Methods:
        __init__(self)
        __iter__(self)
        traverse(self)
        insert_first(self, node)
        insert_last(self, node)
        remove(key)
        reverse(self)

    ⬇ Your code starts here:
    '''
    def __init__(self):
        self.start = None


    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next_node
    
    def traverse(self):
        '''
        Navigates every node in the list.
        Args:
            None
        Returns:
            None
        '''
        
        current_node = self.start

        while current_node is not None:
            print(current_node)
            current_node = current_node.next

    def insert_first(self, node):
        '''
        Inserts a node at the beginning of the list.
        Args:
            node (Node): node to be inserted
        Returns:
            None
        '''
        node.next_node = self.start
        self.start = node

    def insert_last(self, node):
        '''
        Inserts a node at the end of the list.
        Args:
            node (Node): node to be inserted
        Returns:
            None
        '''
        if self.start is None:
            self.start = node
        else:
            current_node = self.start
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = node

    def remove(self, key):
        '''
        Removes a node from the list.
        Args:
            key (str): commit's hash
        Returns:
            None
        '''
        current_node = self.start
        previous_node = None

        while current_node.commit_hash != key:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:
            self.start = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

    def reverse(self):
        '''
        Reverses the list.
        Args:
            None
        Returns:
            None
        '''
        current_node = self.start
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.start = previous_node

    '''
    ⬆ Your code ends here.
    '''
