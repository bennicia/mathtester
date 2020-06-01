def checkanswer(answer):
    userAns = input('your answer: ').upper()
    if userAns == answer:
        results.append(1)
    else:
        results.append(0)
level = input('What level would you like 1 (HARD multiplication), 2 (make(x)the subject), multiple choice questions 3 of H (help) ')
if level.strip() == '1':
    f = open('data 1')
elif level.strip() == '2':
    f = open('data 2')
elif level.strip() == '3':
    f = open('data 3')
else :
    f = open('data 4')

results = []

answers = []

for line in f:
    data = (line.strip().split(","))
    print(data[0])

    checkanswer(data[0])
    answers.append(data[0])

print(results)

total = 0
for i in range(len(results)):
    score = results[i]
    if score == 0:
        print("question", i + 1, "was wrong. the corect answer was", answers[i])
    else:
        print("question", i + 1, "was corect")
    total = total + score

print("your total score was", total, '/ 8')
