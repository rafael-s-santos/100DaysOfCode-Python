# Reading and Writing Files
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files


# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
    ontents = file.read()
