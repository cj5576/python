import datetime
print(datetime.date.today().strftime('%Y/%m/%d'))
mybirthday=datetime.date(1974,6,20)
print(mybirthday.strftime('%Y/%m/%d'))
print((mybirthday+datetime.timedelta(days=1)).strftime('%Y/%m/%d'))
print((mybirthday+datetime.timedelta(days=30)).strftime('%Y/%m/%d'))
print((mybirthday.replace(month=mybirthday.month+3)).strftime('%Y/%m/%d'))
print((mybirthday.replace(year=mybirthday.year+2)).strftime('%Y/%m/%d'))