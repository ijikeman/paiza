from abc import ABCMeta, abstractclassmethod

class Data(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def get(self):
        pass

    @abstractclassmethod
    def set(self):
        pass

class ValueData(Data):
    def __init__(self):
        self.__data = ''

    def get(self):
        return self.__data

    def set(self, value):
        self.__data = value

class ArrayData(Data):
    def __init__(self):
        self.__data = []

    def get(self, num):
        return self.__data[int(num)]
    
    def set(self, value):
        self.__data.append(value)

    def sets(self, *value):
        self.__data.extend(value)

    def pop(self):
        return self.__data.pop(0)

class HashData(Data):
    def __init__(self):
        self.__data = {}
    
    def get(self, key):
        return self.__data[key]
    
    def set(self, key, value):
        self.__data[key: value]

class PaizaValueData(ValueData):
    def set(self):
        super().set(input())

class PaizaArrayData(ArrayData):
    def set(self):
        super().set(input())

    def sets(self, num):
        for i in range(num):
            super().set(input())

import logging
import sys
logger = logging.getLogger(__name__)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)
# ロガーのログレベルをWARNINGに設定する
logger.setLevel(logging.WARNING)

#最初の行データをインスタンス化
first_line = PaizaValueData()
first_line.set()
logger.debug(first_line.get())

data = PaizaValueData()
data.set()
array = []
array = data.get().split(" ")
sum = 0
for num in array:
  sum += int(num)

print(sum)
