let distance = 0
let start_time = 0
let stop_time = 0
let running_time = 0
let speed_ = 100
let diameter = 1
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    start_time = input.runningTime() / 1000
    servos.P0.run(speed_)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    stop_time = input.runningTime() / 1000
    running_time += stop_time - start_time
    servos.P0.run(0)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    basic.showNumber(distance)
})
basic.forever(function on_forever() {
    
    distance = Math.round(running_time * (2 * (3.1415926585 * (diameter / 2))) * (speed_ / 100))
})
