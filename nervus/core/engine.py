class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op

    def __add__(self, other):
        return Value(
            self.data + other.data,
            (self, other),
            '+'
        )

    def __mul__(self, other):
        return Value(
            self.data * other.data,
            (self, other),
            '*'
        )
