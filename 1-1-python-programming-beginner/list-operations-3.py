## 2. Parsing the File ##

weather_data = []
csvfile = open('la_weather.csv' , 'r')
data_csv = csvfile.read()
datalist = data_csv.split('\n')
for item in datalist:
    splitdata = item.split(',')
    weather_data.append(splitdata)

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []

for record in weather_data:
    weather.append(record[1])

## 4. Counting the Items in a List ##

#count = len(weather)
count = 0
for item in weather:
    count += 1

## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = 'cat' in animals
space_monster_found = 'space_monster' in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for weather in weather_types:
    weather_type_found.append(weather in new_weather)
        