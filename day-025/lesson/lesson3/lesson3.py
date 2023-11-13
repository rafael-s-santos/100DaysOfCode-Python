import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231112.csv")

number_of_grays = len(data[data["Primary Fur Color"] == "Gray"])
number_of_reds = len(data[data["Primary Fur Color"] == "Cinnamon"])
number_of_blacks = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {"Fur Color": ["grey", "red", "black"], "Count": [number_of_grays, number_of_reds, number_of_blacks]}

df = pd.DataFrame(squirrel_dict)
df.to_csv("squirrel_count.csv")
