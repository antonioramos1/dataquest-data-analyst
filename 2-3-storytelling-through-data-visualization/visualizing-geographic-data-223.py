## 1. Geographic Data ##

import pandas as pd

airlines= pd.read_csv('airlines.csv')
airports= pd.read_csv('airports.csv')
routes= pd.read_csv('routes.csv')
for i in [airlines, airports, routes]:
    print(i.iloc[0])

## 4. Workflow With Basemap ##

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

## 5. Converting From Spherical to Cartesian Coordinates ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

latitudes=airports['latitude'].tolist()
longitudes=airports['longitude'].tolist()

x,y = m(longitudes, latitudes)
help(m)

## 6. Generating A Scatter Plot ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
x, y = m(longitudes, latitudes)

m.scatter(x,y, s=1)
plt.show()

## 7. Customizing The Plot Using Basemap ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()

plt.show()

## 8. Customizing The Plot Using Matplotlib ##


fig, ax = plt.subplots(figsize=(20,20))
ax.set_title('Scaled Up Earth With Coastlines')

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 9. Introduction to Great Circles ##

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

geo_routes = pd.read_csv('geo_routes.csv')
geo_routes.info()
geo_routes.head(5)

## 10. Displaying Great Circles ##

fig, ax = plt.subplots(figsize=(15,30))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()


def create_great_circles(df):
    for index, row in df.iterrows():
        if (abs(row[0] - row[1]) < 180) and (abs(row[2] - row[3]) < 180):
            m.drawgreatcircle(row[0], row[1], row[2], row[3])                 

dfw = geo_routes[['start_lon', 'start_lat','end_lon', 'end_lat']][geo_routes['source'] == 'DFW']
create_great_circles(dfw)

plt.show()