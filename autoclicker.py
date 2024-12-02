import pyautogui
import time
import keyboard

def autoclicker():
    while True:
        print("Press Ctrl+Alt+A to start the autoclicker.")
        while not keyboard.is_pressed('ctrl+alt+a'):
            time.sleep(0.1)  # Wait for Ctrl + Alt + A to start
        print("Autoclicker started. Press Alt+Ctrl+S to stop.")
        while not keyboard.is_pressed('alt+ctrl+s'):
            pyautogui.click()
            time.sleep(0.1)  # Adjust the interval as needed
        print("Autoclicker stopped.")

autoclicker()
