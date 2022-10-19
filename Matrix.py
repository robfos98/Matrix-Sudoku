class vec:
    def __init__(self, x=[]):
        if not isinstance(x, list):
            raise ArithmeticError
        for a in x:
            if not isinstance(a, (int,float,)):
                raise ArithmeticError
        self.x = x