def on_logo_long_pressed():
    control.reset()
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    global start_time
    start_time = input.running_time() / 1000
    servos.P0.run(speed_)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global switch_for_reverse
    if switch_for_reverse == 1:
        switch_for_reverse = 0
    else:
        switch_for_reverse = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global stop_time, running_time
    stop_time = input.running_time() / 1000
    running_time += stop_time - start_time
    servos.P0.run(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_number(distance)
    basic.pause(200)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

distance = 0
running_time = 0
stop_time = 0
switch_for_reverse = 0
speed_ = 0
start_time = 0
diameter = 1

def on_forever():
    global distance
    distance = Math.round(running_time * (2 * (3.1415926585 * (diameter / 2))) * (speed_ / 100))
basic.forever(on_forever)

def on_forever2():
    global speed_
    if switch_for_reverse == 0:
        speed_ = 100
    else:
        speed_ = -100
basic.forever(on_forever2)
