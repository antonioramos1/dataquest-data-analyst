## 3. Read the File Into a String ##

filenames = open('dq_unisex_names.csv', 'r')
names = filenames.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
first_five = names_list[:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for valuelist in names_list:
    comma_list = valuelist.split(',')
    nested_list.append(comma_list)
print(nested_list)
    


## 6. Convert Numerical Values ##

print(nested_list[0:5])

numerical_list = []

for lst in nested_list:
    index0 = lst[0] 
    index1 = float(lst[1])
    numerical_list.append([index0,index1])
print(numerical_list[:5])
                      

## 7. Filter the List ##

# The last value is ~100 people
# numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for value in numerical_list:
    if value[1] > 1000:
        thousand_or_greater.append(value[0])
thousand_or_greater