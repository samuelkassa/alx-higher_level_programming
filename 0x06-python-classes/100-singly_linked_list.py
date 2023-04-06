#!/usr/bin/python3
"""Singly linked list with class"""


class Node:
    """Singly linked list with class"""

    def __init__(self, data, next_node=None):
        """initialize a new Node
        Args:
            data (int): The data of the new node
            next_node (Node): The next node of the new node
        """
        self.data = date
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (type(value) is not int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """Represent a singly linked list"""

    def __init__(self):
        """iniliaze a new linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new node to SinglyLinkedList
        
        The node is inserted into the list at the correct
        ordering position
        
        Args:
            value(Node): The new node to insert
        """

        new = Node(value)
        if self.__head = None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

        def __str__(self):
            """Defining the print() representation of SinglyLinkedList"""
            value = []
            temp = self.__head
            while temp is not None:
                value.append(str(temp.data))
                temp = temp.next_node
            return('\n'.join(value))

