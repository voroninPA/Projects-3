from datetime import datetime, timedelta
try:
    print('Введите дату рождения (ДД/ММ/ГГ):')
    birthday = datetime.strptime(input(), "%d/%m/%y")
except:
    print('Дата отправления в неверном формате')
    exit()
Days=10000
Minutes=1000000
Seconds=1000000000
Day_time=timedelta(days=Days)
a=birthday+Day_time
Min_time = timedelta(minutes=Minutes)
b=birthday+Min_time
Sec_time=timedelta(seconds=Seconds)
c=birthday+Sec_time

print('Исполнится 10,000 дней:', a)
print('Исполнится 1,000,000 минут:', b)
print('Исполнится 1,000,000,000 секунд:', c)
