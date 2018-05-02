from microbit import *
import random

# luodaan lista tuvista
TUVAT   = ["Rohkelikko",
            "Luihunen",
            "Korpinkynsi",
            "Puuskupuh", "Surkki...",
           ]

gesture = accelerometer.current_gesture()
# create an endless loop waiting for button_a to be pressed


while True:
    display.scroll("RAVISTA!")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(100)
    #if button_a.is_pressed():
        display.scroll(random.choice(TUVAT))
    sleep(100)
    
    
