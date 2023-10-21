import json

directory = "C:\\Users\\Asif\\Desktop\\Practice\\Python\\Pytest 2\\Class 2\\user_info.json"

with open(directory, 'r') as json_file:
    read_json = json.load(json_file)

# for i in read_json:
#     if i['id']==501:
#         print(i['car']['price'])


for i in read_json:
    if i['id'] == 502:
        for club in i["fan_of"]:
            if club['club_name'] == "Man City":
                club['plays_in'] = input("Plays in: ")

print(read_json)


#
# print(read_json[0]['name'])
# read_json[0]['name'] = input("Enter a new name: ")
#
output_directory = open(directory, 'w')
json.dump(read_json, output_directory)
