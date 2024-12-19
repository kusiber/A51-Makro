import pyautogui
import pydirectinput
import time
import threading
import keyboard

running = False

def mouse_click():
    while running:
        pyautogui.mouseDown(button='right')
        pyautogui.mouseDown(button='left')
        time.sleep(0.1)
        pyautogui.mouseUp(button='left')
        time.sleep(120)

def press_e():
    while running:
        pydirectinput.keyDown('e')
        time.sleep(0.01)
        pydirectinput.keyUp('e')
        time.sleep(0.01)

def start_on_f10():
    global running
    global mouse_thread
    print("F10 Bas baslasin")
    keyboard.wait('F10')
    running = True
    print("Basladi")
    mouse_thread = threading.Thread(target=mouse_click)
    mouse_thread.start()
    press_e()

def stop_on_f10():
    global running
    global mouse_thread
    print("F10")
    keyboard.wait('F10')
    print("Durdu")
    print("RHYS")
    running = False
    mouse_thread.join()

start_thread = threading.Thread(target=start_on_f10)
start_thread.start()

while True:
    if running:
        stop_on_f10()
        break
    time.sleep(1)
