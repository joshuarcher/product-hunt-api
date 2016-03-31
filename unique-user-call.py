import json, requests
import csv


def write_csv(user_id, product_ids):
  arrUserNo = [user_id] * len(product_ids)
  with open('test.csv', 'a', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    data = list(zip(arrUserNo, product_ids))
    data.append(())
    a.writerows(data)


headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer d38b9613db574876c06bd2db6dca16091e22d0ace28de2c59fd7b340d78607a9',
  'Host': 'api.producthunt.com'
}

parameters = {'order': 'asc','per_page': 50}
post_ids = []
_user_id = 2

'''
execute http request beginning at _user_id
when all user likes are found (vote count)
  write to csv
  increment user id and clear post_ids
  do it again with the next user
  BUTTTT if you get to user #100, stop.. for now
'''

while True:
  response = requests.get('https://api.producthunt.com/v1/users/{}/votes'.format(_user_id)
                         ,headers=headers
                         ,params=parameters)
  if response.status_code != 200:
    print('error with status_code: {}'.format(response.status_code))
    break
  data = json.loads(response.text)
  votes = data['votes']
  post_ids.extend(list(v['post_id'] for v in votes))
  parameters['newer'] = votes[-1]['id']
  if len(votes) < 50:
    write_csv(_user_id, post_ids)
    _user_id += 1
    post_ids = []
    break
    if _user_id >= 100:
      break

print('done')
