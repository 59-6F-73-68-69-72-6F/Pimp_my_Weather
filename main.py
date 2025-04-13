import gui
import weather_api as weather
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QThread
import sys


# Initialize the application
app = QApplication(sys.argv)

# Set application
main_window = gui.WeatherAppGUI()
weather_worker = weather.WeatherPicker()

# Create a thread for the weather worker to run in background
# This is to prevent the GUI from freezing during long operations
search_thread = QThread()
weather_worker.moveToThread(search_thread)

# Connect weather worker signals and slots to the main_window 
main_window.search_requested.connect(weather_worker.search)

# Connect the weather worker to the main window to update the UI
weather_worker.weather_ready.connect(main_window.display_weather_data)

# Connect the thread to start when the search is requested
app.aboutToQuit.connect(search_thread.quit)
search_thread.finished.connect(weather_worker.deleteLater)
search_thread.start()

# Set the main window title
main_window.show()
sys.exit(app.exec())
