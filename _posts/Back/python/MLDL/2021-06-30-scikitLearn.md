---
layout: single
title: "머신러닝 - Scikit-learn"
categories : 
    - Machine Learning

---

# scikit learn 순서
1. 데이터셋 불러오기
    - sklearn.datasets.load_&#91;DATA&#93;()
    - X, Y 가르기(Pandas 활용)
    - 열의 종류에 따라 Feature Normalization(scaling) 작업 진행
        > Numeric(Continuous) Column(Variable) -> Min-Max Algorithm or Standardization  1
        > Categorical(Discontinuous) Column(Variable) -> one-hot encoder

2. Train/Test set
    - sklearn.model_selection.train_test_split(X,Y,test_size)
        ```python
        from sklearn import model_selection
        ```

3. 모델객체 (Model Instance) 생성하기  
      - model =  
          - sklearn.linear_model.LinearRegression()  
          - sklearn.linear_model.LogisticRegresion()  
          - sklearn.neighbor.KNeighborsClassifier(n_neighbors)  
          - sklearn.cluster.KMean(n_clusters)  
          - sklearn.decomposition.PCA(n_components)  
          - sklearn.svm.SVC(kernel, C, gamma)  

4. 모델 학습시키기 (Model fitting)
    - model.fit(x_train, y_train)

5. 모델로 새로운 데이터 예측하기 (predict on test data)
    - model.fit(x_train, y_train)
        > y = a * x + b  
        > coefficients == a, intercepts == b
6. 모델 테스트
    - model.predict(x_train)
