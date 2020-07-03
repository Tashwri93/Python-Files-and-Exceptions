import json

filename = 'fav_num.json'



try:
    with open(filename) as file_object:
        favourite_num = json.load(file_object)
except FileNotFoundError:
    favourite_num = input("What is your favourite number?: ")
    with open(filename, 'w') as file_object:
        json.dump(favourite_num, file_object)
        print("Your favourite number is " + str(favourite_num))
else:
    print("I still remember your favourite number which is " + str(favourite_num))





