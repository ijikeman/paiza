import logging
import sys
logger = logging.getLogger(__name__)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)
# ロガーのログレベルをWARNINGに設定する
logger.setLevel(logging.WARNING)

sys.path.append("./libs/") ## paiza
import data ## paiza
# import paiza ## debug
import vscode as paiza ## debug

"""
判定した数値を返す
[条件]
"""
# class B81(ValueData): ## paiza
class B81(data.ValueData):
    def __init__(self):
        super().set(0)

    def judge(self, before, current, upper, vertical, vertical_max, horizontal, horizontal_max):
        logger.debug("before=" + before + ", current=" + current + ", upper=" + upper + "END, vertical=" + str(vertical) + ", vertical_max=" + str(vertical_max) + ", horizontal=" + str(horizontal) + ", horizontal_max=" + str(horizontal_max))
        # 最初の行
        if vertical == 0:
            # 最上部判定
            if current == "#":
                self.__count_up()
                logger.info("upper")
        # 最初の行以外
        else:
            # 上部判定
            if current == "#":
                if upper == ".":
                    self.__count_up()
                    logger.info("up")
            # 下部判定
            elif current == ".":
                if upper == "#":
                    self.__count_up()
                    logger.info("down")
        # 最終行判定を改めて行う
        if int(vertical) == (int(vertical_max) - 1):
            # 最下部判定
            if current == "#":
                self.__count_up()
                logger.info("downnn")

        # 横部判定
        if current == "#":
            # 最左部判定
            if before == "":
                logger.info("left")
                self.__count_up()
            elif before == ".":
                logger.info("left")
                self.__count_up()

            # 最右部判定
            if int(horizontal) == (int(horizontal_max) - 1):
                logger.info("right")
                self.__count_up()
        elif current == ".":
            if before == "#":
                logger.info("right")
                self.__count_up()

    def __count_up(self):
        super().set(super().get() + 1)

"""
Main
"""
#最初の行データをインスタンス化
# first_line = PaizaValueData() ## paiza
first_line = paiza.ValueData() ## paiza
# 最初の行を取得し、スペースで分割
first_line.set()
vertical_max, horizontal_max = first_line.get().split(" ")

# 花壇データをインスタンス化
# kadan_data = PaizaArrayData() ## paiza
kadan_data = paiza.ArrayData() ## paiza
# 花壇データを取り込み
kadan_data.sets(int(vertical_max))
kadan_data.set() ### debug ## 行が１行足りない
kadan_data.pop() ### debug ## 先頭行を削除

# b81クラスのインスタンス化
b81 = B81()
# 縦の行数分データを取得
for vertical in range(int(vertical_max)):
    current_line = kadan_data.get(vertical) # 1行ずつ取得(pythonはsplitしなくても取得できるためsplitしない)
    # 横の数分データを取得
    logger.info(b81.get())
    for horizontal in range(int(horizontal_max)):
        current = current_line[horizontal] # 配列の様に指定すると文字数が取得可能
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
        b81.judge(before, current, upper, vertical, vertical_max, horizontal, horizontal_max)

print(b81.get())
