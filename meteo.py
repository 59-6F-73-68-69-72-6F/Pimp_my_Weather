from tkinter import *
import requests
from the_weather import Weather

COLOR_TEXT = "light grey"
ICON = "/Users/Yoshiro/PycharmProjects/100 Days of Code - The Complete Python Pro Bootcamp/Day-35/icons/{}.png"

#----------------SEARCH FUNCTION-------------------
def update_weather(d_mor,v_mor,d_aft,v_aft,d_feel,v_feel,d_date,v_date):
        canvas.itemconfig(d_mor, text=f" Morning\n  {v_mor} C°")
        canvas.itemconfig(d_aft, text=f" Afternoon\n  {v_aft} C°")
        canvas.itemconfig(d_feel, text=f"Feels Like:{round(v_feel)} C°")
        canvas.itemconfig(d_date, text=f"{v_date}")

def search():
    newcity = search_bar.get()
    weather_forecast = Weather().get_weather_forecast(newcity)
    weather_today = Weather().get_weather_today(newcity)
    
    
    try:
        
        canvas.itemconfig(city, text=f"{newcity.capitalize()}")
        canvas.itemconfig(temp, text=f"Average Tempeture: {round(weather_forecast[0][3])} C°")
        canvas.itemconfig(humidity, text=f"Average Humidity: {round(weather_forecast[0][6])} %")
        canvas.itemconfig(wind_speed, text=f"Average Wind Speed: {round(weather_forecast[0][5])} m/s")
        #----------------TODAY-------------------
        canvas.itemconfig(today_temp, text=f"{weather_today['temp']} C°")
        canvas.itemconfig(today_min, text=f" Minimal:  {weather_today['min_temp']} C°")
        canvas.itemconfig(today_max, text=f" Maximal:  {weather_today['max_temp']} C°")
        canvas.itemconfig(today_feel_like, text=f"Feels Like:  {weather_today['feels_like']} C°")
        canvas.itemconfig(today_humidity, text=f"Humidity:  {weather_today['humidity']} %")
        canvas.itemconfig(today_wind, text=f"Wind Speed:  {weather_today['wind_speed']} m/s")
        canvas.itemconfig(today_pressure, text=f"Pressure:  {weather_today['pressure']} hPa")
        
        #----------------DAY 1-------------------
        update_weather(day1_mor,weather_forecast[0][1],day1_aft,weather_forecast[0][2],day1_feel_like,weather_forecast[0][4],day1_date,weather_forecast[0][0])
        #-------DAY 2---------------------------
        update_weather(day2_mor,weather_forecast[1][1],day2_aft,weather_forecast[1][2],day2_feel_like,weather_forecast[1][4],day2_date,weather_forecast[1][0])
        #-------DAY 3---------------------------
        update_weather(day3_mor,weather_forecast[2][1],day3_aft,weather_forecast[2][2],day3_feel_like,weather_forecast[2][4],day3_date,weather_forecast[2][0])
        #-------DAY 4---------------------------
        update_weather(day4_mor,weather_forecast[3][1],day4_aft,weather_forecast[3][2],day4_feel_like,weather_forecast[3][4],day4_date,weather_forecast[3][0])
        #-------DAY 5---------------------------
        update_weather(day5_mor,weather_forecast[4][1],day5_aft,weather_forecast[4][2],day5_feel_like,weather_forecast[4][4],day5_date,weather_forecast[4][0])
        #----------------ICON-------------------
        imgs[0]["file"] = ICON.format(weather_forecast[0][7])
        imgs[1]["file"] = ICON.format(weather_forecast[1][7])
        imgs[2]["file"] = ICON.format(weather_forecast[2][7])
        imgs[3]["file"] = ICON.format(weather_forecast[3][7])
        imgs[4]["file"] = ICON.format(weather_forecast[4][7])
        imgs[5]["file"] = ICON.format(weather_today["icon"])
        
    except requests.exceptions.HTTPError:
        canvas.itemconfig(city, text="City not found")


#----------------MOUSE OVER FUNCTION-------------------
def on_enter_day(event,index):
    newcity = search_bar.get()
    weather_forecast = Weather().get_weather_forecast(newcity)
    canvas.itemconfig(temp, text=f"Average Tempeture: {round(weather_forecast[index][3])} C°")
    canvas.itemconfig(humidity, text=f"Average Humidity: {round(weather_forecast[index][6])} %")
    canvas.itemconfig(wind_speed, text=f"Average Wind Speed: {round(weather_forecast[index][5])} m/s")

#----------------PRESS RETURN FUNCTION-------------------
def press_return(event):
    search()

#--------------------------------------------UI----------------------------------------------------
window = Tk()
window.title("Pimp my Weather")
window.minsize(width=1095,height=695)
window.maxsize(width=1095,height=695)
background = PhotoImage(file="/Users/Yoshiro/PycharmProjects/100 Days of Code - The Complete Python Pro Bootcamp/Day-35/BluePrint.png")
window.bind("<Return>", press_return)
canvas = Canvas(width=1100,height=700)
canvas.create_image(550,350,image=background)

#----------------SEARCH BAR------------------
search_bar = Entry(window,width=35,font=("Arial",20,"bold"),textvariable= "")
search_bar.place(x=473,y=65)

#----------------LABEL-------------------
city = canvas.create_text(300,82,text="City",font=("Arial",30,"bold"),fill= COLOR_TEXT)
temp = canvas.create_text(613,190,text="",font=("Arial",11,"bold"),fill= COLOR_TEXT)
humidity = canvas.create_text(607,220,text="",font=("Arial",11,"bold"),fill= COLOR_TEXT)
wind_speed = canvas.create_text(620,250,text="",font=("Arial",11,"bold"),fill= COLOR_TEXT)

