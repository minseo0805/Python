#파일 입출력
score_file = open("score.txt", "w", encoding="utf-8")
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf-8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close


# score_file = open("score.txt", "r", encoding="utf-8")
# lines = score_file.readline()
# for line in lines:

# score_file.close()