from data import *

class PaizaValueData(ValueData):
    def set(self):
        self.data = input()

class PaizaArrayData(ArrayData):
    def set(self):
        self.data.append(input())

    def sets(self, num):
        for i in range(num):
            self.data.append(input())
