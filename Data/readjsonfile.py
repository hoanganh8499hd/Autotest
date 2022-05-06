import json

# Opening JSON file
with open('Data/userlogin.json', 'r') as openfile:

    # Reading from json file
    json_object = json.load(openfile)

print(json_object['name'])
print(type(json_object))
