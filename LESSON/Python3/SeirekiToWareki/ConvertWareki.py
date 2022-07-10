import sys

class Validation:
    # intかどうか
    @staticmethod
    def CheckInt(param):
        return isinstance(param, int)

class ConvertWareki:
    @staticmethod
    def __GetKeyYear(year):
        if 2019 < year:
            return [2018, "令和"]
        elif 1989 < year:
            return [1988, "平成"]
        elif 1926 < year:
            return [1925, "昭和"]

    @classmethod
    def Convert(cls, year): # GetKeyYearを呼ぶ為にクラスメソッドにしている
        if Validation.CheckInt(year):
            key_year, key_wareki = cls.__GetKeyYear(year)
            if (year < key_year):
                raise (ValueError)
            else:
                return [year - key_year, key_wareki]
        else:
            raise (TypeError)

try:
    print(ConvertWareki.Convert(int(sys.argv[1])))
except Exception as e:
    print(e)