#----------------TODAY------------------
today_temp = canvas.create_text(347,230,text="0 C°",font=("Arial",40,"bold"),fill= COLOR_TEXT)
today_min = canvas.create_text(140,190,text=f"",font=("Arial",11,"bold"),fill= COLOR_TEXT)
today_max = canvas.create_text(140,215,text=f"",font=("Arial",11,"bold"),fill= COLOR_TEXT)
today_feel_like = canvas.create_text(150,240,text=f"",font=("Arial",11,"bold"),fill= COLOR_TEXT)
today_pressure = canvas.create_text(156,265,text=f"",font=("Arial",11,"bold"),fill= COLOR_TEXT)
today_wind = canvas.create_text(163,290,text=f"",font=("Arial",11,"bold"),fill= COLOR_TEXT)
today_humidity = canvas.create_text(140,315,text=f"",font=("Arial",11,"bold"),fill= COLOR_TEXT)

#----------------DAY 1-------------------
day1_mor = canvas.create_text(165,500,text=f" Morning\n--- C°",font=("Arial",16,"bold"),fill= COLOR_TEXT)
day1_aft = canvas.create_text(165,555,text=f" Afternoon\n--- C°",font=("Arial",16,"bold"),fill= COLOR_TEXT)
day1_feel_like = canvas.create_text(170,610,text=f"Feels Like: --- C°",font=("Arial",12,"bold"),fill= COLOR_TEXT)
day1_date = canvas.create_text(170,640,text=f"Date ",font=("Arial",12,"bold"),fill= COLOR_TEXT)
day1_id = canvas.create_text(170,435,text=f"",font=("Arial",50,"bold"),fill= COLOR_TEXT)
#----------------DAY 2-------------------
day2_mor = canvas.create_text(355,500,text=f" Morning\n--- C°",font=("Arial",16,"bold"),fill= COLOR_TEXT)
day2_aft = canvas.create_text(355,555,text=f" Afternoon\n--- C°",font=("Arial",16,"bold"),fill= COLOR_TEXT)
day2_feel_like = canvas.create_text(360,610,text=f"Feels Like: --- C°",font=("Arial",12,"bold"),fill= COLOR_TEXT)
day2_date = canvas.create_text(360,640,text=f"Date ",font=("Arial",12,"bold"),fill= COLOR_TEXT)
day2_id = canvas.create_text(360,435,text=f"",font=("Arial",50,"bold"),fill= COLOR_TEXT)
#----------------DAY 3-------------------
day3_mor = canvas.create_text(545,500,text=f" Morning\n--- C°",font=("Arial",16,"bold"),fill= COLOR_TEXT)
day3_aft = canvas.create_text(545,555,text=f" Afternoon\n--- C°",font=("Arial",16,"bold"),fill= COLOR_TEXT)
day3_feel_like = canvas.create_text(550,610,text=f"Feels Like: --- C°",font=("Arial",12,"bold"),fill= COLOR_TEXT)
day3_date = canvas.create_text(550,640,text=f"Date ",font=("Arial",12,"bold"),fill= COLOR_TEXT)
day3_id = canvas.create_text(550,435,text=f"",font=("Arial",50,"bold"),fill= COLOR_TEXT)
#----------------DAY 4-------------------
day4_mor = canvas.create_text(735,500,text=f" Morning\n--- C°",font=("Arial",16,"bold"),fill= COLOR_TEXT)
day4_aft = canvas.create_text(735,555,text=f" Afternoon\n--- C°",font=("Arial",16,"bold"),fill= COLOR_TEXT)
day4_feel_like = canvas.create_text(740,610,text=f"Feels Like: --- C°",font=("Arial",12,"bold"),fill= COLOR_TEXT)
day4_date = canvas.create_text(740,640,text=f"Date ",font=("Arial",12,"bold"),fill= COLOR_TEXT)
day4_id = canvas.create_text(740,435,text=f"",font=("Arial",50,"bold"),fill= COLOR_TEXT)
#----------------DAY 5-------------------
day5_mor = canvas.create_text(925,500,text=f" Morning\n--- C°",font=("Arial",16,"bold"),fill= COLOR_TEXT)
day5_aft = canvas.create_text(925,555,text=f" Afternoon\n--- C°",font=("Arial",16,"bold"),fill= COLOR_TEXT)
day5_feel_like = canvas.create_text(930,610,text=f"Feels Like: --- C°",font=("Arial",12,"bold"),fill= COLOR_TEXT)
day5_date = canvas.create_text(930,640,text=f"Date ",font=("Arial",12,"bold"),fill= COLOR_TEXT)
day5_id = canvas.create_text(930,435,text=f"",font=("Arial",50,"bold"),fill= COLOR_TEXT)

#---------------WEATHER ICON--------------
imgs = [PhotoImage(file=""),PhotoImage(file=""),PhotoImage(file=""),PhotoImage(file=""),PhotoImage(file=""),PhotoImage(file="")]

x_pos = [165, 355, 545, 735, 925, 340]
y_pos = [420, 420, 420, 420, 420, 297]

icons = []
for i, (x, y) in enumerate(zip(x_pos, y_pos)):
    icon = canvas.create_image(x, y, image=imgs[i])
    icons.append(icon)

# #----------------MOUSE OVER-------------------
canvas.tag_bind(icons[0], "<Enter>", lambda event: on_enter_day(event,0))
canvas.tag_bind(icons[1], "<Enter>", lambda event: on_enter_day(event,1))
canvas.tag_bind(icons[2], "<Enter>", lambda event: on_enter_day(event,2))
canvas.tag_bind(icons[3], "<Enter>", lambda event: on_enter_day(event,3))
canvas.tag_bind(icons[4], "<Enter>", lambda event: on_enter_day(event,4))

canvas.pack()
window.mainloop()
