
---

## 파이썬

---
 1. IDE = integrated development envirment(통합개발환경)

 visual studio code
 sublime text 3(4)

 2. 핵심 라이브러리 
    * Numerical Python : 산술연산 빠르게(-> 행렬 연산)

    * panel-data & Series(pandas) : 정형데이터(엑셀) 핸들링

    * Matrix Plotting Library(matplotlib) : 행렬데이터를 기반으로 차트를 그려줌(데이터 시각화)
    
    * Scipy : 과학계에서 활용
    
---

1. 문법 
   1. str 변수
        * f 스트링

        * {} ()

        * %d

   2. 괄호
        * temp(~~~) # X로 주면서 temp함수를 호출한다


        * temp[] # 그룹형 변수인 temp로부터 ???에 해당하는 값을 꺼낸다
            * index number : str / list / tuple / numpy.array() # 수치행렬

            * key : dict / pandas.DataFrame() # 엑셀 파일과 같은 정형 프레임

            * temp[0:4] #~이상 ~ 미만
            ``` python
            temp = 'Python'
            temp[0:4]
            'Pyth'
            ```
            * matrix [ , , ] # numpy.array() 수치행렬