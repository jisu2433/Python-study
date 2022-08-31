def grader(s,a):
    student_dict = dict()
    for grade in s :
        student_name = grade.split(',')[0]
        student_answer = list(grade.split(',')[1])
        student_score = []
        for(x,y) in zip(a,student_answer):
            if str(x) == y:
                student_score.append(1)
            else :
                student_score.append(0)
        student_dict[student_name] = int(sum(student_score)/len(student_score)*100)
    sorted_student_dict = sorted(student_dict.items(), key = lambda item : item[1] , reverse=True)
    for(x,y), z in zip(sorted_student_dict, range(1,len(sorted_student_dict))+1):
        print(f"학생 : {x} 점수 : {y}점 {z}등")
# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

grader(s,a)
