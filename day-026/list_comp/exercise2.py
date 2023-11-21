list_of_strings = ['1', ' 1', ' 2', ' 3', ' 5', ' 8', ' 13', ' 21', ' 34', ' 55']
numbers = [int(s) for s in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)