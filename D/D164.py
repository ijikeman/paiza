
input_line = input()
tmp=int(input_line)

while True:
    if (tmp > 2):
        result = tmp / 2
        if (result % 2 == 0):
            tmp=result
        else:
            print("NG")
            break
    else:
        if (tmp % 2 == 0):
            print("OK")
            break
        else:
            print("NG")
            break
