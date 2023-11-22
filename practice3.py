#조건문

wether = input("오늘 날씨는 어떄요?")
if wether == "비" or wether == "눈":
    print("우산을 챙기세요")

elif wether =="미세먼지":
    print("마스크를 챙기세요")

else:
    print("준비물 필요 없어요")    


temp = int(input("기온은 어떄요?"))
if 30 <= temp:
    print("덥다")
elif 10 <= temp < 30:
    print("괜찮다")
elif 0 <= temp < 10:
    print ("외투를 챙기세요")
else:
    print("너무 춥다")            

