import random

class WEATHER:

    def __init__(self):
        self.weather_pick_list = ['Sunny']

    def pick_weather(self):
        weather_list = ['Sunny', 'Cloudy', 'Overcast', 'Partly Cloudy', 'Mostly Sunny', 'Light Rain', 'Heavy Rain']
        global weather_pick_list
        current_weather = random.choice(weather_list)
        self.weather_pick_list.append(current_weather)
