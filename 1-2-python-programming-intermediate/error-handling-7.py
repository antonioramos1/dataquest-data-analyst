## 2. Sets ##

gender = []
for item in legislators:
    gender.append(item[3])
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

party = []

for item in legislators:
    party.append(item[6])
party = set(party)
print(party)

## 4. Missing Values ##

for item in legislators:
    if item[3] == '':
        item[3] = 'M'

## 5. Parsing Birth Years ##

birth_years = []
for item in legislators:
    parts = item[2].split('-')
    birth_years.append(parts[0])
birth_years
    

## 6. Try/except Blocks ##

try:
    float('hello')
except:
   print('Error converting to float.') 

## 7. Exception Instances ##

try:
    int('lol')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []

for element in birth_years:
    year = element
    try:
        year = int(year)
    except:
        pass
    converted_years.append(year)

## 9. Convert Birth Years to Integers ##

for item in legislators:
    birthday_column = item[2].split('-')[0]
    try:
        birth_year = (int(birthday_column))
    except:
        birth_year = 0
    item.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value = 1
for item in legislators:
    if item[7] == 0:
        item[7] = last_value
    last_value = item[7]