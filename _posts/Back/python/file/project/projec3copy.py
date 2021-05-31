total_dictionary = {}

while True:
    key = input ("키값 입력하세요 : ")
    if (key == 'q'):
        break
    else:
        total_dictionary [key] = ""

for i in total_dictionary:
    print(i)
    key = input ("밸류값") #입력
    total_dictionary[i] = key #대입

print(total_dictionary) #출력문