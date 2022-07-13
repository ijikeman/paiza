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
        self.data = ''

    def get(self):
        return self.data

    def set(self, value):
        self.data = value

class ArrayData(Data):
    def __init__(self):
        self.data = []

    def get(self, num):
        return self.data[int(num)]
    
    def set(self, value):
        self.data.append(value)

    def sets(self, *value):
        self.data.extend(value)

class HashData(Data):
    def __init__(self):
        self.data = {}
    
    def get(self, key):
        return self.data[key]
    
    def set(self, key, value):
        self.data[key: value]
