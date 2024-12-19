import pyautogui
import pydirectinput
import time
import threading
import keyboard

running = False
use_mouse_click = True
mouse_click_delay = 90  # Varsayılan bekleme süresi
key_press_delay = 600   # Varsayılan tuş basıp bırakma bekleme süresi
mouse_thread = None
key_thread = None
two_key_thread = None

def mouse_click():
    while running:
        pyautogui.mouseDown(button='right')
        pyautogui.mouseDown(button='left')
        time.sleep(0.1)
        pyautogui.mouseUp(button='left')
        time.sleep(mouse_click_delay)

def press_e():
    while running:
        pydirectinput.keyDown('e')
        time.sleep(0.01)
        pydirectinput.keyUp('e')
        time.sleep(0.01)

def two_key_press():
    while running:
        pydirectinput.keyDown('2')
        time.sleep(key_press_delay)
        pydirectinput.keyUp('2')
        time.sleep(key_press_delay)

def start_threads():
    global mouse_thread, key_thread, two_key_thread

    if use_mouse_click:
        mouse_thread = threading.Thread(target=mouse_click)
        mouse_thread.start()

    key_thread = threading.Thread(target=press_e)
    key_thread.start()

    two_key_thread = threading.Thread(target=two_key_press)
    two_key_thread.start()

def stop_threads():
    global mouse_thread, key_thread, two_key_thread

    if use_mouse_click and mouse_thread:
        mouse_thread.join()
    if key_thread:
        key_thread.join()
    if two_key_thread:
        two_key_thread.join()

def toggle_running():
    global running

    if running:
        print("F10 - Duruyor")
        running = False
        stop_threads()
    else:
        print("F10 - Başlıyor")
        running = True
        start_threads()

def configure_settings():
    global mouse_click_delay
    global key_press_delay
    global use_mouse_click

    use_mouse_click = input("Hakkımı Helal Ediyorum (e/h): ").strip().lower() == 'e'

    try:
        mouse_click_delay = float(input("Mouse tıklama bekleme süresi (saniye): "))
    except ValueError:
        print("Geçersiz değer, varsayılan 120 saniye kullanılacak.")

    try:
        key_press_delay = float(input("2 tuşuna basıp bırakma bekleme süresi (saniye): "))
    except ValueError:
        print("Geçersiz değer, varsayılan 600 saniye kullanılacak.")

configure_settings()

print("F10 ile başlat/durdur")
while True:
    keyboard.wait('F10')
    toggle_running()
