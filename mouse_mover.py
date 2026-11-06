import pyautogui
import time
from pynput import keyboard
import threading

is_running = False
exit_program = False

def on_press(key):
    global is_running

    if key == keyboard.Key.f8:
        is_running = not is_running

        if is_running:
            print("\n🟢 Mouse Mover: ON")
        else:
            print("\n🔴 Mouse Mover: OFF")


def mouse_mover():
    while not exit_program:
        if is_running:
            x, y = pyautogui.position()

            pyautogui.moveTo(x + 1, y, duration=0.2)
            time.sleep(0.3)
            pyautogui.moveTo(x, y, duration=0.2)

            print("Mouse moved!")

            time.sleep(5)
        else:
            time.sleep(0.1)


print("==============================")
print("       MOUSE MOVER")
print("==============================")
print("F8       : Toggle ON / OFF")
print("Ctrl + C : Exit program")
print("==============================")
print("🔴 Current Status: OFF")

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    mouse_mover()
except KeyboardInterrupt:
    print("\nMouse mover stopped.")
finally:
    exit_program = True
    listener.stop()