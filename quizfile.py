from os import path


dir = path.dirname(__file__)
data_dir = path.join(dir, 'data')
quiz_database = path.join(data_dir, 'quizdatabase.txt')

f = open(quiz_database, "r")

for line in f:
    fields = line.split("|")

question = fields[0]
correct_answer = fields[1]
wrong_answer1 = fields[2]
wrong_answer2 = fields[3]
wrong_answer3 = fields[4]
tags = fields[5]

print(fields[0])
