from shengcheng import *
import sys

# 命令行参数
n = int(sys.argv[2])
r = int(sys.argv[4])

exercises_file = open("Exercises.txt", "w", encoding="utf-8")
answers_file = open("Answers.txt", "w", encoding="utf-8")

problem_list = generate_problem_list(n, r)

# 生成题号以及规范格式
count = 1
for eachKey in problem_list.keys():
    exercises_file.write(str(count) + '. ' + eachKey + ' = ' + '\n')
    answers_file.write(str(count) + '. ' + problem_list[eachKey] + '\n')
    count += 1

exercises_file.close()
answers_file.close()
