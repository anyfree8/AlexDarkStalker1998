class Calculator:

    def __init__(self, init_value=0, max_count=10):
        self.__dict__["MaxCount"] = max_count
        self.value = init_value

    def __setattr__(self, key, value):
        if len(self.__dict__) >= self.MaxCount:
            raise AttributeError('Много атрибутов')
        else:
            self.__dict__[key] = value

    def __add__(self, other):
        if type(other) == type(self):
            self.value += other.value
        elif isinstance(other, (int, float)):
            self.value += other
        return self

    def __sub__(self, other):
        if type(other) == type(self):
            self.value -= other.value
        elif isinstance(other, (int, float)):
            self.value -= other
        return self

    def __mul__(self, other):
        if type(other) == type(self):
            self.value *= other.value
        elif isinstance(other, (int, float)):
            self.value *= other
        return self

    def __floordiv__(self, other):
        if type(other) == type(self):
            self.value //= other.value
        elif isinstance(other, int):
            self.value //= other
        return self

    def __truediv__(self, other):
        if type(other) == type(self):
            self.value /= other.value
        elif isinstance(other, (int, float)):
            self.value /= other
        return self

    def __pow__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value ** value)

    def pow(self, *args):
        for x in args:
            self.value **= x
        return self

    def add(self, *args):
        self.value += sum(args)
        return self

    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.__dict__)

    def __iter__(self):
        return self.value


if __name__ == '__main__':
    calculator = Calculator(100)
    for y in calculator:
        print(y)
    print(calculator)
    calculator.faqZXCAS = 0
    calculator.faq2XCZX = 1
    calculator.faqCAS = 2
    calculator.faq2ZXCAS = 3
    calculator.faqZXFA = 4
    calculator.faq2ASD = 5
    calculator.faqasf = 6
    calculator.faq2asda = 7
    calculator.faqfasf = 8
    calculator.faq2saf = 9
    calculator.faq2df = "asds"
