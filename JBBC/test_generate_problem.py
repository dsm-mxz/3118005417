import random
from fractions import Fraction


def fra(r):
    zi = random.randint(1, max(10, r))  # 分子
    mu = random.randint(1, max(10, r))  # 分母
    return Fraction(zi, mu)


# 生成一道题目的函数
def generate_problem(r):
    list_op = ['+', '-', '×', '÷']
    list_expression = []
    fq = random.randint(1, 3)  # 随机生成符号的次数
    while fq:
        number = fra(r)
        op = random.choice(list_op)
        list_expression.append(number)
        list_expression.append(op)
        fq -= 1
    number1 = fra(r)
    list_expression.append(number1)

    # 判断括号是否需要插入以及插入的位置
    brackets = random.randint(0, 1)
    length = len(list_expression)
    cnt = (length + 1) / 2
    if brackets == 1:
        if length == 5 or length == 7:
            L = random.randint(1, cnt - 1)
            R = random.randint(L + 1, cnt)
            L = 2 * L - 2
            R = 2 * R
            # print("L: " + str(L))
            # print("R: " + str(R))
            # print(list_expression)
            list_expression.insert(L, '(')
            list_expression.insert(R, ')')

    return list_expression


for each in range(10):
    a = generate_problem(20)
    print(a)
