from tkinter import *
import requests


API_KEY = "a09650f906ab71989f0856575cd597c8"
url = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}"
url_today = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

#---------------------GET WEATHER------------------------------
def get_weather(city = None):
    result = requests.get(url.format(city,API_KEY))
    result_today = requests.get(url_today.format(city,API_KEY))
    result.raise_for_status()
    result_today.raise_for_status()
    data_today = result_today.json()
    data = result.json()
    meteo_hub = []
    
    meteo_today = {
        "icon": data_today["weather"][0]["icon"],
        "temp": round(data_today["main"]["temp"]-273.15),
        "min_temp": round(data_today["main"]["temp_min"]-273.15),
        "max_temp": round(data_today["main"]["temp_max"]-273.15),
        "feels_like": round(data_today["main"]["feels_like"]-273.15),
        "wind_speed": data_today["wind"]["speed"],
        "humidity": data_today["main"]["humidity"],
        "pressure": data_today["main"]["pressure"],
    }
    
    for n in range (2,len(data["list"]),2):
        meteo ={
            "date": data["list"][n]["dt_txt"],
            "icon": data["list"][n]["weather"][0]["icon"],
            "temp": data["list"][n]["main"]["temp"],
            "min_temp": data["list"][n]["main"]["temp_min"],
            "max_temp": data["list"][n]["main"]["temp_max"],
            "feels_like": data["list"][n]["main"]["feels_like"],
            "wind_speed": data["list"][n]["wind"]["speed"],
            "humidity": data["list"][n]["main"]["humidity"],
        }
        meteo_hub.append(meteo)
        
    
    day_1 = {"morning": meteo_hub[1],"afternoon": meteo_hub[2]}
    day_2 = {"morning": meteo_hub[5],"afternoon": meteo_hub[6]}
    day_3 = {"morning": meteo_hub[9],"afternoon": meteo_hub[10]}
    day_4 = {"morning": meteo_hub[13],"afternoon": meteo_hub[14]}
    day_5 = {"morning": meteo_hub[17],"afternoon": meteo_hub[18]}
    
    def day_gen(day_entry):
    	day_icon = day_entry["morning"]["icon"]
    	day_date = day_entry["morning"]["date"].split(" ")[0]
    	day_mor = round((day_entry["morning"]["min_temp"])-273.15)
    	day_aft = round((day_entry["afternoon"]["max_temp"])-273.15)
    	day_temp_avg = (day_mor+day_aft)/2
    	day_feel_like = round((day_entry["morning"]["feels_like"])-273.15)
    	day_humidity = round((day_entry["morning"]["humidity"]+day_entry["afternoon"]["humidity"])/2,2)
    	day_wind = round((day_entry["morning"]["wind_speed"]+day_entry["afternoon"]["wind_speed"])/2,2)
    	day_final = (day_date,day_mor,day_aft,day_temp_avg,day_feel_like,day_wind,day_humidity,day_icon)
    	return day_final
    	
    day1 = day_gen(day_1)
    day2 = day_gen(day_2)
    day3 = day_gen(day_3)
    day4 = day_gen(day_4)
    day5 = day_gen(day_5)
    
    return day1,day2,day3,day4,day5,meteo_today

#----------------SEARCH FUNCTION-------------------
def update_weather(d_mor,v_mor,d_aft,v_aft,d_feel,v_feel,d_date,v_date):
    	canvas.itemconfig(d_mor, text=f" Morning\n  {v_mor} C°")
    	canvas.itemconfig(d_aft, text=f" Afternoon\n  {v_aft} C°")
    	canvas.itemconfig(d_feel, text=f"Feels Like:{round(v_feel)} C°")
    	canvas.itemconfig(d_date, text=f"{v_date}")

