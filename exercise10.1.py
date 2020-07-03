filename = 'learning_python.txt'

##Reading an Entire file

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print('\n')

##Reading line by line

with open(filename) as file_object:
    for line in file_object:
        print(line)

print('\n')

##Making a List of Lines from a file

with open(filename) as file_object:
    lines = file_object.readlines()


for line in lines:
    print(line.rstrip())


