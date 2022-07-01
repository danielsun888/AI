from Reservater import Reservater as Reservater
from User import User as User
import datetime
import config

def main():
  
  user_count = len(config.USERS_INFO)

  # 사용할 드라이브 세팅
  users = [User(i) for i in range(user_count)]
  
  date_start = datetime.datetime(2022, 7, 4)
  date_end = 5

  # 날짜 단위로
  for i in range(date_end):
    date = date_start + datetime.timedelta(float(i))
    # 방 단위로
    for j in config.ROOM_NUM:
      user = users[(i + j) % user_count]
      name = Reservater(user).booking(room_num = j, date = date)
      print(name , config.URL2ROOM.index(j), date)

if __name__ == '__main__':
  main()