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
    pass
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

logger.info(data_array.get(9))

# b81クラスのインスタンス化
b82 = B82()
