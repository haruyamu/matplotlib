import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
response_dict = r.json
repo_dicts = response_dict['items']

repo_dict = repo_dicts[0]
for key in sorted(repo_dict.keys()):
    print(key)
