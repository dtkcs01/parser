import os
import sys
sys.path.append(os.path.join(os.getcwd(), "classes"))
from TerminalClass import Terminal

class Production(object):
    """docstring for Production."""

    def __init__(self, terminals, non_terminals, production):
        super(Production, self).__init__()
        self._terminals = terminals
        self._non_terminals = non_terminals
        self.load_production(production)

    def load_production(self, production):
        self._LHS = self._non_terminals[production[0]]
        self._RHS = []
        for elem in production[2:]:
            if elem in self._non_terminals:
                self._RHS.append(self._non_terminals[elem])
            else:
                if not (elem in self._terminals):
                    self._terminals.setdefault(elem, Terminal(elem))
                self._RHS.append(self._terminals[elem])

    @property
    def rhs(self):
        for element in self._RHS:
            yield element

    @rhs.setter
    def rhs(self, element):
        if element:
            self._RHS.append(element)

    def load_follow(self, element):
        if(element in self._RHS):
            l = len(self._RHS)
            i = self._RHS.index(element) + 1
            if(i == l and self._LHS != element):
                for (follow, _) in self._LHS.follow_set:
                    element.follow_set = (follow, None)

            while(i < l):
                if(self._RHS[i].symbol in self._non_terminals):
                    for (first, _) in self._RHS[i].first_set:
                        if(not first.is_nullable):
                            element.follow_set = (first, None)
                else:
                    element.follow_set = (self._RHS[i], None)
                if(not self._RHS[i].is_nullable):
                    break
                else:
                    for (follow, _) in self._RHS[i].follow_set:
                        element.follow_set = (follow, None)
                i += 1
        return False

    def show(self):
        print("{} -> {}".format(self._LHS.symbol, " ".join([ elem.symbol for elem in self._RHS ])))
