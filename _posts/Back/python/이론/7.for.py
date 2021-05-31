for x in range(30):
    print(x)

foods = ["된장찌개","피자","제육볶음"] # list의 for문
for x in range(3):
    print(foods[x])

for x in foods: # foods(list) 길이만큼 반복
    print(x)

# dictionary의 for문
information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
for x, y in information.items():
    print(x)
    print(y)