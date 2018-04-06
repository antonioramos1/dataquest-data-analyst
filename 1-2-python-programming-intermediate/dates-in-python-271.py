## 1. The Time Module ##

import time

current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time

current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour

## 3. UTC ##

import datetime

current_datetime = datetime.datetime.utcnow()

current_year = current_datetime.year
current_month = current_datetime.month

print(current_datetime)

## 4. Timedelta ##

import datetime

kirks_birthday = datetime.datetime(year = 2233, month = 3, day = 22)
diff = datetime.timedelta(weeks = 15)

before_kirk = kirks_birthday - diff

print(before_kirk)

## 5. Formatting Dates ##

import datetime

mystery_date_formatted_string =mystery_date.strftime('%I:%M%p on %A %B %d, %Y')

print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime

mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string , '%I:%M%p on %A %B %d, %Y')


## 8. Reformatting Our Data ##

import datetime

for item in posts:
    item[2] = float(item[2])
    item[2] = datetime.datetime.fromtimestamp(item[2])

## 9. Counting Posts from March ##

march_count = 0


for item in posts:
    if item[2].month == 3:
        march_count +=1

## 10. Counting Posts from Any Month ##

def users_per_month(month):
    month_count = 0
    for row in posts:
        if row[2].month == month:
            month_count += 1
    return month_count

feb_count = users_per_month(2)
aug_count = users_per_month(8)