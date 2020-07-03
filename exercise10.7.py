def read_files(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        pass
       # msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_files(filename)
    
