from microbit import *
import music # Täällä tietoa music-kirjastosta ja sävelten koodaamisesta: http://microbit-micropython.readthedocs.io/en/latest/music.html#musical-notation

tune = [r:4, c4:4, d4:4, e4:4, f4:4, g4:8, g4:8, r:2, g4:4, f4:4, e4:4, d4:4, c4:8, c4:8]
# tune on laulu, jota soitetaan

while True:
  
  music.play(tune, pin1) # Oletus on, että kaiutin kytketään pin0:aan, joten poikkeus pitää kertoa koodissa
  
