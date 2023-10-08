import datetime
from datetime import timedelta

#スタート日時を設定
startDate = datetime.datetime(2015, 1, 10, 21, 30)
#print(startDate)

with open('date2.txt', 'w') as f:

#スタート日時から1日ずつ足して範囲指定
#    for d in range(100):
    for d in reversed(range(100)): #逆順
        day = startDate + datetime.timedelta(days=d)

        f.write(day.strftime('%Y-%m-%d %H:%M:%S') + '\n')
#        f.write(day.strftime('%Y-%m-%d') + '\n')
#        f.write(day.strftime('%Y-%m-%dT%H:%M:%S+09:00') + '\n')

# python3 test_2.py


