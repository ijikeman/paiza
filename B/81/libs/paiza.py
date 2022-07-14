from data import *

class PaizaValueData(ValueData):
    def set(self):
        super().set(input())

class PaizaArrayData(ArrayData):
    def set(self):
        super().set(input())

    def sets(self, num):
        for i in range(num):
            super().set(input())
