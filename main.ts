function Tobbie_Stop () {
    pins.digitalWritePin(DigitalPin.P13, 0)
    pins.digitalWritePin(DigitalPin.P14, 0)
}
function Tobbie_Walk () {
    pins.digitalWritePin(DigitalPin.P13, 1)
    pins.digitalWritePin(DigitalPin.P14, 0)
}
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # . . . #
        . . . . .
        . . # . .
        . # . # .
        # . . . #
        `)
    Tobbie_Walk()
    basic.pause(5001)
    Tobbie_Stop()
    basic.showLeds(`
        # . . . #
        . . . . .
        # . . . #
        . # . # .
        . . # . .
        `)
})
input.onSound(DetectedSound.Loud, function () {
    TobbieClapWalk += 1
    if (TobbieClapWalk == 1) {
        Tobbie_Walk()
        control.waitMicros(5000000)
        Tobbie_Stop()
    }
})
let TobbieClapWalk = 0
TobbieClapWalk = 0
basic.forever(function () {
    basic.showNumber(TobbieClapWalk)
})