def search():
    newcity = search_bar.get()
    weather = get_weather(newcity)
    
    try:
        
        canvas.itemconfig(city, text=f"{newcity.capitalize()}")
        canvas.itemconfig(temp, text=f"Average Tempeture: {round(weather[0][3])} C°")
        canvas.itemconfig(humidity, text=f"Average Humidity: {round(weather[0][6])} %")
        canvas.itemconfig(wind_speed, text=f"Average Wind Speed: {round(weather[0][5])} m/s")
        #----------------TODAY-------------------
        canvas.itemconfig(today_temp, text=f"{weather[5]['temp']} C°")
        canvas.itemconfig(today_min, text=f" Minimal:  {weather[5]['min_temp']} C°")
        canvas.itemconfig(today_max, text=f" Maximal:  {weather[5]['max_temp']} C°")
        canvas.itemconfig(today_feel_like, text=f"Feels Like:  {weather[5]['feels_like']} C°")
        canvas.itemconfig(today_humidity, text=f"Humidity:  {weather[5]['humidity']} %")
        canvas.itemconfig(today_wind, text=f"Wind Speed:  {weather[5]['wind_speed']} m/s")
        canvas.itemconfig(today_pressure, text=f"Pressure:  {weather[5]['pressure']} hPa")
        #----------------DAY 1-------------------
        update_weather(day1_mor,weather[0][1],day1_aft,weather[0][2],day1_feel_like,weather[0][4],day1_date,weather[0][0])
        #----------------DAY 2-------------------
        update_weather(day2_mor,weather[1][1],day2_aft,weather[1][2],day2_feel_like,weather[1][4],day2_date,weather[1][0])
        #----------------DAY 3-------------------
        update_weather(day3_mor,weather[2][1],day3_aft,weather[2][2],day3_feel_like,weather[2][4],day3_date,weather[2][0])
        #----------------DAY 4-------------------
        update_weather(day4_mor,weather[3][1],day4_aft,weather[3][2],day4_feel_like,weather[3][4],day4_date,weather[3][0])
        #----------------DAY 5-------------------
        update_weather(day5_mor,weather[4][1],day5_aft,weather[4][2],day5_feel_like,weather[4][4],day5_date,weather[4][0])
        #----------------ICON-------------------
        img_1["file"] = "/storage/emulated/0/Python/Weather/icons/{}.png".format(weather[0][7])
        img_2["file"] = "/storage/emulated/0/Python/Weather/icons/{}.png".format(weather[1][7])
        img_3["file"] = "/storage/emulated/0/Python/Weather/icons/{}.png".format(weather[2][7])
        img_4["file"] = "/storage/emulated/0/Python/Weather/icons/{}.png".format(weather[3][7])
        img_5["file"] = "/storage/emulated/0/Python/Weather/icons/{}.png".format(weather[4][7])
        img_today["file"] = "/icons/{}.png".format(weather[5]["icon"])
        
    except requests.exceptions.HTTPError:
        canvas.itemconfig(city, text="City not found")


#----------------MOUSE OVER FUNCTIONS-------------------
def on_enter_day_1(event):
    newcity = search_bar.get()
    weather = get_weather(newcity)
    canvas.itemconfig(temp, text=f"Average Tempeture: {round(weather[0][3])} C°")
    canvas.itemconfig(humidity, text=f"Average Humidity: {round(weather[0][6])} %")
    canvas.itemconfig(wind_speed, text=f"Average Wind Speed: {round(weather[0][5])} m/s")

def on_enter_day_2(event):
    newcity = search_bar.get()
    weather = get_weather(newcity)
    canvas.itemconfig(temp, text=f"Average Tempeture: {round(weather[1][3])} C°")
    canvas.itemconfig(humidity, text=f"Average Humidity: {round(weather[1][6])} %")
    canvas.itemconfig(wind_speed, text=f"Average Wind Speed: {round(weather[1][5])} m/s")

def on_enter_day_3(event):
    newcity = search_bar.get()
    weather = get_weather(newcity)
    canvas.itemconfig(temp, text=f"Average Tempeture: {round(weather[2][3])} C°")
    canvas.itemconfig(humidity, text=f"Average Humidity: {round(weather[2][6])} %")
    canvas.itemconfig(wind_speed, text=f"Average Wind Speed: {round(weather[2][5])} m/s")

def on_enter_day_4(event):
    newcity = search_bar.get()
    weather = get_weather(newcity)
    canvas.itemconfig(temp, text=f"Average Tempeture: {round(weather[3][3])} C°")
    canvas.itemconfig(humidity, text=f"Average Humidity: {round(weather[3][6])} %")
    canvas.itemconfig(wind_speed, text=f"Average Wind Speed: {round(weather[3][5])} m/s")

def on_enter_day_5(event):
    newcity = search_bar.get()
    weather = get_weather(newcity)
    canvas.itemconfig(temp, text=f"Average Tempeture: {round(weather[4][3])} C°")
    canvas.itemconfig(humidity, text=f"Average Humidity: {round(weather[4][6])} %")
    canvas.itemconfig(wind_speed, text=f"Average Wind Speed: {round(weather[4][5])} m/s")

def press_return(event):
    search()
	   
#----------------UI---------------------

window = Tk()
window.title("Pimp my Weather")
window.minsize(width=1095,height=695)
window.maxsize(width=1095,height=695)
background = PhotoImage(file="/storage/emulated/0/Python/Weather/BluePrint.png")
window.bind("<Return>", press_return)


canvas = Canvas(width=1100,height=700)
canvas.create_image(550,350,image=background)

#----------------SEARCH BAR------------------
search_bar = Entry(window,width=35,font=("Arial",20,"bold"),textvariable= "")
search_bar.place(x=473,y=65)

#----------------LABEL-------------------
city = canvas.create_text(300,82,text="City",font=("Arial",30,"bold"),fill="light grey")
temp = canvas.create_text(613,190,text="",font=("Arial",11,"bold"),fill="light grey")
humidity = canvas.create_text(607,220,text="",font=("Arial",11,"bold"),fill="light grey")
wind_speed = canvas.create_text(620,250,text="",font=("Arial",11,"bold"),fill="light grey")

