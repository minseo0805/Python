#리스트 []

subway = [10,20,30]
print(subway)

subway = ["유재석","박명수","조세호"]
print(subway)
print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정현돈")
print(subway)

print(subway.pop())
print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

#같은 이름의 사람이 몇 며 있는지 확인
subway.append("유재석")
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear
print(num_list)

#다양한 자료형 함께 사용 
num_list = [5, 4, 3, 2, 1]
mix_list = ["조세호", 20, True]

#리스트 확장
num_list.extend(mix_list)
print(num_list)

#딕셔너리
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

# print((cabinet.get(3)))
# print(cabinet[5])
# print(cabinet.get(5))
# print("hi")

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys()) #key 들만 출력

print(cabinet.values()) #value 들만 출력

print((cabinet).items()) #key, value 쌍으로 출력

cabinet.clear
print(cabinet)

#튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")

#집합 (set)
#중복 안됨, 순서 없음 
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 
print(java & python)
print(java.intersection(python))

#합집합 
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 잊음 
java.remove("김태호")
print(java)

#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

