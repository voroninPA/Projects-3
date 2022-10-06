from datetime import datetime, timedelta
try:
    print("Введите дату отправления поезда(ДД/ММ/ГГ ЧЧ:ММ)")
    startrun=datetime.strptime(input(),"%d/%m/%y %H:%M")
except:
    print("Дата введена в неккоректном формате")
    exit()
try:
    print("Введите дату прибытия поезда(ДД/ММ/ГГ ЧЧ:ММ)")
    endrun=datetime.strptime(input(),"%d/%m/%y %H:%M")
except:
    print("Дата введена в неккоректном формате")
    exit()
travel_time=endrun-startrun
if startrun>=endrun:
    print("Дата прибытия раньше даты отправления")
else:
    print("Время в пути:",travel_time)
