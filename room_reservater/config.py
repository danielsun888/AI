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

class InputData:
  belong = '회사명'
  people = '인원 수'
  purpose = '목표'

class Url:
  login = '로그인 url'
  reservate = '예약 url'
