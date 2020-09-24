import jieba  # 导入结巴中文分词库
import math
import sys  # 导入命令行参数模块
from test1.thesis import thesis

# 命令行参数
txt1_file = open(sys.argv[1], 'r', encoding='utf-8')
txt2_file = open(sys.argv[2], 'r', encoding='utf-8')
answer = open(sys.argv[3], 'w', encoding='utf-8')

txt1 = txt1_file.read()
txt2 = txt2_file.read()

# 通过结巴库中的的精准模式对文本进行分词,并返回一个列表形式
words1 = jieba.lcut(txt1)
words2 = jieba.lcut(txt2)

# 调用thesis函数，并分别存放两篇文章词语的次数
dict1 = thesis(words1)
dict2 = thesis(words2)

# 运用余弦相似度算法进行重复率的计算
t = 0
for each in dict1:
    if each in dict2:
        t += dict1[each] * dict2[each]

m = 0
for each in dict1:
    m += dict1[each] ** 2

n = 0
for each in dict2:
    n += dict2[each] ** 2

cos = t / (math.sqrt(m) * math.sqrt(n))

answer.write(str(cos))
print(cos)

print('参数个数为:', len(sys.argv), '个参数。')
print('参数列表:', str(sys.argv))
