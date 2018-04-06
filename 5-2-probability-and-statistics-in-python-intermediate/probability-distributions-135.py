## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

prob_over_5000 = bikes['cnt'][bikes['cnt'] > 5000].shape[0] / bikes['cnt'].shape[0]

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))
p = 0.39
q = 1-p

def prob(k, N):
    combinations = math.factorial(N) / (math.factorial(k)*(math.factorial(N-k)))
    probability = (p**k)*(q**(N-k))
    return probability * combinations

outcome_probs = [prob(i,30) for i in outcome_counts]

## 5. Plotting the distribution ##

import matplotlib.pyplot as plt

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)
dist = binom.pmf(outcome_counts,30,0.39)

plt.bar(outcome_counts, dist)
plt.show()

## 8. Computing the mean of a probability distribution ##

dist_mean = None

dist_mean = 30*0.39

## 9. Computing the standard deviation ##

dist_stdev = None

n = 30
p = .39
q = 1-p

dist_stdev = (p*q*n)**(1/2)


## 10. A different plot ##

# Enter your answer here.

binom10 = binom.pmf(range(0,11), 10, 0.39)
plt.bar(range(0,11), binom10)
plt.show()

binom100 = binom.pmf(range(0,101), 100, 0.39)
plt.bar(range(0,101), binom100)
plt.show()

## 11. The normal distribution ##

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 12. Cumulative density function ##

outcome_counts = linspace(0,30,31)
cdf = binom.cdf(range(31),30,0.39)

plt.plot(range(31), cdf)

## 14. Faster way to calculate likelihood ##

left_16 = None
right_16 = None

left_16 =binom.cdf(16,30,.39)
right_16 = 1 -left_16