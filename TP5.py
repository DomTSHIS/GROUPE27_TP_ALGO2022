# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:00:21 2023

@author: MULAMBA-CEDRICK
"""

class CircularQueue:
    """Queue implementation using
    circularly linked list for storage"""
    class _Node:
        """Lightweight, nonpublic class
        for storing a singly linked node
        (omitted here; identical to that
        of LinkedStack._Node)"""
    def __init__(self):
        """ Create an empty queue"""
        self._tail = None
        self._size = 0
    def __len__(self):
        """Return the number of
        elements in the queue"""
        return self._size
    def is_empty(self):
        """Return True if the
        queue is empty."""
        return self._size == 0
    def first(self):
        """Return (but not remove)
        the element at the front of
        the queue. Raise Empty
        exception if the queue is empty."""
        if self.is_empty():
            raise Empty("Queue is empty")
        head = self._tail._next
        return head._element
    def dequeue(self):
            """Remove and return the first
            element of the queue (FIFO).
            Raise Empty exception if the
            queue is empty."""
            if self._isempty():
                raise Empty("Queue is empty")
            oldhead = self._tail._next
            if self._size == 1:
                self._tail = None
            else:
                self._tail._next = oldhead._next
                self._size -= 1
            return oldhead._element
    def enqueue(self, e):
        """Add an element to the back
        of the queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = self._tail._next
            self._tail_next = newest
        self._tail = newest
        self._size += 1
    def rotate(self):
        """Rotate front element to
        the back of the queue."""
        if self._size >0:
            self._tail = self._tail._next
