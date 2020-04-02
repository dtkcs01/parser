class Parser(object):
    """docstring for Parser."""

    def __init__(self, terminals, non_terminals):
        super(Parser, self).__init__()
        self.load_table(terminals, non_terminals)
        print(self._non_terminal_indexes)
        print(self._terminal_indexes)
        print(self._table)

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
