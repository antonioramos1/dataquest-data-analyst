## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {'t':'day'}
python_top = (requests.get('https://oauth.reddit.com/r/python/top', params=params, headers=headers)).json()

print(python_top)

## 3. Getting the Most Upvoted Post ##

#print(python_top)
python_top_articles =python_top['data']['children']


dict_ups= {'upvotes': 0, 'id': 0}
for i in python_top_articles:
    if i['data']['ups'] > dict_ups['upvotes']:
        dict_ups['upvotes'] = i['data']['ups']
        dict_ups['id'] = i['data']['id']
     
most_upvoted = str(dict_ups['id'])
    #print(i['data']['ups'])
#print(python_top_articles[0]['data']['ups'])




## 4. Getting Post Comments ##

comments = (requests.get('https://oauth.reddit.com/r/python/comments/4b7w9u', headers = headers)).json()

print(comments)

## 5. Getting the Most Upvoted Comment ##

most_upvotes_comment = 0
most_upvoted_comment = ''

for i in comments[1]['data']['children']:
    i['data']['ups']
    if i['data']['ups'] > most_upvotes_comment:
        most_upvotes_comment = i['data']['ups']        
        most_upvoted_comment = i['data']['id']

## 6. Upvoting a Comment ##

params = {'id': 'd16y4ry', 'dir': 1}
request = requests.post('https://oauth.reddit.com/api/vote', headers=headers, json=params)

status =request.status_code