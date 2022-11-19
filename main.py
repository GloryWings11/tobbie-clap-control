def Tobbie_Stop():
    pins.digital_write_pin(DigitalPin.P13, 0)
    pins.digital_write_pin(DigitalPin.P14, 0)
def Tobbie_Walk():
    pins.digital_write_pin(DigitalPin.P13, 1)
    pins.digital_write_pin(DigitalPin.P14, 0)

def on_button_pressed_a():
    basic.show_leds("""
        # . . . #
                . . . . .
                . . # . .
                . # . # .
                # . . . #
    """)
    Tobbie_Walk()
    basic.pause(5001)
    Tobbie_Stop()
    basic.show_leds("""
        # . . . #
                . . . . .
                # . . . #
                . # . # .
                . . # . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    global TobbieClapWalk
    TobbieClapWalk += 1
    if TobbieClapWalk == 1:
        Tobbie_Walk()
        control.wait_micros(5000000)
        Tobbie_Stop()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

TobbieClapWalk = 0
TobbieClapWalk = 0

def on_forever():
    basic.show_number(TobbieClapWalk)
basic.forever(on_forever)
