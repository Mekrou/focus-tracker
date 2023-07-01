import keyboard
import time
from csv_model import CSVModel
from datetime import date

start_hotkey = 'ctrl+shift+k'
end_hotkey = 'ctrl+shift+j'
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
    return round(end_time - start_time, 2)

def end_focus():
    global start_time
    global end_time
    global focused
    if focused:
        end_time = time.time()
        focused = False
        print(f'Congrats! You focused {get_time_focused()}')
        model.create([date.today(), get_time_focused(), True])
    else:
        print('You cannot end focus time without starting!')

keyboard.add_hotkey(end_hotkey, end_focus)

model = CSVModel('focus_time.csv')
def init_csv():
    global model
    model.create(['Date', 'Time', 'Exercised'])

keyboard.wait()
