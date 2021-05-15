import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

print(person_dict['languages'])


with open('python/filtered_data_file.json') as f:
    data = json.load(f)

print(data)