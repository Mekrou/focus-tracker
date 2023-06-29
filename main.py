import keyboard
import time

start_hotkey = 'ctrl+shift+f'
end_hotkey = 'ctrl+shift+g'
start_time = 0
end_time = 0
focused = False

def start_focus():
    global start_time
    global end_time
    global focused
    focused = True
    start_time = time.time()
    print('Focusing starts now!')
keyboard.add_hotkey(start_hotkey, start_focus)

def get_time_focused():
    global start_time
    global end_time
    return end_time - start_time

def end_focus():
    global start_time
    global end_time
    global focused
    if focused:
        end_time = time.time()
        focused = False
        print(f'Congrats! You focused {get_time_focused()}')
    else:
        print('You cannot end focus time without starting!')
keyboard.add_hotkey(end_hotkey, end_focus)



keyboard.wait()
