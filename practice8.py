#표준 입출력
print("Python", "Java", sep=",",end="?")
print("무엇이 더 재밌을까요?")
print("Python", "Java", sep="vs")

import sys
print("Python", "Java", file=sys.stdout)


scores = {"수학":0, "영어": 50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))   

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은" + answer + '입니다.')     

answer = 10
print(type(answer))