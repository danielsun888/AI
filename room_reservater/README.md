# room_reservater

방 예약을 쉽게하기 위한 오토 프로그램

공간을 빌릴 때, 복잡한 정해진 방법으로 빌려야 했습니다. 코드를 작성하여 auto로 처리해 버립시다

이 레파지토리는 다음이 포함되어 있습니다.

```bash
.
├── LICENSE
├── README.md # 사용법이 적힌 파일
├── Reservater.py # 예약 클래스
├── User.py # 유저 클래스
├── config.py # 유저 정보와 사이트 정보를 담은 파일
├── main.py # 실행시킬 파일
├── requirement.txt # python 라이브러리 모음
└── settings.py # Chrome 기반 driver 세팅 관련 파일

0 directories, 8 files
```

각 파일에 대한 간단한 설명과 실행법을 나열합니다.

## 목차

***

- [설치](#설치)
  - [chrome 설치](#chrome-설치)
  - [config 파일 수정](#config-파일-수정)
- [사용법](#사용법)

## 설치

***

가장 먼저 설치할 컴퓨터에 git을 복제합니다.

```bash
git clone https://github.com/LBR56/reservater.git
```

이 프로젝트는 python 3.8.9 버전을 사용하였습니다. 또 필요한 라이브러리는 requirement.txt에 기제되어 있습니다.

그럼으로 필요한 라이브러리를 설치합니다.

```bash
python -m pip install --upgrade pip
# 맥의 경우 python -> python3
```

```bash
pip install -r requirement.txt
```

### chrome 설치

***

이 프로젝트는 여러 브라우저 중 크롬에 중점적으로 맞췄습니다. 그럼으로 chrome 브라우저가 설치되어 있어야 합니다.

[크롬 다운로드 링크](https://www.google.com/intl/ko_kr/chrome/)를 통해 설치해 주시길 바랍니다.

### config 파일 수정

***

기본적으로 config 파일은 다음의 모습을 가지고 있습니다.

```python
USERS_INFO = [
  {
    'id':'아이디1',
    'pw':'비번1',
  },  
  {
    'id':'아이디2',
    'pw':'비번2',
  },
]

# 룸 번호당 url 위치
URL2ROOM = range(13, 5, -1)
# 빌릴 방 넣기
ROOM_NUM = [URL2ROOM[3], URL2ROOM[5]]

class Url:
  login = '로그인 url'
  reservate = '예약 url'
```

다음 각 요소를 변경해주지 않는다면, 원치 않는 사이트로 들어갈 위험이 있습니다.

## 사용법

***

1. 위 나열한 config 요소를 넣어줍니다.
1. ```python main.py```를 실행합니다.

```bash
python main.py
# 맥일 경우 python -> python3
```