#----------------TODAY------------------
today_temp = canvas.create_text(347,230,text="0 C°",font=("Arial",40,"bold"),fill="light grey")
today_min = canvas.create_text(140,190,text=f"",font=("Arial",11,"bold"),fill="light grey")
today_max = canvas.create_text(140,215,text=f"",font=("Arial",11,"bold"),fill="light grey")
today_feel_like = canvas.create_text(150,240,text=f"",font=("Arial",11,"bold"),fill="light grey")
today_pressure = canvas.create_text(156,265,text=f"",font=("Arial",11,"bold"),fill="light grey")
today_wind = canvas.create_text(163,290,text=f"",font=("Arial",11,"bold"),fill="light grey")
today_humidity = canvas.create_text(140,315,text=f"",font=("Arial",11,"bold"),fill="light grey")

#----------------DAY 1-------------------
day1_mor = canvas.create_text(165,500,text=f" Morning\n--- C°",font=("Arial",16,"bold"),fill="light grey")
day1_aft = canvas.create_text(165,555,text=f" Afternoon\n--- C°",font=("Arial",16,"bold"),fill="light grey")
day1_feel_like = canvas.create_text(170,610,text=f"Feels Like: --- C°",font=("Arial",12,"bold"),fill="light grey")
day1_date = canvas.create_text(170,640,text=f"Date ",font=("Arial",12,"bold"),fill="light grey")
day1_id = canvas.create_text(170,435,text=f"",font=("Arial",50,"bold"),fill="light grey")

#----------------DAY 2-------------------
day2_mor = canvas.create_text(355,500,text=f" Morning\n--- C°",font=("Arial",16,"bold"),fill="light grey")
day2_aft = canvas.create_text(355,555,text=f" Afternoon\n--- C°",font=("Arial",16,"bold"),fill="light grey")
day2_feel_like = canvas.create_text(360,610,text=f"Feels Like: --- C°",font=("Arial",12,"bold"),fill="light grey")
day2_date = canvas.create_text(360,640,text=f"Date ",font=("Arial",12,"bold"),fill="light grey")
day2_id = canvas.create_text(360,435,text=f"",font=("Arial",50,"bold"),fill="light grey")
#----------------DAY 3-------------------
day3_mor = canvas.create_text(545,500,text=f" Morning\n--- C°",font=("Arial",16,"bold"),fill="light grey")
day3_aft = canvas.create_text(545,555,text=f" Afternoon\n--- C°",font=("Arial",16,"bold"),fill="light grey")
day3_feel_like = canvas.create_text(550,610,text=f"Feels Like: --- C°",font=("Arial",12,"bold"),fill="light grey")
day3_date = canvas.create_text(550,640,text=f"Date ",font=("Arial",12,"bold"),fill="light grey")
day3_id = canvas.create_text(550,435,text=f"",font=("Arial",50,"bold"),fill="light grey")
#----------------DAY 4-------------------
day4_mor = canvas.create_text(735,500,text=f" Morning\n--- C°",font=("Arial",16,"bold"),fill="light grey")
day4_aft = canvas.create_text(735,555,text=f" Afternoon\n--- C°",font=("Arial",16,"bold"),fill="light grey")
day4_feel_like = canvas.create_text(740,610,text=f"Feels Like: --- C°",font=("Arial",12,"bold"),fill="light grey")
day4_date = canvas.create_text(740,640,text=f"Date ",font=("Arial",12,"bold"),fill="light grey")
day4_id = canvas.create_text(740,435,text=f"",font=("Arial",50,"bold"),fill="light grey")
#----------------DAY 5-------------------
day5_mor = canvas.create_text(925,500,text=f" Morning\n--- C°",font=("Arial",16,"bold"),fill="light grey")
day5_aft = canvas.create_text(925,555,text=f" Afternoon\n--- C°",font=("Arial",16,"bold"),fill="light grey")
day5_feel_like = canvas.create_text(930,610,text=f"Feels Like: --- C°",font=("Arial",12,"bold"),fill="light grey")
day5_date = canvas.create_text(930,640,text=f"Date ",font=("Arial",12,"bold"),fill="light grey")
day5_id = canvas.create_text(930,435,text=f"",font=("Arial",50,"bold"),fill="light grey")
#---------------WEATHER ICON--------------
img_1 = PhotoImage(file="")
img_icon_1 = canvas.create_image(165,420,image=img_1)
img_2 = PhotoImage(file="")
img_icon_2 = canvas.create_image(355,420,image=img_2)
img_3 = PhotoImage(file="")
img_icon_3 = canvas.create_image(545,420,image=img_3)
img_4 = PhotoImage(file="")
img_icon_4 = canvas.create_image(735,420,image=img_4)
img_5 = PhotoImage(file="")
img_icon_5 = canvas.create_image(925,420,image=img_5)
img_today = PhotoImage(file="")
img_icon_today = canvas.create_image(340,297,image=img_today)
#----------------MOUSE OVER-------------------
canvas.tag_bind(img_icon_1, "<Enter>", on_enter_day_1)
canvas.tag_bind(img_icon_2, "<Enter>", on_enter_day_2)
canvas.tag_bind(img_icon_3, "<Enter>", on_enter_day_3)
canvas.tag_bind(img_icon_4, "<Enter>", on_enter_day_4)
canvas.tag_bind(img_icon_5, "<Enter>", on_enter_day_5)


canvas.pack()
window.mainloop()
