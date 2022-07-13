import sys
sys.path.append("./libs/")
import paiza

"""
判定した数値を返す
[条件]
-- 全ての行で判定する -- 
current=#
  before=. 1
  before="" !
  before=# 0

current=. 
  before=. 0
  before="" 0
  before=# 1

vertical=0 or max
  current=# 1

vertical !=0 and !max
  current=# and upper=. 1

中間業と最終行
current=. and upper=# 1
current=# and upper=. 1
"""
class B81(paiza.ValueData):
    def __init__(self):
        self.data = 0

    def judge(self, before, current, upper, vertical, vertical_max):
        print("before=" + before + ", current=" + current + ", upper=" + upper + "END", vertical, vertical_max)

        if current == ".":
            if before == "" or before == ".":
                self.data += 0
            elif before == "#":
                self.data += 1
            
            # 最初の行、最終行以外の行の場合
            if vertical != 0 and vertical != vertical_max:
                # 前の行が#で現在が.の場合
                if upper == "#":
                    self.data += 1

        elif current == "#":
            if before == "" or before == ".":
                self.data += 1
            elif before == "#":
                self.data += 0

            # 最初の行か最終行なら + 1
            if vertical == 0 or vertical == vertical_max:
                self.data += 1

            # 最初の行、最終行以外の行の場合
            if vertical != 0 and vertical != vertical_max:
                # 前の行がなしで現在が#もしくは.の場合
                if upper == "" or upper == ".":
                    self.data += 1

#最初の行データをインスタンス化
first_line = paiza.PaizaValueData()
# 最初の行を取得し、スペースで分割
first_line.set()
vertical_max, horizontal_max = first_line.get().split(" ")

# 花壇データをインスタンス化
kadan_data = paiza.PaizaArrayData()
# 花壇データを取り込み
kadan_data.sets(int(vertical_max))

# b81クラスのインスタンス化
b81 = B81()
# 縦の行数分データを取得
for vertical in range(int(vertical_max)):
    current_line = list(kadan_data.get(vertical)) # 最初の行は省く必要ので+1、1文字ずつ分割して配列に入れる
    # 横の数分データを取得
    for horizontal in range(int(horizontal_max)):
        current = current_line[horizontal]
        # 横の最初ならば前は存在しない
        if horizontal == 0:
            before = ''
        # それ以外は前のデータを取得
        else:
            before = current_line[horizontal - 1]

        # 縦が最初ならば上の行は存在しない
        if vertical == 0:
            upper = ''
        # それ以外は上の行のデータを取得
        else:
            upper = kadan_data.get(vertical - 1)[horizontal]

        # ロジック判定
        b81.judge(before, current, upper, vertical, vertical_max)

print(b81.get())
