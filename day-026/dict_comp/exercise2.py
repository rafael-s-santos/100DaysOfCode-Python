input_data = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: ((temp_c * 9/5) + 32) for (day, temp_c) in input_data.items()}

print(weather_f)