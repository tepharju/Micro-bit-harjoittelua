from microbit import *
import random

display.scroll("Ravista minua!")

while True:
    if accelerometer.was_gesture("shake"):
        throw = random.randint(1,6)
        if throw == 1:
            display.show("1")   # Miten saat näyttöön numeroiden tilalle kuvion?
        elif throw == 2:
            display.show("2")
        elif throw == 3:
            display.show("3")
        elif throw == 4:
            display.show("4")
        elif throw == 5:
            display.show("5")
        elif throw == 6:
            display.show("6")
