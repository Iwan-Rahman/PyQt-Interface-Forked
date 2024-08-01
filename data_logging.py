#Not entirely sure this will work, as I am still working on it
import csv
import logging
import json
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

def setup_logging():
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(message):
    logging.info(message)

def read_data_from_file(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
    except Exception as e:
        log_message(f"Failed to read CSV file: {e}")
        print(f"Failed to read CSV file: {e}")
    return data

def snap_screen(main_window):
    screen = QPixmap.grabWindow(main_window.winId())
    return screen

def save_screen(pixmap, file_name):
    pixmap.save(file_name)

def upload_file(file_path):
    try:
        data = read_data_from_file(file_path)
        log_message(f"CSV file content read successfully: {data}")
        print(f"CSV file content: {data}")
    except Exception as e:
        log_message(f"Failed to read CSV file: {e}")
        print(f"Failed to read CSV file: {e}")

def save_live_data(live_data, file_name):
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(live_data)
        log_message(f"Live data saved successfully: {file_name}")
    except Exception as e:
        log_message(f"Failed to save live data: {e}")
        print(f"Failed to save live data: {e}")

def save_all_data(live_data, previous_data, file_name):
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write previous data
            writer.writerow(['Previous Data'])  
            writer.writerows(previous_data)
            # Write live data
            writer.writerow(['Live Data']) 
            writer.writerows(live_data)
        log_message(f"All data saved successfully: {file_name}")
    except Exception as e:
        log_message(f"Failed to save all data: {e}")
        print(f"Failed to save all data: {e}")

def save_and_upload(main_window, live_data, previous_data):

    live_data_file_name, _ = QFileDialog.getSaveFileName(main_window, "Save Live Data", "", "CSV Files (*.csv)")
    if live_data_file_name:
        save_live_data(live_data, live_data_file_name)
    
    all_data_file_name, _ = QFileDialog.getSaveFileName(main_window, "Save All Data", "", "CSV Files (*.csv)")
    if all_data_file_name:
        save_all_data(live_data, previous_data, all_data_file_name)
    
    csv_file, _ = QFileDialog.getOpenFileName(main_window, "Open CSV File", "", "CSV Files (*.csv)")
    if csv_file:
        upload_file(csv_file)