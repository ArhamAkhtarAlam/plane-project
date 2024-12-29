input.onButtonPressed(Button.A, function () {
    running_time = times - (times - stoped_time)
    servos.P0.run(speed_)
})
input.onButtonPressed(Button.B, function () {
    stoped_time = times
    servos.P0.run(0)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showNumber(distance)
})
let distance = 0
let times = 0
let stoped_time = 0
let running_time = 0
let speed_ = 0
speed_ = 100
let diameter = 1
running_time = 0
stoped_time = 0
basic.forever(function () {
    times = input.runningTime() / 100
    distance = Math.round(running_time * (2 * (3.1415926585 * (diameter / 2))) * (speed_ / 100))
})
