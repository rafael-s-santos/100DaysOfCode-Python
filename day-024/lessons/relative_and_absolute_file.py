# Caminho de ficheiro relativo
#with open("file/my_file2.txt") as file: 
# Caminho de ficheiro absoluto
with open("/home/rafaelsantos/development/python/100DaysOfCode-Python/day-024/file/lessons/my_file2.txt") as file:
    contents = file.read()
    print(contents)