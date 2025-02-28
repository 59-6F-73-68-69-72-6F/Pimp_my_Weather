import requests
import tkinter as tk

API_KEY = "YOUR API"
class Weather:

    def __init__(self):
        self.url = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}"
        self.url_today = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    
    def get_weather_forecast(self,city):
        self.result = requests.get(self.url.format(city,API_KEY))
        self.result.raise_for_status()
        self.data = self.result.json()
        self.meteo_hub = []
        
        for n in range (2,len(self.data["list"]),2):
            self.meteo = {
                "date": self.data["list"][n]["dt_txt"],
                "icon": self.data["list"][n]["weather"][0]["icon"],
                "temp": self.data["list"][n]["main"]["temp"],
                "min_temp": self.data["list"][n]["main"]["temp_min"],
                "max_temp": self.data["list"][n]["main"]["temp_max"],
                "feels_like": self.data["list"][n]["main"]["feels_like"],
                "wind_speed": self.data["list"][n]["wind"]["speed"],
                "humidity": self.data["list"][n]["main"]["humidity"],
            }
            self.meteo_hub.append(self.meteo)
        
        self.day_1_dic = {"morning": self.meteo_hub[1],"afternoon": self.meteo_hub[2]}
        self.day_2_dic = {"morning": self.meteo_hub[5],"afternoon": self.meteo_hub[6]}
        self.day_3_dic = {"morning": self.meteo_hub[9],"afternoon": self.meteo_hub[10]}
        self.day_4_dic = {"morning": self.meteo_hub[13],"afternoon": self.meteo_hub[14]}
        self.day_5_dic = {"morning": self.meteo_hub[17],"afternoon": self.meteo_hub[18]}
        
        @staticmethod
        def day_gen(day_entry):
            day_icon = day_entry["morning"]["icon"]
            day_date = day_entry["morning"]["date"].split(" ")[0]
            day_mor = round((day_entry["morning"]["min_temp"])-273.15)
            day_aft = round((day_entry["afternoon"]["max_temp"])-273.15)
            day_temp_avg = (day_mor + day_aft)/2
            day_feel_like = round((day_entry["morning"]["feels_like"])-273.15)
            day_humidity = round((day_entry["morning"]["humidity"]+day_entry["afternoon"]["humidity"])/2,2)
            day_wind = round((day_entry["morning"]["wind_speed"]+day_entry["afternoon"]["wind_speed"])/2,2)
            day_final = (day_date,day_mor,day_aft,day_temp_avg,day_feel_like,day_wind,day_humidity,day_icon)
            return day_final

        self.day1 = day_gen(self.day_1_dic)
        self.day2 = day_gen(self.day_2_dic)
        self.day3 = day_gen(self.day_3_dic)
        self.day4 = day_gen(self.day_4_dic)
        self.day5 = day_gen(self.day_5_dic)
        
        return self.day1,self.day2,self.day3,self.day4,self.day5
    
    def get_weather_today(self,city=None):
        self.result_today = requests.get(self.url_today.format(city,API_KEY))
        self.result_today.raise_for_status()
        self.data_today = self.result_today.json()
        
        self.meteo_today = {
            "temp": round(self.data_today["main"]["temp"]-273.15),
            "min_temp": round(self.data_today["main"]["temp_min"]-273.15),
            "max_temp": round(self.data_today["main"]["temp_max"]-273.15),
            "feels_like": round(self.data_today["main"]["feels_like"]-273.15),
            "wind_speed": self.data_today["wind"]["speed"],
            "humidity": self.data_today["main"]["humidity"],
            "pressure": self.data_today["main"]["pressure"],
            "icon": self.data_today["weather"][0]["icon"],    
        }
        
        return self.meteo_today
