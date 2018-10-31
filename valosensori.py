import microbit as m

SUN_IMAGE = m.Image(
                "90909\n"
                "09990\n"
                "99999\n"
                "09990\n"
                "90909")
MOON_IMAGE = m.Image(
                "99900\n"
                "09990\n"
                "00990\n"
                "09990\n"
                "99900")

while True:
    light = m.pin0.read_analog()
    
    if light > 512:   #kokeile muuttaa tätä arvoa sopivaksi
        m.display.show(SUN_IMAGE)
    else:
        m.display.show(MOON_IMAGE)
