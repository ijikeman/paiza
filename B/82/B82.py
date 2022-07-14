"""
あなたは、溜まった有給休暇を利用し、長期旅行を計画しています。
あなたは、今後 N 日についての日程、すなわち、各日が出勤日であるか、休みであるかわかっています。
下図は、入力例 1 における日程を表しています。

あなたが持っている M 日分の有給休暇を利用した、最長の連休日数の出力してください。
入力例 1 では、有給休暇を M = 3 日利用できるので、下図のように有給休暇を取ると連続する休みの日の数が最大化できます

この場合、2 日から 7 日までの合計 6 日間が連続する休みとなるので、6 と出力してください。

有給休暇を利用したときの、最長の連休日数を出力してください。

入力例1
10 3
work
off
off
work
work
work
off
work
work
off
出力例1
6
"""
import logging
import sys
logger = logging.getLogger(__name__)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)
# ロガーのログレベルをWARNINGに設定する
logger.setLevel(logging.INFO)

sys.path.append("../..//libs/") ## paiza
import data ## paiza
# import paiza ## debug
import vscode as paiza ## debug

class B82():
    # offが連続何回なのか計算する
    def keisan(self):
        pass

    # 現在値と最大値を比較して最大値を超えていれば書き換える
    # スキップカウントをあげていく
    def hikaku(self):
        pass

    # 渡された最大数分だけ配列のworkをoffに書き換える
    def kakikae(self, convert_num):
        pass

    # workの数をカウントする
    def count_work_day(seelf):
        pass
    
    # holiday - work_numがloop実行回数
    # 書き換えskipカウントをあげていく
"""
Main
"""
first_line = paiza.ValueData()
first_line.set()
logger.info(first_line.get())
set_num, key_num = first_line.get().split(" ")

data_array = paiza.ArrayData()
data_array.sets(int(set_num))
data_array.set() ### debug ## 行が１行足りない
data_array.pop() ### debug ## 先頭行を削除

# b81クラスのインスタンス化
b82 = B82()
