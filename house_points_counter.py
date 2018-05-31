from microbit import *

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

points = 0


def leds():
#   9 LEDs (of the appropriate house colour) wired to the following pins:
    led_1 = pin0
    led_2 = pin1
    led_3 = pin8
    led_4 = pin12
    led_5 = pin2
    led_6 = pin13
    led_7 = pin14
    led_8 = pin15
    led_9 = pin16
    led_list = [led_1, led_2, led_3, led_4, led_5,
                led_6, led_7, led_8, led_9]
    for led in range(0, points):
        led_list[led].write_digital(1)
    for led in range(points, len(led_list)):
        led_list[led].write_digital(0)


while True:
    display.show(str(points))
    leds()
    if button_b.was_pressed() and points < 9:
        points += 1
    if button_a.was_pressed() and points > 0:
        points -= 1
