import mouse
import keyboard
import win32gui

position = mouse.get_position()
print(position)
#mouse.move(10,10,absolute=False, duration=0.2)
#mouse.press(button='left')
#keyboard.write('The ',delay=0.2)
#windows = win32gui.GetActiveWindow()
#print(windows)
keyboard.write('a',delay=5)
keyboard.write('a',delay=1)
keyboard.send('space')
keyboard.send('enter')
keyboard.send(57)
keyboard.write('b',delay=0.2)