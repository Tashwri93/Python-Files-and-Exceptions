filename = 'guest_book.txt'

prompt = "\nEnter 'quit' to end the program."
prompt += "\nWhat is your name?: "

active = True
while active:
    name = input(prompt)

    if name == 'quit':
        active = False
    else:
        print("Hi " + name + " , you are added to the guest book")
        with open(filename, 'a') as file_object:
            file_object.write(name+'\n')

 
