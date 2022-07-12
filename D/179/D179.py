"""
分ける人数 n とお菓子の個数 m が改行区切りで与えられるので余ったお菓子の数を出力してください。

末尾に改行を入れ、余計な文字、空行を含んではいけません。
"""

class paizaData:
    def __init__(self):
        self.data_array = []

    def set_data(self, num):
        for i in range(num):
            self.data_array.append(input())

    def get_data(self, num):
        return self.data_array[num]

paiza_data = paizaData()
paiza_data.set_data(2)
print(int(paiza_data.get_data(1)) % int(paiza_data.get_data(0)))
