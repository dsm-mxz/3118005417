import random
from fractions import Fraction



# 生成分数的fra函数
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


# 中缀表达式转成后缀表达式
def middle2behind(exp):
    result = []  # 结果列表
    stack = []  # 栈
    for item in exp:
        if isinstance(item, Fraction):  # 判断传进来的表达式的每个元素是否与分数是同一类型
            result.append(item)
        else:  # 如果当前字符为一切其他操作符
            if len(stack) == 0:  # 如果栈空，直接入栈
                stack.append(item)
            elif item in '×÷(':  # 如果当前字符为×÷（，直接入栈
                stack.append(item)
            elif item == ')':  # 如果右括号则全部弹出（碰到左括号停止）
                t = stack.pop()
                while t != '(':
                    result.append(t)
                    t = stack.pop()
            # 如果当前字符为加减且栈顶为乘除，则开始弹出
            elif item in '+-' and stack[len(stack) - 1] in '×÷':
                if stack.count('(') == 0:  # 如果有左括号，弹到左括号为止
                    while stack:
                        result.append(stack.pop())
                else:  # 如果没有左括号，弹出所有
                    t = stack.pop()
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                    stack.append('(')
                stack.append(item)  # 弹出操作完成后将‘+-’入栈
            else:
                stack.append(item)  # 其余情况直接入栈（如当前字符为+，栈顶为+-）

    # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
    while stack:
        result.append(stack.pop())
    # 返回列表
    return result


# 后缀表达式的计算
def calculate_postfix(postfix):
    """
    calculate postfix expression
    :param postfix: postfix expression str, like '23x83/+'
    :return: int result, like 2x3+8/3=6+2=8
    """
    stack2 = []  # 用list模拟栈的后进先出
    for p in postfix:
        if not isinstance(p, Fraction):  # 判断传进来的参数是否与分数不为同一类型
            value_2 = stack2.pop()  # 第二个操作数
            value_1 = stack2.pop()  # 第一个操作数
            if p == '+':
                result = value_1 + value_2
            elif p == '-':
                result = value_1 - value_2
            elif p == '×':
                result = value_1 * value_2
            else:  # 除法
                if value_2 == 0:  # 当分母为0时，会报错，所以设置条件使得程序重新生成题目
                    return -1
                result = value_1 / value_2  # 由于传进来的数值为分数，所以这里不能用整除
            if result < 0:  # 如果计算过程中出现负值，则需要返回进行判断并且重新生成题目
                return result
            stack2.append(result)
        else:
            stack2.append(p)
    return stack2.pop()


# middle2behind(list_expression)
# ans = calculate_postfix(middle2behind(list_expression))


# 判断数值类型，如果小于1大于0则输出真分数格式，如果大于1且不为整数，则输出带分数格式，否则为整数
def str_frac(each):
    num = int(each)
    frac = each - num
    if frac == 0 or num == 0:
        return str(each)
    else:
        return str(num) + "'" + str(frac)


# 生成题目的道数以及题目里的值
def generate_problem_list(count, r):
    dict1 = {}
    problem_list = {}

    while count:
        str1 = ''
        problem = generate_problem(r)
        # print(problem)
        pre = middle2behind(problem)
        # print(pre)
        res = calculate_postfix(pre)
        if res < 0:  # 出现负数，则重新生成
            continue
        # 判断结果是否出现重复
        if res not in dict1:
            dict1[res] = 1
            count -= 1
            # problem_list.append(problem)
            for each in problem:
                if each in ['+', '-', '×', '÷']:
                    str1 = str1 + ' ' + str(each) + ' '
                elif each == '(' or each == ')':
                    str1 = str1 + str(each)
                else:
                    str1 = str1 + str_frac(each)

            problem_list[str1] = str_frac(res)

        # count--

    return problem_list

# print(generate_problem_list(5, 15))
