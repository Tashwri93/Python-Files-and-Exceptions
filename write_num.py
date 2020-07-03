import json

favourite_num = input("What is your favourite number?: ")

filename = 'fav_num.json'
with open(filename, 'w') as file_object:
    json.dump(favourite_num, file_object)
