## 1. Overview ##

open_data = open('movie_metadata.csv', 'r')
read_data = open_data.read()
list_data = read_data.split('\n')
movie_data = []
for item in list_data:
    movie_data.append(item.split(','))

movie_data[:5]



## 3. Writing Our Own Functions ##

def first_elts(listvar):
    emptylist = []
    for item in listvar:
        emptylist.append(item[0])
    return emptylist
movie_names = first_elts(movie_data)
movie_names[:5]

    

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(listvar):
    if listvar[6] == 'USA':
        return True
    return False

wonder_woman_usa = is_usa(wonder_woman)
    

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def index_equals_str(listvar, indexvar, stringvar):
    if listvar[indexvar] == stringvar:
        return True
    return False

wonder_woman_in_color = index_equals_str(wonder_woman, 2, 'Color')

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(input_lst, index, input_str, header_row = False):
    countvar = 0
    if header_row == True:
        input_lst = input_lst[1:]
    for item in input_lst:
        if item[index] == input_str:
            countvar += 1
    return countvar

num_of_us_movies = feature_counter(movie_data, 6, 'USA', True)
        
    


## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(listvar):
    num_japan_films = feature_counter(listvar,6,'Japan',True)
    num_color_films = feature_counter(listvar,2,'Color',True)
    num_films_in_english = feature_counter(listvar,5,'English',True)
    dict_movies = {'japan_films': num_japan_films,
                   'color_films': num_color_films,
                   'films_in_english': num_films_in_english}
    return dict_movies

summary = summary_statistics(movie_data)
    
    