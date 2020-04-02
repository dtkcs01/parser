import os
import sys
import pprint
sys.path.append(os.path.join(os.getcwd(), "classes"))
from ProductionClass import Production
from TerminalClass import Terminal

class Parser(object):
    """docstring for Parser."""

    def __init__(self, terminals, non_terminals):
        super(Parser, self).__init__()
        self.load_table(terminals, non_terminals)
        self.create_parse_table(terminals, non_terminals)

    def load_table(self, terminals, non_terminals):
        self._table = [ [ None for j in range(len(terminals)) ] for i in range(len(non_terminals)) ]
        i = 0
        self._non_terminal_indexes = {}
        for non_terminal in non_terminals:
            self._non_terminal_indexes.setdefault(non_terminal, i)
            i += 1
        i = 0
        self._terminal_indexes = {}
        for terminal in terminals:
            self._terminal_indexes.setdefault(terminal, i)
            i += 1

    def create_parse_table(self, terminals, non_terminals):
        for non_terminal, element in non_terminals.items():
            for (first, production) in element.first_set:
                if(first.is_nullable):
                    for (follow, _) in element.follow_set:
                        i = self._non_terminal_indexes[non_terminal]
                        j = self._terminal_indexes[follow.symbol]
                        self._table[i][j] = Production(terminals, non_terminals, [non_terminal, ":", "~"])
                else:
                    i = self._non_terminal_indexes[non_terminal]
                    j = self._terminal_indexes[first.symbol]
                    self._table[i][j] = production

    def test(self, test_array, terminals, non_terminals, init):
        steps = []
        err = test_array.copy()
        test_array.append("$")
        stack = [ [ non_terminals[init], terminals["$"] ], test_array]
        while(stack[0] and stack[1]):
            steps.append([ [ s.symbol for s in stack[0] ], stack[1].copy() ])
            l_stack = stack[0].pop(0)
            r_stack = stack[1][0]
            if(not r_stack in terminals):
                steps[-1].append("Error : Unknown identifier '{}' in '{}' at index '{}'".format(test_array.pop(0), " ".join(err), (len(err) - len(test_array))))
                steps[-1].append(True)
            elif(l_stack.symbol == r_stack):
                steps[-1].append("Shift")
                steps[-1].append(False)
                stack[1].pop(0)
            elif(isinstance(l_stack, Terminal) and l_stack.is_nullable):
                steps[-1].append("Shift")
                steps[-1].append(False)
            else:
                i = self._non_terminal_indexes[l_stack.symbol]
                j = self._terminal_indexes[r_stack]
                production = self._table[i][j]
                if(production):
                    steps[-1].append("Reduce")
                    steps[-1].append(False)
                    stack[0] = [ element for element in production.rhs ] + stack[0]
                else:
                    steps[-1].append("Error : Invalid Syntax due to identifier '{}' in '{}' at index '{}'".format(test_array.pop(0), " ".join(err), (len(err) - len(test_array))))
                    steps[-1].append(True)
        return steps
