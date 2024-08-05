import requests
import json
from bs_select_opponents import get_opponents
         
response = requests.get('https://en.wikipedia.org/wiki/Khabib_Nurmagomedov')
# print(response.status_code)
opponents = get_opponents(response.text)
opponents_json = json.dumps(opponents)
print(opponents_json)

with open('khabib_opponents.json', 'w', encoding = 'utf-8') as f:
    f.write(opponents_json)

# with open('khabib.html', 'r', encoding = 'utf-8') as f:
#     contents = f.read()
#     print(contents)

# with open('khabib2.html', 'w', encoding = 'utf-8') as f:
#     f.write(response.text)