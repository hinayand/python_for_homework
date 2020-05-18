while True:
    num = int(input("请输入命令，1为长方形，2为正方形，3为退出:"))
    if num == 1:
        a = int(input("请输入长："))
        b = int(input("请输入宽："))
        c = a * b
        print(f"面积为{c}")
    if num == 2:
        a = int(input("请输入边长："))
        b = a
        c = a * b
        print(f"面积为{c}")
    if num == 3:
        break