#출석번호가 1, 2, 3, 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

#학생 이름을 길이로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [len(i) for i in student]
print(student)

#학생 이름을 대문자로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [i.upper() for i in student]
print(student)

from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 14:
        print("[0]{0}번쨰 손님 (소요시간: {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i,time))
print("총 탑승 승객: {0}분".format(cnt))

