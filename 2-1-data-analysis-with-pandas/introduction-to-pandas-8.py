## 3. Read in a CSV file ##

import pandas

food_info = pandas.read_csv('food_info.csv')
type(food_info)
print(food_info)

## 4. Exploring the DataFrame ##

print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)

first_twenty = food_info.head(20)

## 7. Selecting a row ##

hundredth_row = food_info.loc[99]

print(hundredth_row)

## 8. Data types ##

print(food_info.dtypes)

## 9. Selecting multiple rows ##

num_rows = food_info.shape[0]

num_rows
#last_rows = food_info.loc[num_rows-5:num_rows-1]

## 10. Selecting individual columns ##

saturated_fat = food_info['FA_Sat_(g)']
cholesterol = food_info['Cholestrl_(mg)']

## 11. Selecting multiple columns by name ##

selenium_thiamin = food_info[['Selenium_(mcg)', 'Thiamin_(mg)']]

## 12. Practice ##


column_names = food_info.columns.tolist()

gram_columns = []
for item in column_names:
    if item.endswith('(g)'):
        gram_columns.append(item)
gram_df = food_info[gram_columns]
gram_df.head(3)

