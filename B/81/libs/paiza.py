class paizaData:
    def __init__(self):
        self.data_array = []

    def set_data(self, num):
        for i in range(num):
            self.data_array.append(input())

    def get_data(self, num):
        return self.data_array[num]
