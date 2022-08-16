# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

def grader(s,a):
    nameList= []
    scoreList = []
    grade= 0
    for answers in s:
        score = 0
        name, answer = answers.split(',')
        nameList.append(name)
        answerList = list(answer)
        for i in range(len(answerList)):
            if int(answerList[i]) == a[i]:
                score+=1
                scoreList.append(score)
        print(f'학생: {name} 점수:{score*10}점')

grader(s,a)

