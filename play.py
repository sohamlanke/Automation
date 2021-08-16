import pyautogui
import json
pyautogui.FAILSAFE = False
f = open("mouselogs.txt", "r")
data = json.loads(f.read())
for log in data:
    if log['mouse'] == True:
        pyautogui.click(log['x'], log['y'], duration=log['duration'])
    else:
        pyautogui.typewrite(log['keypressed'])