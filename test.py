class A:
    def __init__(self):
        pass

    def __eq__(self, other):
        return "hello overloading"


a = A()
b = A()
