class Terminal(object):
    """docstring for Terminal."""

    def __init__(self, symbol):
        super(Terminal, self).__init__()
        self._is_epsilon = False
        self._is_closing = False
        self.symbol = symbol

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        if(symbol == "~"):
            self._is_epsilon = True
        elif(symbol == "$"):
            self._is_closing = True
        self._symbol = symbol

    @property
    def is_nullable(self):
        return self._is_epsilon
