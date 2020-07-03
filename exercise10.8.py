filename = 'the.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
        
except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)

else:
    words = contents.split()
    num_words =  words.count('the')
    print(num_words)
