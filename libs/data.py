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

    def sets(self, value):
        self.__data.extend(value)

    def pop(self):
        return self.__data.pop(0)

    def get_count(self):
        return len(self.__data)

class HashData(Data):
    def __init__(self):
        self.__data = {}
    
    def get(self, key):
        return self.__data[key]
    
    def set(self, key, value):
        self.__data[key: value]
