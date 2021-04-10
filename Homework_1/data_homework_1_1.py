import json
import requests

USERNAME = 'Artemprod'
URL = f"https://api.github.com/users/{USERNAME}/repos"
# USERNAME = str(input('input username: '))
req = requests.get(URL)
req_json = req.json()

with open('git_repo_js.json', 'w') as f:
    json.dump(req_json, f)

lenth_json = len(list(req_json))
print(f"amount of dicts in json file -  {lenth_json}")


def get_info():
    number_of_json_dict = int(input('Select number of dict: ')) - 1
    dict_1 = dict(req_json[number_of_json_dict])
    selected_dict = dict_1.items()
    for index, i in enumerate(selected_dict):
        print(index + 1, i)

def get_repos():
    number_of_json_dict = int(input('Select number of dict: ')) - 1
    dict_1 = dict(req_json[number_of_json_dict])
    selected_repo = dict_1.get('full_name')
    print(selected_repo)


action = int(input('What are you want to do?:\n 1 - get info\n 2 - get repo \n input: ' ))

if action == 1:
    get_info()
else:
    get_repos()