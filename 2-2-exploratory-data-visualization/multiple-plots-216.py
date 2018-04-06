## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

plt.plot(unrate['DATE'].head(12),unrate['VALUE'].head(12))
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')

plt.show()

## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 5. Adding Data ##

fig = plt.figure()
top = fig.add_subplot(2,1,1)
bottom = fig.add_subplot(2,1,2)

top.plot(unrate['DATE'].head(12), unrate['VALUE'].head(12))
bottom.plot(unrate['DATE'][12:24], unrate['VALUE'][12:24])

plt.show
print(type(top))

## 6. Formatting And Spacing ##

fig = plt.figure(figsize=(18, 12))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')


plt.show()

## 7. Comparing Across More Years ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,12))

grid1 = fig.add_subplot(5,1,1)
grid2 = fig.add_subplot(5,1,2)
grid3 = fig.add_subplot(5,1,3)
grid4 = fig.add_subplot(5,1,4)
grid5 = fig.add_subplot(5,1,5)

grid1.plot(unrate['DATE'][0:12], unrate['VALUE'][0:12])
grid2.plot(unrate['DATE'][12:24], unrate['VALUE'][12:24])
grid3.plot(unrate['DATE'][24:36], unrate['VALUE'][24:36])
grid4.plot(unrate['DATE'][36:48], unrate['VALUE'][36:48])
grid5.plot(unrate['DATE'][48:60], unrate['VALUE'][48:60])

plt.show()

## 8. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6,3))
#ax1 = fig.add_subplot(2,1,1)
#ax2 = fig.add_subplot(2,1,2)

plt.plot(unrate['MONTH'][0:12],unrate['VALUE'][0:12], c='red')
plt.plot(unrate['MONTH'][12:24],unrate['VALUE'][12:24], c='blue')

plt.show()

## 9. Adding More Lines ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))

start_index = 12
end_index = 12
colors = ['red', 'blue','green','orange','black']

for i in range(5):
    plt.plot(unrate['MONTH'][start_index*i:end_index*(i+1)], unrate['VALUE'][start_index*i:end_index*(i+1)], c=colors[i])
plt.show()

## 10. Adding A Legend ##

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,6))
start_index = 12
end_index = 12
colors = ['red', 'blue','green','orange','black']
for i in range(5):
    plt.plot(unrate['MONTH'][start_index*i:end_index*(i+1)],
             unrate['VALUE'][start_index*i:end_index*(i+1)],
             c=colors[i],
             label=str(1948+i))
plt.legend(loc='upper left')
plt.show()

## 11. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title('Monthly Unemployment Trends, 1948-1952')
plt.xlabel('Month, Integer')
plt.ylabel('Unemployment Rate, Percent')
plt.show()