import sys
sys.path.append("./libs/")
import paiza

class B81():
    def __init__(self):
        self.__score = 0
    
    def judge(self, before, current, upper, vertical, vertical_max):
        if vertical == 0:
            self.__score+=1
        elif vertical == vertical_max:
            self.__score+=1

# インスタンス化
paiza_data = paiza.paizaData()

# 最初の行を取得し、スペースで分割
paiza_data.set_data(1)
vertical_max, horizontal_max = paiza_data.get_data(0).split(" ")

b81 = B81()

# 縦の行数分データを取得
for vertical in range(int(vertical_max)):
    paiza_data.set_data(1)
    current_line = list(paiza_data.get_data(vertical + 1)) # 最初の行は省く必要ので+1、1文字ずつ分割
    for horizontal in range(int(horizontal_max)):
        current = current_line[horizontal]
        if horizontal == 0:
            before = ''
        else:
            before = current_line[horizontal - 1]

        if vertical == 0:
            upper = ''
        else:
            upper = list(paiza_data.get_data(vertical))[horizontal]

        b81.judge("before=" + before + ", current=" + current + ", uppper=" + upper + "END", vertical, vertical_max)

# paiza = Paiza.Input()
# paiza.getInput()

# # paiza = lib.paiza.Paiza.Input()
# # print(paiza)
# paiza = Paiza()
# paiza.get_data()
# print(paiza.input_data)
