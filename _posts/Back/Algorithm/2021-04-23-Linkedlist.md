---
layout: single
title:  "3. Algorithm - Array and String"
categories : 
    - Algorithm
---

## Linked List
---

1. Linked List 개념
   
* DATA에 다음 NODE의 주소를 가지고 있는 형태
  
* Linked List는 배열과 비교 가능

> 장점: 자료가 연결된 구조여서 크기가 정해지지 않은 자료를 구현할때 용이

> 단점 : 자료 흐름을 타고 가야하여 느림
    
    📢 상반된 개념 : 배열

---

2. Linked List 종류

 * 단방향 : 다음 Data의 Node값만 가지고 있음(헤더 주소 하나만 가지고 있음)
  
 * 양방향 : 이전 Data, 다음 DATA의 Node값을 모두 가지고 있음(양쪽 끝에 포인터를 가지고 있음)
  
    ※ 편집할때 A - B - C // B가 가진 Node 값을 A와 C에게 물려줌 

---

3. Linked List 구현
   
    ~~~java
    class Node{
        int datai 
        Node next = null
        
    }
    ~~~
