import datetime

weeks = ["월", "화", "수", "목", "금", "토", "일"]
mon = input("월을 입력하세요 :")
day = input("일을 입력하세요 :")
week = input("요일을 입력하세요 :")
mon = int(mon)
day = int(day)
today = datetime.date(1, mon, day)
delta = datetime.timedelta(days=99)
today += delta
now_week = weeks[weeks.index(week) + 99%7]
print(f"{mon}월 {day}일 {week}요일부터 100일뒤는 {today.month}월 {today.day}일 {now_week}요일")

