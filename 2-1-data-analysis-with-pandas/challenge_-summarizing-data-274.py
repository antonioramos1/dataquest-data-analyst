## 2. Introduction to the Data ##

import pandas as pd

all_ages = pd.read_csv('all-ages.csv')
recent_grads = pd.read_csv('recent-grads.csv')

all_ages.head()
recent_grads.head()

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
unique_majors_recent = recent_grads['Major_category'].unique()
unique_majors_all = all_ages['Major_category'].unique()

aa_cat_counts = {}
rg_cat_counts = {}

def calculate_major_cat_totals(df):
    cats = df['Major_category'].unique()
    counts_dictionary = {}

    for c in cats:
        major_df = df[df["Major_category"] == c]
        total = major_df["Total"].sum()
        counts_dictionary[c] = total
    return counts_dictionary

aa_cat_counts = calculate_major_cat_totals(all_ages)
rg_cat_counts = calculate_major_cat_totals(recent_grads)

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0

low_wage_proportion =0.0
low_wage_proportion= recent_grads['Low_wage_jobs'].sum() / recent_grads['Total'].sum()


## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for row in majors:
    jobless_rg = recent_grads['Unemployment_rate'][(recent_grads['Major'] == row)]
    jobless_all = all_ages['Unemployment_rate'][(all_ages['Major'] == row)]
    if jobless_rg.sum() < jobless_all.sum():
        rg_lower_count +=1