import json, requests
import csv

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer xxx',
  'Host': 'api.producthunt.com'
}

parameters = {'order': 'asc','per_page': 50}
post_ids = []

while True:
  response = requests.get('https://api.producthunt.com/v1/users/1/votes'
                         ,headers=headers
                         ,params=parameters)

  data = json.loads(response.text)
  votes = data['votes']
  post_ids.extend(list(v['post_id'] for v in votes))
  parameters['newer'] = votes[-1]['id']
  if len(votes) < 50:
    break

arrUserNo = [1] * len(post_ids)

with open('test.csv', 'w', newline='') as fp:
  a = csv.writer(fp, delimiter=',')
  data = list(zip(arrUserNo, post_ids))
  a.writerows(data)

print('done')

