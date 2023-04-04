# commit_ref.md
### commit 생성 규칙에 대해 정의한 파일 
----
### 개요 
- commit 생성 시 한눈에 알아볼 수 있도록 하기 위한 규칙 정의 
- commit 생성 메세지는 조직마다 혹은 회사마다 다른 방식으로 사용하며 해당 조직에서는 아래와 같이 사용하도록 한다. 


### Commit Msg
```
[Title] 
[Type 명] : Type 내용

[Body] : 수정 내용요약 

[Resolve] : 해결 내용 작성
[See Also] : 참고 사항 및 기타
```
### Commit Msg Detail 
#### Title 
- 커밋 메세지의 제목을 작성 
- 제목은 한눈에 알아볼 수 있는 내용 혹은 작업 내용(번호 포함)으로 작성하는 것이 좋다.

#### Type
- 작업에 따른 커밋 유형을 구분하여 작성 
- 해당 프로젝트에서 사용할 type의 종류는 아래와 같다.
  ```
  feature dev : 기능 개발 
  feature del : 신규 개발 기능 삭제 
  feature mod : 신규 개발 기능 수정 
  fix : 파일 및 오류 수정
  cicd : CI/CD 관련 설정 수정
  docs : 문서 등록 및 수정 
  style : 코드 스타일(css 포함) 및 포멧 수정
  refactor : 코드 리팩토링에 대한 커밋
  test : 테스트 코드 수정에 대한 커밋
  ```
- 추후 변경 가능
- type 내용 부분에 파일 이름 또는 내용 작성

#### Body
- 작업한 내용을 간결하게 작성
- 과거형 사용 X
  - [EX]
  - 회원 권한 구분에 따른 userAdmin.jsp 로직 내 JQurey 수정입니다. (X)
  - 회원 권한 구분에 따른 userAdmin.jsp 로직 내Jquery 수정했습니다.(X)
  - 회원 권한 구분에 따른 userAdmin.jsp 로직 내Jquery 수정(O), 수정 완료(O)

#### Resolve /  See Also
- 참고부분이라 작성안해도 무관 
- Resolce는 작성이 필요한 경우라면 작성하되 작업이 완료되었을 경우 작성 
- See Also의 경우 참고가 필요한 경우 언급 
  ```
  ex)
  1. Resolve
    - 작성 안함
    - [Resolve] : N/A   
    - [Resolve] : resolve
    - [Resolve] : jira name 등 
  2. See Also 
    - 작성 안함 
    - [See Also] : N/A
    - [See Also] : 팀원 명
    - [See Also] : 기타 내용 (로직 추후 리펙토링 필요 등) 
    
  ```


### Commit Msg(ex)
```
[Type 1]
  docs:Update READEME.md
  docs : README.md

  [docs] READMD.md 파일 내용 수정 
  - REPOS의 용도 정리

  [Resolve] : N/A
  [See Also] : N/A

[Type 2]
  docs: 레파지토리 설명 파일 신규 생성
  docs : 레파지토리 설명 파일 신규 생성

  - READMD.MD 파일 신규 생성 
  
 [See Also] : ONECHANHO

```
