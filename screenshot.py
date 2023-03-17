import time
import datetime
import tkinter as tk
from selenium import webdriver
import subprocess

def take_screenshot():
    # Get the URL and time interval from the user inputs
    url = url_entry.get()
    interval = interval_entry.get()

    # Check if both fields have been filled in
    if url and interval:
        # Set up Chrome driver
        driver = webdriver.Chrome()

        while True:
            # Navigate to the website
            driver.get(url)

            # Wait for the website to load
            time.sleep(5)

            # Take a screenshot of the Chrome window
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"screenshot_{timestamp}.png"
            driver.save_screenshot(filename)

            # Wait for the specified interval before taking another screenshot
            time.sleep(int(interval))
    else:
        # Display an error message if either field is empty
        error_label.config(text="Please enter a URL and interval.")

# Create the UI
root = tk.Tk()
root.title("Screenshot Taker")
root.geometry("500x300")

# URL label and entry box
url_label = tk.Label(root, text="URL:",pady=10)
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

# Interval label and entry box
interval_label = tk.Label(root, text="Interval (in seconds):",pady=10)
interval_label.pack()
interval_entry = tk.Entry(root)
interval_entry.pack()

# Screenshot button
screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack()

text_label = tk.Label(root, text="Developed by Jordan Junior")
text_label.pack()

# Error label
error_label = tk.Label(root, fg="red")
error_label.pack()

# Hide the console window
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

if __name__ == '__main__':
    subprocess.call(["python", "main.py"], startupinfo=startupinfo)