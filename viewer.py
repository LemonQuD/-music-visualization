import random
from emulator_backend import Adafruit_NeoPixel
# from neopixel_effects import NeoPixel_Effects

NUM_LEDS = 30
UPDATE_LEDS = 2


class Emulator:
    def __init__(self):
        self.pixels = Adafruit_NeoPixel(NUM_LEDS, 6, "NEO_GRB + NEO_KHZ800")
        self.pixels.begin()
        self.leds = []

        for i in range(NUM_LEDS):
            self.leds.append([0, 0, 0])

    def Animate(self, red, blue):

        # Move pixels to the left by UPDATE_LEDS times
        for i in range(NUM_LEDS - 1, 1, -1):
            self.leds[i] = self.leds[i - UPDATE_LEDS]

        # Set first UPDATE_LEDS
        for i in range(UPDATE_LEDS):
            self.leds[i] = [red, 0, blue]

        # Make the aniamtion
        for i in range(NUM_LEDS):
            self.pixels.setPixelColor(i, self.leds[i])
        self.pixels.show()
        self.pixels.clear()
        # self.pixels.delay(0)


# def run():
#     strip = Emulator()

#     while True:
#         value = random.randint(100, 250)
#         brightness = random.randint(0, 1)
#         strip.Animate(value, brightness)


# run()
