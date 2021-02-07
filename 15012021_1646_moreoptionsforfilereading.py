f = open("quizdatabase.txt", "r")



text_lines = []


for line in f:
    fields = line.split("|")
    #print(fields)
    text_lines.append(fields)
    
question = fields[0]
correct_answer = fields[1]
wrong_answer1 = fields[2]
wrong_answer2 = fields[3]
wrong_answer3 = fields[4]
tags = fields[5]

#print(fields[0:6])
#print(fields[1])
#print(fields)

print(text_lines[0][1].split(" ")[1])
