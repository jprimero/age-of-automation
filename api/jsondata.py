import json
from pprint import pprint

json_file = open('srxfacts.json', encoding='utf=8')
data = json.load(json_file)

pprint(data)
