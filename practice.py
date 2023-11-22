# 숫자, 문자
print("v"*9)

#bool
print(5>10)
print(True)
print(not False)
print(not (5>10))

#변수
animal = "강아지"
name = "연탄"
age = 4
is_adult = age >= 3

print("우리집" + animal + "의 이름은" + name + "예요")
print(name + "는" + str(age) + "살이며" )
print(name + "는 어른일까요 ? " + str(is_adult))

#연산자 
print(3+2)
print(5*2)
print(6/3)
print(2**3)
print(5%3)
print(10//3)

print(4 >= 7)
print(10 < 3)
print(5 > 2)
print(4 == 4)
print(3 + 4 !=7)
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 2))
print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))
print( 5>4>7)

#간단한 수식
print(2+3*4)
print((2+3)*4)

number = 2+3
number *= 2 
print(number)

#숫자 처리 함수
print(abs(-5)) #절댓값
print(pow(4,2)) #제곱 
print(max(5, 12))#최댓값
print(min(5, 12))#최솟값
print(round(3.14))#반올림
print(round(4.99))

from math import *
print(floor(4.99))#내림
print(ceil(3.14))#올림
print(sqrt(16))#제곱근

#랜덤함수
from random import *

print(random())
print(random() * 10 )
print(int(random() * 10))
print(randrange(1, 45)) #1~45 미만의 임의의 값 생성 

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매일" + str(date) + "일로 선정되었습니다.")

#문자열
sentence = "나는 소년입니다"
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요 
"""
print(sentence3)

#슬라이싱
jumin = "990120-1234567"
print("성별: " + jumin[7])
print("연: " + jumin[0:2]) #0부터 2직전까지
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])
print("생년월일 : " + jumin[:6]) #처음부터 6 직전까지 
print("뒤 7자리: " + jumin[7:]) #7 부터 끝까지
print("뒤 4자리 (뒤에부터): " + jumin[-4:]) #맨 뒤에서 4번쨰부터 끝까지

python = 'Python is Amazing'
print(python.lower()) #소문자 
print(python.upper()) #대문자 
print(python[0].isupper()) #첫번째 문자가 대문자인지 
print(len(python))#길이반환
print(python.replace("Python", "Java")) #문자 변환 

index = python.index("n")
print(index)
print(python.find("Java")) #find에서 원하는 값이 없을 시 -1반환
# print(python.index("Java")) #index에서 원하는 값이 없을 시 오류
print(python.count("n")) #횟수 

#문자열 포맷
print("a"+ "b")
print("a", "b")

#방법 1
print("나는 %d살입니다" %20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살 입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간"))

#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

#방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자
print("백문이 불여일견\n백견이 불여일타") #줄바꿈 
print("저는'나도코딩'입니다") #\" 문장 내에서 따옴표 
print("저는 \"나도코딩\"입니다.")

#\\ : 문장 내에서 \
print("C:\\Users\\minseo\\Desktop\\pythonWorkspace>")

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

#\b: 백스페이스(한 글자 삭제)
print("Redd\bApple")

#\t: 탭 
print("Red\tApple")

