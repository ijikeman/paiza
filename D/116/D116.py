import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../libs")) # ディレクトリ移動
import data # 格納用
import vscode as paiza # input用

input_data = paiza.ArrayData()
input_data.sets(2) # 2行分取得

convert_data = data.ArrayData() # 変換用
convert_data.sets(input_data.get(1).split()) # 2行目をsplit

sum = 0
for i in range(int(convert_data.get_count())): # countでループ
    sum += int(convert_data.get(i)) # 足し算

print(sum)
