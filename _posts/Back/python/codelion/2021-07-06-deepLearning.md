---
layout: single
title: "딥러닝 - 자연어 처리"
categories : 
    - Deep Learning
---

    1. Back of Word
    2. N - Gram
    3. TF-IDF
        - TF 
            - 출현빈도 / 단어종류로 판단
        - IDF
            - Log()
            - 문서와 연관성이 없는 단어 삭제 (a, is ...)
        - TF 단어 갯수

    4. TF-IDF Back of Word
        - 장점
        - 구현하기가 쉽다
        - 중요한단어 점수 유지
        - 자주 출연하는 불용어 점수 낮춰줌

        - 단점
        - 단어는 알되 속뜻은 모름
        - 다른 단어인데 같은 뜻인 경우를 못잡아냄

        - 극복 방법
            - LSA(Latent Semantic Analysis)
            - Word Embeddings(Word2Vec, Glove)
            - ConceptNet


---

1. Euclidean Distance Similarity



2. Cosine Similarity