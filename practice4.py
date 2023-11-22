# for wating_no in [0,1,2,3,4]:
#     print("대기번호: {0}".format(wating_no))

for waiting_no in range(1, 6):
    print("대기번호: {0}".format(waiting_no))    

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for cusomer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(cusomer))

 #while
customer = "토르"
index =5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번남았어요.".format(cusomer,index))
    index -= 1
    if index ==0:
        print("커피는 폐기처분되었습니다.")

# cusomer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(cusomer,index))
#     index +=1



cusomer = "토르"
person = "Unknown"

while person != cusomer:
    print("{0}, 커피가 준비 되었습니다.".format(cusomer))
    person = input("이름이 어떻게 되세요? ")

absent = [2, 5] #결석
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

     