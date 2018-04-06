## 2. Introduction to the Data ##

nfl_suspensions =  list(csv.reader(open('nfl_suspensions_data.csv', 'r')))
nfl_suspensions = nfl_suspensions[1:]

years = {}

for item in nfl_suspensions:
    if item[5] in years.keys():
        years[item[5]] += 1
    else:
        years[item[5]] = 1

years        

## 3. Unique Values ##

team =[item[1] for item in nfl_suspensions[1:]]
unique_teams = set(team)

games =[item[2] for item in nfl_suspensions[1:]]
unique_games = set(games)

print(unique_games)
print(unique_teams)

## 4. Suspension Class ##

class Suspension:
    
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]
        
third_suspension = Suspension(nfl_suspensions[2])  

third_suspension.name

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except:
            self.year = 0
    def get_year(self):
        return self.year

missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()