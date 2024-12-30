distance = 0
start_time = 0
stop_time = 0
running_time = 0
speed_ = 100
diameter = 1

def on_button_pressed_a():
    global start_time
    start_time = input.running_time() / 1000
    servos.P0.run(speed_)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global stop_time, running_time
    stop_time = input.running_time() / 1000
    running_time += stop_time - start_time
    servos.P0.run(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_number(distance)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    global distance
    distance = Math.round(running_time * (2 * (3.1415926585 * (diameter / 2))) * (speed_ / 100))
basic.forever(on_forever)

# input.onButtonPressed(Button.A, function () {
# servos.P0.run(speed_)
# })
# input.onButtonPressed(Button.B, function () {
# stoped_time = times
# running_time = times - (times - stoped_time) + past_running_time
# past_running_time = running_time
# servos.P0.run(0)
# })
# input.onLogoEvent(TouchButtonEvent.Pressed, function () {
# basic.showNumber(running_time)
# })
# let distance = 0
# let past_running_time = 0
# let times = 0
# let stoped_time = 0
# let running_time = 0
# let speed_ = 0
# speed_ = 100
# let diameter = 1
# running_time = 0
# stoped_time = 0
# basic.forever(function () {
# times = input.runningTime() / 1000
# distance = Math.round(running_time * (2 * (3.1415926585 * (diameter / 2))) * (speed_ / 100))
# })