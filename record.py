
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Key
import json
import sys
import time

f = open("mouselogs.txt", "w")

clicks = []
pressTime = 0
releaseTime = 0
def on_click(x,y,button,ispressed):
    global pressTime, releaseTime
    isdoublepress = False
    if ispressed:
        pressTime = time.time()

    if not ispressed:
        releaseTime = time.time()
    if(ispressed == False):
        diff = abs(pressTime - releaseTime)
        print(diff)
        if diff <= 0.1:
            isdoublepress = True
            print("double clicked")
    if(ispressed == False):
        dict = {"mouse": True, "x": x, "y": y, "duration": 0 if isdoublepress else 1}
        clicks.append(dict)
        # print(clicks)
def on_release(keys):
    if keys != Key.esc:
        print('{0} release'.format(
            keys.char))
        print(type(keys.char))
        dict = {"mouse": False, "keypressed": keys.char}
        clicks.append(dict)
        print(clicks)
    if keys == Key.esc:
        print("Escape pressed, end string in file")
        f.write(json.dumps(clicks))
        f.close()
        sys.exit()

with keyboard.Listener(on_release=on_release) as k_listener, mouse.Listener(on_click=on_click) as m_listener:
    k_listener.join()
    m_listener.join()
