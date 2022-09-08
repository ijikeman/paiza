from data import *
import sys

class ValueData(ValueData):
    def __init__(self):
        super().__init__()
        self.fp = open(sys.argv[1])

    def get(self):
        return super().get()
    
    def set(self):
        super().set(self.fp.readline().rstrip())

class ArrayData(ArrayData):
    def __init__(self):
        super().__init__()
        self.fp = open(sys.argv[1])

    def get(self, num):
        return super().get(num)
    
    def set(self):
        super().set(self.fp.readline().rstrip())

    def sets(self, num):
        for i in range(num):
            super().set(self.fp.readline().rstrip())

    def pop(self):
        try:
            return super().pop()
        except:
            return False
