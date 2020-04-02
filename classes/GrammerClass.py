import os
import sys
sys.path.append(os.path.join(os.getcwd(), "classes"))
from ProductionClass import Production

class Grammer(object):
    """docstring for Grammer."""

    def __init__(self, terminals, non_terminals, productions, tests):
        super(Grammer, self).__init__()
        self._terminals = terminals
        self._non_terminals = non_terminals
        self.load_productions(productions)
        self.compute_first_pos(productions[0][0])
        self.compute_follow_pos(productions)
        self._tests = tests

    def load_productions(self, productions):
        self._productions = {}
        for production in productions:
            self._productions.setdefault(production[0], [])
            self._productions[production[0]].append(Production(self._terminals, self._non_terminals, production))
        self._non_terminals[productions[0][0]].follow_set = (self._terminals["$"], None)

    def compute_first_pos(self, non_terminal):
        self._non_terminals[non_terminal].is_discovered = True
        productions = self._productions[non_terminal]
        for production in productions:
            flag = True
            for element in production.rhs:
                if(element.symbol in self._non_terminals):
                    if(not element.is_discovered):
                        self.compute_first_pos(element.symbol)
                    if(flag):
                        for sub_element in element.first_set:
                            self._non_terminals[non_terminal].first_set = (sub_element[0], production)
                else:
                    if(flag):
                        self._non_terminals[non_terminal].first_set = (element, production)
                if(not element.is_nullable):
                    flag = False
            self._non_terminals[non_terminal].is_nullable = self._non_terminals[non_terminal].is_nullable or flag
        self._non_terminals[non_terminal].is_discovered = False

    def compute_follow_pos(self, productions):
        non_terminals = []
        for production in productions:
            element = self._non_terminals[production[0]]
            if(not element in non_terminals):
                non_terminals.append(element)
        for element in non_terminals:
            for non_terminal, sub_productions in self._productions.items():
                for sub_production in sub_productions:
                    sub_production.load_follow(element)

    def show(self):
        for non_terminal, productions in self._productions.items():
            for production in productions:
                production.show()
        print()
