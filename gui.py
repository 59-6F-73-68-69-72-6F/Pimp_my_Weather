from PyQt6.QtWidgets import QWidget,QLabel,QLineEdit
from PyQt6.QtGui import QFont,QPixmap
from PyQt6.QtCore import QSize,pyqtSignal
import update_ui
import requests
import os



COLOR = "#dedbd2"
FONT_SIZE = 15
FONT_WEIGHT = 600
SCRIPT_PATH = script_path = os.path.dirname(os.path.abspath(__file__))

class WeatherAppGUI(QWidget):
    # Signal to request a search
    search_requested = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        # Set Window
        self.setMinimumSize(1095,695)
        self.setMaximumSize(1095,695)
        self.setWindowTitle("Pimp My Weather")
        # Set Background
        self.background = QLabel(self)
        self.img_background = QPixmap(f"{SCRIPT_PATH}\images\BluePrint.png")
        self.background.setPixmap(self.img_background)
        
        # Set City Title
        self.city_title = self.label_text(35,"CITY           ",226,50)
        self.temp = self.label_text(11,"Average Temperature: 0 C°   ",515,210)
        self.humidity = self.label_text(11,"Average Humidity: 0 %   ",515,230)
        self.wind_speed = self.label_text(11,"Average Wind Speed: 0 m/s   ",515,250)
        
        # Set Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setFont(QFont("Sans serif",15))
        self.search_bar.resize(QSize(500,35))
        self.search_bar.move(505,65)
        self.search_bar.returnPressed.connect(self._on_search_bar_return) # Press Enter to search 
        
        # Set TODAY
        self.today_temp = self.label_text(35,"0 C°    ",300,190)
        self.today_min = self.label_text(11,"Minimal: 0 C°   ",90,190)
        self.today_max = self.label_text(11,"Maximal: 0 C°   ",90,210)
        self.today_feel_like = self.label_text(11,"Feels Like: 0 C°   ",90,230)
        self.today_humidity = self.label_text(11,"Humidity: 0 %    ",90,250)
        self.today_wind = self.label_text(11,"Wind Speed: 0 m/s        ",90,270)
        self.today_pressure = self.label_text(11,"Pressure: 0 hPa    ",90,290)
        self.icon_today = self.create_icon_label(300, 260)
        
        # Set DAY 1
        self.day_1_mor = self.label_text(FONT_SIZE,"Morning\n--- C°",130,465)
        self.day_1_aft = self.label_text(FONT_SIZE,"Afternoon\n--- C°",130,525)
        self.day_1_fl = self.label_text(12,"Feels Like: --- C°",110,595)
        self.day_1_date = self.label_text(10,"Date              ",135,628)
        self.icon_1 = self.create_icon_label(125, 370)
        
        # Set DAY 2
        self.day_2_mor = self.label_text(FONT_SIZE,"Morning\n--- C°",320,465)
        self.day_2_aft = self.label_text(FONT_SIZE,"Afternoon\n--- C°",320,525)
        self.day_2_fl = self.label_text(12,"Feels Like: --- C°",300,595)
        self.day_2_date = self.label_text(10,"Date              ",325,628)
        self.icon_2 = self.create_icon_label(315, 370)
        
        # Set DAY 3
        self.day_3_mor = self.label_text(FONT_SIZE,"Morning\n--- C°",510,465)
        self.day_3_aft = self.label_text(FONT_SIZE,"Afternoon\n--- C°",510,525)
        self.day_3_fl = self.label_text(12,"Feels Like: --- C°",490,595)
        self.day_3_date =self.label_text(10,"Date              ",515,628)
        self.icon_3 = self.create_icon_label(505, 370)
        
        # Set DAY 4
        self.day_4_mor = self.label_text(FONT_SIZE,"Morning\n--- C°",700,465)
        self.day_4_aft = self.label_text(FONT_SIZE,"Afternoon\n--- C°",700,525)
        self.day_4_fl = self.label_text(12,"Feels Like: --- C°",680,595)
        self.day_4_date = self.label_text(10,"Date              ",705,628)
        self.icon_4 = self.create_icon_label(695, 370)
        
        # Set DAY 5
        self.day_5_mor = self.label_text(FONT_SIZE,"Morning\n--- C°",890,465)
        self.day_5_aft = self.label_text(FONT_SIZE,"Afternoon\n--- C°",890,525)
        self.day_5_fl = self.label_text(12,"Feels Like: --- C°",870,595)
        self.day_5_date = self.label_text(10,"Date              ",895,628)
        self.icon_5 = self.create_icon_label(885, 370)
        
        # Set Error message
        self.error_label = QLabel(self)
        self.error_label.setFont(QFont("Arial", 11))
        self.error_label.setStyleSheet("color:red")
        self.error_label.move(505,100)
        self.error_label.setWordWrap(True)
        self.error_label.setFixedWidth(490)
        
        
    # Create a label with text
    def label_text(self,font_size,text,xpos,ypos):
        label = QLabel(self)
        label.setText(text)
        label.setFont(QFont("Nimbus Sans, Bold",font_size,FONT_WEIGHT))
        label.setStyleSheet(f"color:{COLOR}")
        label.move(xpos,ypos)
        return label
    
    
    # Create a label for the icon
    def create_icon_label(self, x, y):
        icon_label = QLabel(self)
        icon_label.setPixmap(QPixmap(""))
        icon_label.setScaledContents(True)
        icon_label.setFixedSize(80,80)
        icon_label.move(x,y)
        return icon_label
    
    
    # Triggered when the user press Enter in the search bar
    def _on_search_bar_return(self):
        city = self.search_bar.text().strip()
        try:
            self.last_searched_city = city
            update_ui.reset_ui_elements(self)
            self.error_label.setText("")
            self.city_title.setStyleSheet(f"color:cyan")
            self.city_title.setFont(QFont("Nimbus Sans, Bold",13,FONT_WEIGHT))
            self.search_bar.clear()
            self.search_requested.emit(city) # Connection requested
            if city:
                self.city_title.setText(f"searching for {city.capitalize()}...")
            else:
                self.handle_error("Please enter a city name.")
        except requests.exceptions.HTTPError:
                update_ui.reset_ui_elements(self)
                self.handle_error("Please enter a valide city name.")
            
            
    # Display the weather data updated in the UI
    def display_weather_data(self, weather_today, weather_forecast):
        try:
            update_ui.update_today(self,weather_today)
            update_ui.update_forecast_panel(self,weather_forecast)
        except Exception as e:
            self.handle_error(f"Error displaying data for {self.last_searched_city.capitalize()}.")
        
        
    # Handle errors and reset UI elements
    def handle_error(self, error_message):
        update_ui.reset_ui_elements(self) # Reset UI elements
        self.error_label.setText(error_message)
        self.city_title.setText("Error")
        self.city_title.setStyleSheet("color:red")
        self.city_title.setFont(QFont("Nimbus Sans, Bold", 20, FONT_WEIGHT)) 
    
