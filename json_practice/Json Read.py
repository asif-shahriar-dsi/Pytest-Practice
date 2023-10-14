import json

directory = "C:\\Users\\Asif\\Desktop\\Practice\\Python\\Pytest 2\\json_practice\\User.json"

# File = open("C:\\Users\\Asif\\Desktop\\Practice\\Python\\Pytest 2\\json_practice\\User.json", 'r')
# readJson = json.loads(File.read())

with open(directory, "r") as json_file:
    readJson = json.load(json_file)

# Working with 2nd object
for i in readJson:
    if i['id'] == 560:
        i['name'] = input("Enter name: ")
        print(i['car']['Price'])
    print(i)
print(readJson[1]['car']['Name'])

# Working with third object
key_found = False
for i in readJson:
    if "fan of" in i:
        key_found = True
        for club in i['fan of']:
            if club['club name'] == 'Inter Milan':
                club['plays in'] = input("New League: ")
        else:
            assert key_found, f"The key 'fan of' is not present in any of the objects."

print(readJson)

out_file = open("C:\\Users\\Asif\\Desktop\\Practice\\Python\\Pytest 2\\json_practice\\User.json", 'w')
json.dump(readJson, out_file, indent=3)
