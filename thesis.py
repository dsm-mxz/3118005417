def thesis(words):
    tad = {}  # 创建一个空字典来存放次数
    for e in words:  # 遍历文章中的每个词语，并输出重复的的次数
        tad[e] = 0

    for e in words:
        tad[e] += 1

    return tad


if __name__ == '__main__':
    w = ["我", "是", "谁"]
    thesis(w)
