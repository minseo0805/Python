#기본값

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}")\
        # .format(name, age, main_lang)

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")

#키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")


#가변 인자
def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
         print(lang, end=" ")
    print()     

profile('유재석', 20, "Python", "Java", "C", "C++", "C#", "Javascript")
profile('김태호', 25, "Kotlin", "Swift", "", "", "") 

#지역변수와 전역변수
gun = 10#지역변수 

def checkpoint(soldiers):
    global gun#전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내]남은 총:{0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint(2)
print("남은 총: {0}".format(gun))


gun = 10#지역변수 

def checkpoint(soldiers):
    global gun#전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내]남은 총:{0}".format(gun))

def chechpoint_ret(gun, soidiers):
    gun = gun - soidiers
    print("[함수 내] 남은 총 :{0}".format(gun))
    return gun    

print("전체 총: {0}".format(gun))
# checkpoint(2)
gun = chechpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))


def std_weigt(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weigt(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
