# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 19:00:25 2023

@author: MULAMBA-CEDRICK
"""

class LinkedDeque:
    """Double-ended queue implementation
    based on a doubly linked list """
    def first(self):
        """Return (but not remove) the element
        at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element
    def last(self):
        """Return (but not remove) the
        element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element
    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header_next)
    def delete_first(self):
        """Remove and return the element from the
        front of the deque.
        Raise Empty exception if deque is empty."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete._node(self._header._next)
    def delete_last(self):
        """Remove and return the element from the
        back of the deque.
        Raise Empty exception if deque is empty."""
        if self.is_empty():
           raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)
