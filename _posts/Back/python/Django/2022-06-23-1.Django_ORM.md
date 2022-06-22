---
layout: single
title:  "2022.06.23 - 1.장고 모델(ORM)과 장고 모델 필드"
categories : 
    - Django
---

## 1. 장고 모델(ORM)

#### 애플리케이션의 저장 방법

- 데이터베이스 : **RDBS**, NoSQL
- 파일 : 로컬, 외부 정적 스토리지
- 캐시 서버 : memcached, redis

#### 데이터베이스의 종류
> RDBMS, NoSQL을 사용하는데 같은 작업을 하더라도, 보다 적은 수의 SQL, 보다 높은 성능의 SQL을 수행하도록 노력

1. RDBMS
    - Django Models, SQLAlchemy, Orator, Peewee, PonyORM 등
2. NoSQL
    - django-mongodb-engine, hot-redis, MongoEngine, PynamoDB 등

- SQL을 직접 사용하기도 하지만 ORM을 통해 SQL을 사용함
    - ORM을 쓰더라도 어떤 SQL이 실행되는지 알아야함 **django-debug-toolbar** 사용 권장
    - 직접 SQL문자열을 조합하지말고 인자로 처리해야함 -> SQL Injection 방지 

## 모델 활용시 주의사항
- 장고 모델을 통해 **데이터베이스 테이블**과 **파이썬 클래스**를 1:1로 매핑한다.
    > DB가 먼저 존재하면 DB에 맞게 파이썬 클래스를 만들어야함
    1. 모델 클래스명은 단수로 지정. ex) Posts(X), Post(O)
    2. 매핑되는 모델 클래스는 DB 테이블 필드 내역이 일치해야한다.
    3. 모델을 만들기 전에, 서비스에 맞게 **데이터베이스 설계**가 필수

## 모델 활용 방법
1. **장고 모델**을 통해 데이터베이스 형상 관리할 경우
    1. 모델 클래스 작성
    2. 모델 클래스로부터 마이그레이션 파일 생성 -> makemigrations 명령
    3. 마이그레이션 파일을 데이터베이스에 적용 -> migrate 명령
    4. 모델 활용

- 기본 DB테이블명 : DB테이블명은 "앱이름_모델명"으로 정해짐
- 커스텀 지정 : 모델 Meta 클래스의 db_table 속성 (마이그레이션 하기 전에 지정)

1. **장고 외부**에서 데이터베이스 형상을 관리할 경우
    1. 데이터베이스로부터 모델 클래스 소스 생성 -> inspectdb 명령
    2. 모델 활용

```python
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
                               related_name='+')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # TODO
        pass
```

---

## 2. 장고 모델필드

### 기본지원되는 모델필드 타입

| 종류 | 필드 |
| :---: | :--- |
| Primary Key | **AutoField**, BighAutoField |
| 문자열 | **CharField**, **TextField**, **SlugField** |
| 날짜/시간 | DateField, TimeField, **DateTimeField**, DurationField |
| 참/거짓 | **BooleanField**, NullBooleanField|
| 숫자 | IntegerField, SmallIntegerField, PositiveIntegerField, PositiveSmallIntegerfield, BigIntegerField, DecimalField, FloatField |
| 파일 | BinaryField, **FileField**, **ImageField**, FilePathField |
| 이메일 | EmailField |
| URL | URLField |
| UUID | UUIDField |
| 아이피 | GenericIPAddressField |

### 자주 쓰는 필드 공통 옵션

| 옵션 | 설명 | DB옵션 여부 |
| :---: | :--- | :---: |
| blank | 장고 단에서 validation시에 empty 허용 여부 (디폴트: False) |  |
| null | null 허용 여부 (디폴트: False) | True |
| db_index | 인덱스 필드 여부 (디폴트: False) | True |
| default | 디폴트 값 지정, 혹은 값을 리턴해줄 함수 지정 |  |
| unique | 현재 테이블 내에서 유일성 여부 (디폴트: False) | True |
| choices | select 박스 소스로 사용 |  |
| validators | validators를 수행할 함수를 다수 지정 (ex- 이메일만 받기) |  |
| verbose_name | 필드 레이블, 미지정시 필드명이 사용 |  |
| help_text | 필드 입력 도움말 |  |

### ⭐️⭐️ 설계한 데이터 베이스 구조에 따라, 최대한 필드타입을 타이트하게 지정해 주는 것이, 입력값 오류를 막을 수 있음 ⭐️⭐️

- blank/null 지정은 최소화 -> manage.py inpectdb 명령을 통해 생성된 모델코드는 초안
- validators들이 다양하게, 타이트하게 지정
    - 필요하다면 validators들을 추가로 타이트하게 지정
- 백엔드 유효성 검사를 별도로 수행해야함 -> 프론트엔드 유효성검사는 사용자 편의를 위한 것
- 직접 유효성로직을 만들지말고 Django에 이미 구성된 Features를 사용
    - Django의 Form/Model 또는 DRF의 Serializer를 통해 지원

> ORM은 SQL 쿼리를 만들어주는 역할일뿐
> 성능 높은 애플리케이션을 위해서는 **데이터베이스**에 대한 깊은 이해가 필요