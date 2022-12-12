import requests
import json
URL = 'https://www.dictionaryapi.com/api/v3/references/learners/json/'
APIKEY = '27fb2276-5d24-4862-adfc-bec060a06983'

print ('vocab word to define')
vocab = input(': ')
queryURL = URL + f'{vocab}'
response = requests.get(queryURL +'?key='+APIKEY)

json_data = (response.text)
json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)