input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    control.reset()
})
input.onButtonPressed(Button.A, function () {
    start_time = input.runningTime() / 1000
    servos.P0.run(speed_)
})
input.onButtonPressed(Button.AB, function () {
    if (switch_for_reverse == 1) {
        switch_for_reverse = 0
    } else {
        switch_for_reverse = 1
    }
})
input.onButtonPressed(Button.B, function () {
    stop_time = input.runningTime() / 1000
    running_time += stop_time - start_time
    servos.P0.run(0)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showNumber(distance)
    basic.pause(200)
    basic.clearScreen()
})
let distance = 0
let running_time = 0
let stop_time = 0
let switch_for_reverse = 0
let speed_ = 0
let start_time = 0
let diameter = 1
basic.forever(function () {
    distance = Math.round(running_time * (2 * (3.1415926585 * (diameter / 2))) * (speed_ / 100))
})
basic.forever(function () {
    if (switch_for_reverse == 0) {
        speed_ = 100
    } else {
        speed_ = -100
    }
})
