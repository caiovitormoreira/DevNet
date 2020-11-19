import json

jsonOBJ = json.load(open('sample.json'))

print(jsonOBJ['people'][0]['LastName'])
print(jsonOBJ['people'][1]['LastName'])
print(jsonOBJ['people'][2]['LastName'])
