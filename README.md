# Corona-display

To keep a eye on the current Corona-Virus numbers I created this Programm wich displays the current stats to the Display.

<img src="./data/IMG.jpg">


## Datasource

For data I use [this Website](https://corona.help/).

To extract the data I use BeautifulSoup.

## Make it work

To print the numbers to the Terminal simply run the `fetch.py` file.

To show all Corona-cases to the Display run `display.py`.

To change the location, you ned to adjust the `url_c = "YourCountryLink"`. The Link you can find [here](https://corona.help/). To show the correct countrycode adjust the `CC = "Your countrycode"` as you wish.

```python
# Insert your URL here
url_c = "https://corona.help/country/switzerland"
# Your Countrycode
cc = "CH"
```

## Wiring

Detailed Instructions here: [Adafruit](https://learn.adafruit.com/character-lcd-with-raspberry-pi-or-beaglebone-black/overview)

<img src="https://cdn-learn.adafruit.com/assets/assets/000/018/260/original/raspberry_pi_RaspberryPiRGB_bb.png?1405984925">

- Connect Pi 5V power to the power rail of the breadboard. From the power rail connect one outer lead of the potentiometer, LCD pin 2 (VDD), and LCD pin 15 (LED+).
- Connect Pi ground to the ground rail of the breadboard. From the ground rail connect the other outer lead of the potentiometer, LCD pin 1 (VSS), and LCD pin 5 (R/W).
- Connect the middle lead of the potentiometer to LCD pin 3 (V0/contrast).
- Connect Pi pin 27 (or 21 on older revision Pi's) to LCD pin 4 (RS).
- Connect Pi pin 22 to LCD pin 6 (E/clock enable).
- Connect Pi pin 25 to LCD pin 11 (DB4).
- Connect Pi pin 24 to LCD pin 12 (DB5).
- Connect Pi pin 23 to LCD pin 13 (DB6).
- Connect Pi pin 18 to LCD pin 14 (DB7).
- Connect Pi pin 4 to LCD pin 16 (-R/red).
- Connect Pi pin 17 to LCD pin 17 (-G/green).
- Connect Pi pin 7 / CE1 to LCD pin 18 (-B/blue).

## Setup

Fetch current version of GitHub.
```sh
cd ~
git clone https://github.com/julianbruegger/corona-display.git

cd ~/corona-display
```

To setup the Display run:
```sh
sudo chmod +x install.sh
sudo ./install.sh
```
This Installs all the dependencies.

To start the Program just run:
```sh
python3 display.py
```

## Old Version

The first version of this with an other datasource is linked [Adafruit](https://github.com/julianbruegger/corona-display/tree/V1)