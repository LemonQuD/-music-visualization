class DataProcessing:
    def __init__(self):
        self.pitches = 0
        self.brightness = 0

    def ReturnRGB(self, pitches):
        self.pitches = pitches
        if self.pitches == None:
            self.pitches = [0] * 12
        bass = int(sum(self.pitches[:4]) * 1000)
        midrange = int(sum(self.pitches[4:8:]) * 1000)
        treble = int(sum(self.pitches[-4:]) * 1000)

        if bass > midrange and bass > treble:
            redValue = 255
            blueValue = 0
        elif midrange > treble:
            redValue = 0
            blueValue = 255
        else:
            redValue = 255
            blueValue = 255

        return redValue, blueValue, 0, 1
