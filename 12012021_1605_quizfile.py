f = open("quiz_question_database.txt", "r")

for line in f:
    fields = line.split("|")
    
question = fields[0]
correct_answer = fields[1]
wrong_answer1 = fields[2]
wrong_answer2 = fields[3]
wrong_answer3 = fields[4]
tags = fields[5]

print(fields[0])
