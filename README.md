# Micro:bit harjoituksia


## 1. harjoitus: Micro:bitin ohjaaminen ja tervehdysteksti

Harjoittele koodin kirjoittamista ja lataamista Micro:bittiin.

##### Ohjeet:

1. Kytke Micro:bit kiinni koneeseesi USB-johdolla. Micro:bit näkyy nyt ulkoisena asemana. 
2. Kirjoita koodia. Pääset kirjoittamaan koodia täällä: http://python.microbit.org/v/1
3. Lataa koodia sisältävä tiedosto (esim. helloworld.hex) koneellesi
4. Siirrä tiedosto Micro:bitille
5. Enjoy!

6. Kokeile miten saat tekstiä tulostumaan näytölle, kun microbitille tehdään jotain (painetaan nappia, heilutetaan, käännetään jne.). Huom! ääkköset eivät toimi! 

<img src="https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/microbit1.png" height="50%" width="50%">

Ohjeita tekstin ja kuvien lisäämiseen: http://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html


## 2. harjoitus: Tekstiä ja nappuloita

1. Kirjoita koodi, jolla voit tulostaa Micro:bitin näytölle tekstiä. Painamalla nappia A tulostuu ensimmäinen teksti ja napista B toinen teksti. 
2. Mitä rakenteita ohjelmassasi pitää olla?

## 3. harjoitus: Ledi-ja-nappi



##### Ohjeet:

1. Kirjoita koodi, jonka avulla ledi syttyy, kun nappia A painetaan ja Micro:bit näyttää tekstin: "Valo palaa!" 
<br>Esimerkkikoodia näet tiedostosta nappi.py.
2. Kokeile osaatko lisätä ohjelmaasi toiminnot lampun sytyttämiseksi ja sammuttamiseksi.

#### Virtapiiriin tarvittavat välineet:

Micro:bit, paristokotelo, johtimia, 100 Ohmin vastus, haluamasi värinen ledi. Paristokotelon sijaan voit kytkeä micro:bitin tietokoneeseen USB-johdolla.

<img src="https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/IMG_20180502_133946.jpg" height="200" width="350">

#### huom!:

Käytä kytkennässä 100-200 ohmin vastusta rajoittamaan virtaa:

#### Kytkentäkaavio:

<img src="https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/microbit2.png" height="40%" width="40%">


## 4. harjoitus: Musiikkia ja puhetta Micro:bitillä

#### Ohjeet:

Kytke Micro:bitin 1-pinniin kiinni kuulokkeet tai pietso-kaiutin. 
<img src="https://s3-eu-west-1.amazonaws.com/twsu-production/images/jack-1465559835719.jpg">
Kirjoita koodi, jonka avulla Micro:bit soittaa melodian, kun nappia painetaan. Nappi voi olla A, B tai itse johtimilla 0-pinniin rakennettu. 
Osaatko rakentaa jonkin tutun melodian (vaikkapa Jänis istui maassa)? Miten yhdistät napinpainalluskoodin melodiakoodiin?
Esimerkkikoodia musiikin tekemiseen: https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/musiikkia.py

Kokeile myös saatko microbitin puhumaan?

Esimerkkikoodi: https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/puhetta.py

Kokeile muuttaa say-funktion parametrejä. Saatko tuotettua selvää puhetta?


## 5. harjoitus: RGB-ledin ohjaaminen

#### Ohjeet:

RGB-led on led-lamppu, jonka valon väriä voi ohjata koodilla. Eri väriset valot sekoittuvat additiivisesti; mitä enemmän värejä, sitä enemmän valoa.
<br>1. Kytke RGB-led ja 100 tai 220 Ohmin vatukset kytkentälevyyn ja edelleen Micro:bittiin kuvan mukaisesti. 
<img src="http://www.101computing.net/wp/wp-content/uploads/bbc-microbit-RGB-LED-Circuit-Gradient.png">
<br>2. Koodaa ohjelma, joka saa ledin loistamaan ensin punaisena, sitten sinisenä, sitten vihreänä ja sitten magentan värisenä. Mitkä kaksi väriä muodostavan magentan? 
<br>3. Muuta koodia siten, että valo muuttuu vähitellen esim. vihreä-keltainen-punainen.
<br>4. Pohdi (ja toteuta halutessasi), miten kytkentään voisi liittää fotoresistorin eli valon määrää mittaavan sensorin. Millaisella koodilla saisi valon loistamaan muuten valkoisena, mutta pimeän tullen punaisena?

<img src="https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/RGBPinOut.png" height="20%" width="20%">


Esimerkkikoodi: https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/rgb-led.py

## 6. Harjoitus: Sorting hat / magic 8-ball 

Tee ohjelma joka arpoo tietyn tekstin näytölle toiminnolla. Ohjelmasi voi toimia esim. kääntämäälä Micro:bit ylöalaisin ohjelma arpoo valmiista listasta jonkin tekstin ja näyttää sen microbitin näytöllä.

Magic 8-ball: https://en.wikipedia.org/wiki/Magic_8-Ball

Gestures in MICRO:bit https://microbit-micropython.readthedocs.io/en/latest/tutorials/gestures.html


## 7. Harjoitus: Noppa

Tee MICRO:bitistä noppa. Ravistamalla (katso gestures) Micro:bittiä laite arpoo satunnaisen numeron ja näyttää sen ruudulla. Lisää ohjelma arpomaan myös perinteinen d6 nopan silmälukukuvio (ei numero.)

Esimerkkikoodi: https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/noppa.py

## 8. Harjoitus: Onko yö vai päivä? (Valosensori)

Valosensori näyttää onko yö vai päivä. Rakenna oheisen kuvan mukainen kytkentä ja asenna koodi Micro:bittiin. Testaa eri arvoja, että saat sensorin toimimaan haluamallasi tavalla. 


<img src="https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/microbit_breadboard_schema_light.png" height="40%" width="40%">
(Image by: Kitronic)

Esimerkkikoodi: https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/valosensori.py





## 9. Harjoitus: Kompassi ja vatupassi

Tee MICRO:bitistä kompassi ja vatupassi. Kompassiin tarvitset compass.calibrate() ja compass.heading() -metodeja. Vatupassiin tarvitset ainakin accelerometer.get_x() -metodia. Tallenna kiihtyvyysanturin arvo muuttujaan.

Esimerkkikoodi: https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/kompassi.py

Vatupassin esimerkki: https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/vatupassi.py


## 10. Harjoitus: Valotheremin
Valotheremin on soitin, jonka tuottama äänenkorkeus riippuu sen saaman valon määrästä. Thereminiä voi "soittaa" liikuttelemalla kättä tai vaikkapa kännykän taskulamppua thereminin valosensorin lähellä.

MICRO:bittiin kytketään valovastus eli fotoresistori ja pietsokaiutin kuvan mukaisesti. 
<img src="https://github.com/tepharju/Micro-bit-harjoittelua/blob/master/valotheremin1.png" height="50%" width="50%">

Koodiin tarvitaan music-kirjaston music.pitch()-metodia, joka saa äänentaajuuden arvon lukemalla sen analog_read()-metodilla valovastukselta. Analog_read() palauttaa arvon väliltä 0...1023, missä 0 vastaa 0 volttia ja 1023 vastaa 3,3 volttia. Valovastuksella luetun arvon voi esimerkiksi kertoa viidellä, jotta soitin tuottaisi korkeitakin ääniä.

Koodia ei tarvita kuin muutama rivi. Kokeile kirjoittaa se kokonaan itse!


