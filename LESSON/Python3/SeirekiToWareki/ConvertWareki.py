import sys

class ConvertWareki:
    """
    渡された西暦年から、計算用キーとなる西暦と和暦元号を返す
    return: @計算用西暦, 和暦元号
    """
    @staticmethod
    def __GetParameter(year):
        if 2019 < year:
            return [2018, "令和"]
        elif 1989 < year:
            return [1988, "平成"]
        elif 1926 < year:
            return [1925, "昭和"]

    """
    和暦の年数を計算する
    """
    @classmethod
    def Convert(cls, year): # GetParameterを呼ぶ為にクラスメソッドにしている
        key_year, initial_wareki = cls.__GetParameter(year)
        return [year - key_year, initial_wareki]

try:
    # int型に変換
    input_year = int(sys.argv[1])
    # 和暦を計算
    convert_year, initial_wareki = ConvertWareki.Convert(input_year)
    # 出力
    print("西暦", str(input_year), "年は、" + str(initial_wareki) + str(convert_year) + "年です")
except Exception as e:
    sys.stderr.write(e)
