# 两个变量值互换。
def change(a, b):
    a, b = b, a
    return a, b


a = int(input("请输入数字："))
b = int(input("请输入数字："))
print(change(a, b))


