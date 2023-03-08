# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:32:49 2023

@author: MULAMBA-CEDRICK
"""

class LinkedStack:
    """LIFO Stack implementation using
    a singly linked list for storage"""
    # ------------ nested _Node class -----------
    class _Node:
        """ Lightweight, nonpublic class
        for storing a singly linked node."""
        __slots__ = "_element", "_next"
    def __init__(self, element, next):
        self._element = element
        self._next = next
        # stack methods
    def __init__(self):
        """ Create an empty stack."""
        self._head = None
        self._size = 0
    def __len__(self):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1
    def top(self):
        """ Return (but not remove) the element
        at the top of the stack
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element
    def pop(self):
        """Remove and return the element
        at the top of the stack (LIFO)
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
