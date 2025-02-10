from datetime import datetime,timedelta,time

#1
def substract_five_days():
    current_date=datetime.now()
    return str(current_date-timedelta(days=5))
print(substract_five_days())

#2
def yesterday_today_tomorrow():
    current_date=datetime.now()
    yesterday=current_date-timedelta(days=1)
    tomorrow=current_date+timedelta(days=1)
    return str(yesterday),str(current_date),str(tomorrow)
print(yesterday_today_tomorrow())

#3
def microseconds():
    x=datetime.now()
    return x.strftime('%f')
print(microseconds())

#4
def difference_in_seconds():

    d1 = datetime(2022, 10, 28, 13, 54, 18)
    d2 = datetime(2017, 9, 18, 23, 36, 29)

    time_delta = d1 - d2
    return time_delta.total_seconds()
print(difference_in_seconds())