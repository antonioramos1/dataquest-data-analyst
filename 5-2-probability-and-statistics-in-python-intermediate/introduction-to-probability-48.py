## 1. Probability basics ##

# Print the first two rows of the data.
#print(flags[:2])
most_bars_country = flags['name'][flags['bars'] == max(flags['bars'])]
highest_population_country = flags['name'][flags['population'] == max(flags['population'])]

## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_probability = len(flags[flags['orange'] == 1]) / total_countries
stripe_probability = len(flags[flags['stripes'] > 1]) / total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = .5 ** 10
hundred_heads = 0.5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.

odds_red1 = len(flags[flags['red'] == 1]) / flags.shape[0]
odds_red2 = (len(flags[flags['red'] == 1])-1) / (flags.shape[0] -1)
odds_red3 = (len(flags[flags['red'] == 1])-2) / (flags.shape[0] -2)
three_red = odds_red1 * odds_red2 * odds_red3

## 5. Disjunctive probability ##

start = 1
end = 18000

import random
random.randint(1,18000)

hundred_prob = len([i for i in range(1,18001) if i % 100 == 0]) / 18000
seventy_prob = len([i for i in range(1,18001) if i % 70 == 0]) / 18000

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None

red_or_orange = len(flags[(flags['orange'] == 1) | (flags['red'] == 1)]) / flags.shape[0]
stripes_or_bars = len(flags[(flags['bars'] > 0) | (flags['stripes'] > 0)]) / flags.shape[0]



## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None

heads_or = 0.5 + (0.5*0.5) + (0.5*0.5*0.5)