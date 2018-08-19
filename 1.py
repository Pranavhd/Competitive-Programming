from datetime import datetime,date, timedelta
import datetime
import dateparser
from configparser import ConfigParser  

print(datetime.datetime.today().strftime('%Y-%m-%d'))
yesterday = date.today() - timedelta(1)
daybeforeyesterday = date.today() - timedelta(4)
print(yesterday.strftime('%Y-%m-%d'))
print(daybeforeyesterday.strftime('%Y-%m-%d'))
last_hour_date_time = datetime.datetime.now() - timedelta(hours = 2)
print(last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S'))
datetime_object = dateparser.parse('2018-06-05')
print(datetime_object)
dobj = datetime.datetime.strptime('2018-06-05','%Y-%m-%d')
print(dobj)
today = datetime.datetime.today().strftime('%Y-%m-%d')
history = date.today()
print(today)
print(history)
obj_his = datetime.datetime.strptime(history,'%Y-%m-%d')
if today<obj_his:
    print("yes")
