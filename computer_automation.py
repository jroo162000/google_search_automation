import pyautogui
import time
import webbrowser

# Open a text editor (Notepad on Windows)
webbrowser.open('https://www.onlinegdb.com/online_python_compiler')

# Wait for the text editor to open
time.sleep(5)

# Type text in the text editor
pyautogui.typewrite('Hello, this is an automated message!', interval=0.1)

# Move the mouse to a specific location
pyautogui.moveTo(100, 100, duration=1)

# Click at the current mouse position
pyautogui.click()

# Scroll down
pyautogui.scroll(-500)
