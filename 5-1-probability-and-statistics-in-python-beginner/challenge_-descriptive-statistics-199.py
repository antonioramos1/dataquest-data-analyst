## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")
fig = plt.figure(figsize=(5,12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)
ax4.set_xlim(0,5.0)

movie_reviews["RT_user_norm"].hist(ax=ax1)
movie_reviews["Metacritic_user_nom"].hist(ax=ax2)
movie_reviews["Fandango_Ratingvalue"].hist(ax=ax3)
movie_reviews["IMDB_norm"].hist(ax=ax4)

## 2. Mean ##

def calc_mean(series):
    return series.mean()

rt_mean = calc_mean(movie_reviews['RT_user_norm'])
mc_mean = calc_mean(movie_reviews['Metacritic_user_nom'])
fg_mean = calc_mean(movie_reviews['Fandango_Ratingvalue'])
id_mean = calc_mean(movie_reviews['IMDB_norm'])

## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean
def calc_variance(series):
    mean = calc_mean(series)
    return sum([(i-mean)**2 for i in series]) / len(series)
def calc_variance2(series):
    return series.var(ddof=0) #had to change it to 0 degrees of freedom, 1 by default

rt_var,rt_stdev = calc_variance(movie_reviews['RT_user_norm']), calc_variance(movie_reviews['RT_user_norm'])**(1/2)
mc_var, mc_stdev = calc_variance2(movie_reviews['Metacritic_user_nom']), calc_variance2(movie_reviews['Metacritic_user_nom'])**(1/2)
fg_var,fg_stdev = calc_variance(movie_reviews['Fandango_Ratingvalue']), calc_variance(movie_reviews['Fandango_Ratingvalue'])**(1/2)
id_var,id_stdev = calc_variance(movie_reviews['IMDB_norm']), calc_variance(movie_reviews['IMDB_norm'])**(1/2)

## 4. Scatter plots ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4,8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.set_xlim(0,5)
ax2.set_xlim(0,5)
ax3.set_xlim(0,5)

ax1.scatter(movie_reviews['RT_user_norm'], movie_reviews['Fandango_Ratingvalue'])
ax2.scatter(movie_reviews['Metacritic_user_nom'], movie_reviews['Fandango_Ratingvalue'])
ax3.scatter(movie_reviews['IMDB_norm'], movie_reviews['Fandango_Ratingvalue'])

plt.show()

## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def covariance(x,y):
    return sum([(x[i] - calc_mean(x))*(y[i]-calc_mean(y)) for i in range(len(x))]) / len(x)

rt_fg_covar = covariance(movie_reviews['RT_user_norm'], movie_reviews['Fandango_Ratingvalue'])
mc_fg_covar = covariance(movie_reviews['Metacritic_user_nom'], movie_reviews['Fandango_Ratingvalue'])
id_fg_covar = covariance(movie_reviews['IMDB_norm'], movie_reviews['Fandango_Ratingvalue'])


## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

def calc_correlation(x,y):
    return (calc_covariance(x,y) / (calc_variance(x)**(1/2) * calc_variance(y)**(1/2)))
    
rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])
