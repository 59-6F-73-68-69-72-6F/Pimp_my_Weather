from PyQt6.QtGui import QPixmap, QFont
import os

COLOR = "#dedbd2"
FONT_SIZE = 15
FONT_WEIGHT = 600
SCRIPT_PATH = script_path = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = "\icons\{}.png"


def _reset_forecast_day_panel(d_mor, d_aft, d_feel, d_date):
    d_mor.setText(f"Morning\n--- C°")
    d_aft.setText(f"Afternoon\n--- C°")
    d_feel.setText(f"Feels Like: --- C°")
    d_date.setText(f"Date")
    
    
def reset_ui_elements(window):
    # Reset City Title and Averages (as in original gui.py reset_ui)
    window.city_title.setText("CITY")
    window.city_title.setStyleSheet(f"color:{COLOR}")
    window.city_title.setFont(QFont("Nimbus Sans, Bold", 35, FONT_WEIGHT))
    window.temp.setText("Average Temperature: 0 C°")
    window.humidity.setText("Average Humidity: 0 %")
    window.wind_speed.setText("Average Wind Speed: 0 m/s")

    # Reset Today's Weather (as in original gui.py reset_ui)
    window.today_temp.setText("0 C°")
    window.today_min.setText("Minimal: 0 C°")
    window.today_max.setText("Maximal: 0 C°")
    window.today_feel_like.setText("Feels Like: 0 C°")
    window.today_humidity.setText("Humidity: 0 %")
    window.today_wind.setText("Wind Speed: 0 m/s")
    window.today_pressure.setText("Pressure: 0 hPa")
    window.icon_today.setPixmap(QPixmap("")) # Clear icon

    # RESET FORECAST TEXT DATA
    _reset_forecast_day_panel(window.day_1_mor, window.day_1_aft, window.day_1_fl, window.day_1_date)
    _reset_forecast_day_panel(window.day_2_mor, window.day_2_aft, window.day_2_fl, window.day_2_date)
    _reset_forecast_day_panel(window.day_3_mor, window.day_3_aft, window.day_3_fl, window.day_3_date)
    _reset_forecast_day_panel(window.day_4_mor, window.day_4_aft, window.day_4_fl, window.day_4_date)
    _reset_forecast_day_panel(window.day_5_mor, window.day_5_aft, window.day_5_fl, window.day_5_date)

    # Clear forecast icons
    window.icon_1.setPixmap(QPixmap(""))
    window.icon_2.setPixmap(QPixmap(""))
    window.icon_3.setPixmap(QPixmap(""))
    window.icon_4.setPixmap(QPixmap(""))
    window.icon_5.setPixmap(QPixmap(""))
    
    
def _update_weather_day(d_mor, v_mor, d_aft, v_aft, d_feel, v_feel, d_date, v_date):
    d_mor.setText(f"Morning\n{v_mor} C°")
    d_aft.setText(f"Afternoon\n{v_aft} C°")
    d_feel.setText(f"Feels Like: {v_feel} C°")
    d_date.setText(f"{v_date}")


def update_forecast_panel(window, forecast_data):  
    # UPDATE CITY TITLE
    window.city_title.setText(f"{window.last_searched_city.capitalize()}")
    window.city_title.setStyleSheet(f"color:{COLOR}")
    window.city_title.setFont(QFont("Nimbus Sans, Bold",30,FONT_WEIGHT))
    
    # UPDATE WEATHER FORECAST AVERAGES
    window.temp.setText(f"Average Temperature: {round(forecast_data[0][3])} C°")
    window.humidity.setText(f"Average Humidity: {round(forecast_data[0][6])} %")
    window.wind_speed.setText(f"Average Wind Speed: {round(forecast_data[0][5])} m/s")
                           
    # UPDATE FORECAST TEXT DATA
    _update_weather_day(window.day_1_mor, forecast_data[0][1], window.day_1_aft, forecast_data[0][2], window.day_1_fl, forecast_data[0][4], window.day_1_date, forecast_data[0][0])
    _update_weather_day(window.day_2_mor, forecast_data[1][1], window.day_2_aft, forecast_data[1][2], window.day_2_fl, forecast_data[1][4], window.day_2_date, forecast_data[1][0])
    _update_weather_day(window.day_3_mor, forecast_data[2][1], window.day_3_aft, forecast_data[2][2], window.day_3_fl, forecast_data[2][4], window.day_3_date, forecast_data[2][0])
    _update_weather_day(window.day_4_mor, forecast_data[3][1], window.day_4_aft, forecast_data[3][2], window.day_4_fl, forecast_data[3][4], window.day_4_date, forecast_data[3][0])
    _update_weather_day(window.day_5_mor, forecast_data[4][1], window.day_5_aft, forecast_data[4][2], window.day_5_fl, forecast_data[4][4], window.day_5_date, forecast_data[4][0])
    
    # UPDATE FORECAST ICONS
    forecast_icons = [window.icon_1, window.icon_2, window.icon_3, window.icon_4, window.icon_5]
    for i in range(len(forecast_icons)):
        if i < len(forecast_data):
            icon_code = forecast_data[i][7] 
            icon_path = SCRIPT_PATH + "/" + ICON_PATH.format(icon_code)
            if os.path.exists(icon_path):
                forecast_icons[i].setPixmap(QPixmap(icon_path))
            else:
                forecast_icons[i].setPixmap(QPixmap(""))                


def update_today(window,weather_today):
    # UPDATE TODAY TEXT DATA
    window.today_temp.setText(f"{weather_today['temp']} C°")
    window.today_min.setText(f"Minimal: {weather_today['min_temp']} C°")
    window.today_max.setText(f"Maximal: {weather_today['max_temp']} C°")
    window.today_feel_like.setText(f"Feels Like: {weather_today['feels_like']} C°")
    window.today_humidity.setText(f"Humidity: {weather_today['humidity']} %")
    window.today_wind.setText(f"Wind Speed: {weather_today['wind_speed']} m/s")
    window.today_pressure.setText(f"Pressure: {weather_today['pressure']} hPa")
    
    # UPDATE TODAY ICON
    icon_code = weather_today["icon"]
    icon_path = ICON_PATH.format(icon_code)
    if os.path.exists(icon_path):
        window.icon_today.setPixmap(QPixmap(icon_path))
    else:
        window.icon_today.setPixmap(QPixmap(""))
    
