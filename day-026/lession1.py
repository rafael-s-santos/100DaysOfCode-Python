# numbers = [1, 2, 3]
# # new_list = []
# # for n in numbers:
# #     add_1 = n + 1
# #     new_list.append(add_1)  
# # print(new_list)

# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

names = ["Alex", "Beth", "Caronline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)