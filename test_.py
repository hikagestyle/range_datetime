import datetime
from datetime import timedelta

#スタート日時を設定
startDate = datetime.datetime(2015, 1, 10, 21, 30)
#print(startDate)

#スタート日時から1日ずつ足して範囲指定
for d in range(100):
# for d in reversed(range(100)): #逆順
    day = startDate + datetime.timedelta(days=d)

    print(day)
#    print(day.strftime('%Y-%m-%d'))
#    print(day.strftime('%Y-%m-%dT%H:%M:%S+09:00'))

# python3 test_.py
# python3 test_.py > output.txt
# python3 test_.py > output2.txt
# python3 test_.py > output3.txt

