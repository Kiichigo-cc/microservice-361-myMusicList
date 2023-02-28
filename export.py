f = open("input.txt", "r")
inputs = f.readlines()

f.close()

f = open("output.txt", "w")
f.write("======================\n\n")
f.write("       " + inputs[0] + "\n")
inputs.pop(0)

questions_list = []
question_count = 0
for i in inputs:
    if 'Q.' in i:
        question_count += 1
        questions_list.append(i)
        inputs.remove(i)

print(question_count)
print(inputs)

sublists = []
temp = []
for i in inputs:
    if i[0] == 'A':
        if temp:
            sublists.append(temp)
        temp = []
    temp.append(i)
sublists.append(temp)

print(sublists)

for i in range(question_count):
    f.write("====* Question " + str(i + 1) + " *====\n")
    f.write(questions_list[i])
    for j in sublists[i]:
        f.write(j)
