import os
import sys
sys.path.append(os.path.join(os.getcwd(), "classes"))

class NonTerminal(object):
    """docstring for NonTerminal."""

    def __init__(self, symbol):
        super(NonTerminal, self).__init__()
        self._symbol = symbol
        self._is_nullable = False
        self._is_discovered = False
        self._first_pos = set()
        self._follow_pos = set()

    @property
    def symbol(self):
        return self._symbol

    @property
    def is_nullable(self):
        return self._is_nullable

    @is_nullable.setter
    def is_nullable(self, is_nullable):
        self._is_nullable = is_nullable

    @property
    def is_discovered(self):
        return self._is_discovered

    @is_discovered.setter
    def is_discovered(self, is_discovered):
        self._is_discovered = is_discovered

    @property
    def first_set(self):
        for first in self._first_pos:
            yield first

    @first_set.setter
    def first_set(self, first):
        if(first):
            self._first_pos.add(first)

    @property
    def follow_set(self):
        for follow in self._follow_pos:
            yield follow

    @follow_set.setter
    def follow_set(self, follow):
        if(follow):
            self._follow_pos.add(follow)
