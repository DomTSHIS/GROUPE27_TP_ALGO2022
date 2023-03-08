# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:38:46 2023

@author: MULAMBA-CEDRICK
"""

class LinkedQueue:
    """FIFO queue implementation using
    a singly linked list for storage """
    class _Node:
        """ Lightweight, nonpublic class
        for storing a singly linked node."""
        __slots__ = "_element", "_next"
    def __init__(self, element, next):
        self._element = element
        self._next = next
    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        """Return the number of
        elements in the queue"""
        return self._size
    def is_empty(self):
        """Return True if the
        queue is empty """
        return self._size == 0
    def first(self):
        """Return (but not remove)
        the element at the front of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element
