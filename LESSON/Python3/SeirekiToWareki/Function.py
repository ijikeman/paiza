import sys

# intかどうか
def ValidationInt(argument):
    return isinstance(argument, int)

def ConvertToHeisei(year):
    if ValidationInt(year):
        return year - 1989
    else:
        return False

def ConvertToInt(param):
    try:
        return int(param)
    except:
        print('[ERROR]: Convert Error')
        return False

# main
datas={}
for i in range(1, len(sys.argv)):
    int_argument = ConvertToInt(sys.argv[i])
    if int_argument == False:
        datas[sys.argv[i]] = False
    else:
        datas[int_argument] = ConvertToHeisei(int_argument)

for key in datas:
    if datas[key] == False:
        print(str(key) + "は変換できませんでした")
    else:
        print("西暦" + str(key) + "年は", end="")
        print("平成" + str(datas[key]) + "年です")
