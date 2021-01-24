from microbit import *

WAIT, COUNT, RESULT = range(3)
state = WAIT
start_time = 0
distance = 0

def splash_screen():
    display.show(Image("90000:09000:99900:09000:00900"), wait=False)

def thunder_screen():
    thunder = [
        Image("00000:00000:00900:00000:00000"),
        Image("00000:09990:09090:09990:00000"),
        Image("99999:90009:90009:90009:99999"),
    ]
    display.show(thunder, delay = 300, loop=True, wait=False)

def wait_screen():
    thunderCount = [
        Image("90000:09000:99909:09000:00900"),
        Image("90000:09000:99900:09000:00900"),
    ]
    display.show(thunderCount, loop=True, wait= False, delay=500)

def handle_wait_state():
    global state, start_time
    if button_a.was_pressed():
        start_time = running_time()
        wait_screen()
        state = COUNT
        
def handle_count_state():
    global state, start_time, distance
    if button_a.was_pressed():
        start_time = 0
        splash_screen()
        state = WAIT
    if button_b.was_pressed():
        distance = (((running_time() - start_time) * 0.34) / 1000)
        s = "{:.2f}".format(distance)
        thunder_screen()
        sleep(2000)
        display.scroll("Distance: " + str(s) + " km")
        display.scroll(("Again? Press B"), loop = True, wait = False)
        state = RESULT
    
def handle_result_state():
    global state
    if button_b.was_pressed():
        splash_screen()
        state = WAIT
        
splash_screen()

while True:
    if state == WAIT:
        handle_wait_state()
    elif state == COUNT:
        handle_count_state()
    elif state == RESULT:
        handle_result_state()