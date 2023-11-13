import pandas

data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()s

# average = data["temp"].mean()
# max = data["temp"].max()

# # Get Data in Columns
# print(data["temp"])
# print(data.temp)

# # Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.day == data.day.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = ((monday_temp * 9) / 5) + 32
# print(monday_temp_F)

# Get a dataframe from scratch
data_dict = {
    "students": ["Any", "James", "Angela"], 
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")