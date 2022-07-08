import sys

# intかどうか
def ValidationInt(argument):
    return isinstance(argument, int)

# 平成年に変換
def ConvertToHeisei(year):
    if ValidationInt(year):
        return year - 1989
    else:
        return False

# Int型に変換
def ConvertToInt(param):
    try:
        return int(param)
    except:
        print('[ERROR]: Convert Error')
        return False

def StdoutHeisei(dict):
    # 変換されたデータを出力
    for key in dict:
        if dict[key] == False:
            print(str(key) + "は変換できませんでした")
        else:
            print("西暦" + str(key) + "年は", end="")
            print("平成" + str(dict[key]) + "年です。")

# Main
datas={} # 変換データ保存

# 入力行を全て変換する
# ただし、0番目はプログラムパスなので省く
for i in range(1, len(sys.argv)):
    # Intに変換
    int_argument = ConvertToInt(sys.argv[i])
    # 変換できない場合はValueにFalse
    if int_argument == False:
        datas[sys.argv[i]] = False
    else:
        datas[int_argument] = ConvertToHeisei(int_argument)

StdoutHeisei(datas)