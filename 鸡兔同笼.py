while True:
    num = int(input("1为继续，2为退出："))
    if num == 1:
        a = int(input("请输入头数："))
        b = int(input("请输入脚数："))
        c = int(input("请设定鸡的脚数："))
        d = int(input("请设定兔的脚数："))
        num1 = a * c
        num2 = b - num1
        num3 = d - c
        num4 = num2 / num3
        num5 = a - num4
        print(f"兔数为{num4}，鸡数为{num5}")
    if num == 2:
        break