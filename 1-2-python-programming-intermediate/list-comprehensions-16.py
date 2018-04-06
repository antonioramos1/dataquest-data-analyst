## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for index, item in enumerate(ships):
    print(item)
    print(cars[index])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for index, row in enumerate(things):
    row.append(trees[index])
things

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [item * 2 for item in apple_prices]
apple_prices_lowered = [item - 100 for item in apple_prices]

## 5. Counting Female Names ##

list_females = []
for item in legislators:
    if item[3] == 'F' and item[7] > 1940:
        list_females.append(item[1])

list_females_dict = {}
for item in list_females:
    if item in list_females_dict:
        list_females_dict[item] += 1
    else:
        list_females_dict[item] = 1

name_counts = list_females_dict

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

checks = [item != None and item > 30 for item in values]
checks

## 8. Highest Female Name Count ##

max_value = None

for value in name_counts.values():
    if max_value == None or value > max_value:
        max_value = value
        print(value)

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for key, value in plant_types.items():
    print(key)
    print(value)

## 10. Finding the Most Common Female Names ##

top_female_names = []

for key, value in name_counts.items():
    if value == 2:
        top_female_names.append(key)

## 11. Finding the Most Common Male Names ##

top_male_names = []

male_name_counts = {}

for item in legislators:
    if item[3] == 'M' and item[7] > 1940:
        if item[1] in male_name_counts:
            male_name_counts[item[1]] += 1
        else:
            male_name_counts[item[1]] = 1
            
highest_male_count = None

for key,value in male_name_counts.items():
    if highest_male_count == None or value > highest_male_count:
        highest_male_count = value

top_male_names = [key for key,value in male_name_counts.items() if value == highest_male_count]

top_male_names