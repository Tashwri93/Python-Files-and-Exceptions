filename = 'guest.txt'

guest = input("Please enter your name: ")

with open(filename, 'a') as file_object:
    file_object.write(guest+'\n')
