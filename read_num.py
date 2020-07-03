import json

filename = 'fav_num.json'

with open(filename) as file_object:
    favourite_num = json.load(file_object)
    print("Your favourite number is " + str(favourite_num))
