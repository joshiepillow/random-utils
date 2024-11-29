from pynput import keyboard, mouse
import time


on = False

def on_activate_p():
	global on
	if (on):
		on = False
	else:
		on = True

with keyboard.GlobalHotKeys({
	'p': on_activate_p}) as h:
	h.join()

while True:
	if (on):
		mouse.Controller.click(mouse.Button.left)
	time.sleep(0.03)
