## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for file in data_files:
    data[file[0:file.index('.')]] = pd.read_csv('schools/' + file)
    
    

## 5. Exploring the SAT Data ##

print(data['sat_results'].head())

## 6. Exploring the Remaining Data ##

for i in data.keys():
    print(data[i].head())

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv('schools/survey_all.txt', delimiter='\t', encoding='windows-1252')
d75_survey = pd.read_csv('schools/survey_d75.txt', delimiter='\t', encoding='windows-1252')
survey = pd.concat([all_survey,d75_survey],axis=0)
survey.head()

## 9. Cleaning Up the Surveys ##

survey['DBN']=survey['dbn']
survey = survey[["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]]
data['survey']=survey
data['survey']

## 11. Inserting DBN Fields ##

data['hs_directory']['DBN'] = data['hs_directory']['dbn']
#class_size['padded_csd'] = 
data['class_size']['padded_csd'] = data['class_size']['CSD'].apply(lambda x: str(x).zfill(2))
data['class_size']['DBN'] = data['class_size']['padded_csd'] + data['class_size']['SCHOOL CODE']
#n = 1
#str(n).zfill(10)

## 12. Combining the SAT Scores ##

sat1= data['sat_results']['SAT Math Avg. Score']
sat2 =data['sat_results']['SAT Critical Reading Avg. Score']
sat3= data['sat_results']['SAT Writing Avg. Score']
sat1 = pd.to_numeric(sat1,errors='coerce')
sat2 = pd.to_numeric(sat2,errors='coerce')
sat3 = pd.to_numeric(sat3,errors='coerce')

data['sat_results']['sat_score'] = sat1 + sat2 + sat3
data['sat_results']['sat_score'].head(5)

## 13. Parsing Geographic Coordinates for Schools ##

import re

def find_last(loc):
    coords = re.findall("\(.+\)", loc)
    lat = coords[0][1:coords[0].index(',')]
    return lat
                     
data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(find_last)

## 14. Extracting the Longitude ##

import re

def find_last(loc):
    coords = re.findall("\(.+\)", loc)
    lon = coords[0][coords[0].index(',')+2:-1]
    return lon
                     
data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(find_last)
data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors='coerce')
data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors='coerce')