# with open('weather_data.csv') as file:
#     rows = file.readlines()
    
# data = []
# for row in rows:
#     row_stripped = row.strip()
#     data.append(row_stripped)
    
# print(data)

# # ---------------------

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

# # ---------------------

import pandas


data = pandas.read_csv("weather_data.csv")
print(data["temp"])
# print(data)