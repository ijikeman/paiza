from data import *

# class PaizaValueData(ValueData): ## paiza
class ValueData(ValueData): ## paiza
    def set(self):
        super().set(input())

# class PaizaArrayData(ArrayData): ## paiza
class ArrayData(ArrayData): ## paiza
    def set(self):
        super().set(input())

    def sets(self, num):
        for i in range(num):
            super().set(input())
