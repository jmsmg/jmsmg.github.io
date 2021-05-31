import random
import time

jungle = ["엘리스", "리신", "이블린", "람머스"] # 리스트

while True:     #추가부분
    print(jungle)
    item = input("캐릭터를 추가해주세요 : ")
    if(item == "q"):
        break
    else:    
        jungle.append(item)
print(jungle)

set_jungle = set(jungle)    #리스트를 집합화
while True:     #삭제는 집합을 활용하였음
    print(set_jungle)
    item = input("캐릭터를 삭제해주세요 : ")
    if(item == "q"):
        break
    else:
        set_jungle = set_jungle - set([item]) #item(변수)을 리스트화한 후 집합화

print(set_jungle, "중에서 선택합니다.")

print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print(random.choice(list(set_jungle)))