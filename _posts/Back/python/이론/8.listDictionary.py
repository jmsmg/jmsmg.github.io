information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
foods = ["된장찌개", "피자", "제육볶음"]
print(information.get("취미"))
information["특기"] = "피아노"
information["사는곳"] = "서울"
del information["좋아하는 음식"] # 삭제 명령어
print(information)
print(len(information)) # 길이 명령어
information.clear() # 리스트 비우기
print(information) 
print(foods[2]) # 리스트 번호에 맞춰 출력
foods.append("김밥")
del foods[1]
print(len(foods))
