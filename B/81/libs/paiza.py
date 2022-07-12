class paizaData:
    def __init__(self):
        self.__data_array = []

    def set_data(self, num):
        for i in range(num):
            self.__data_array.append(input())

    def get_data(self, num):
        return self.__data_array[int(num)]
