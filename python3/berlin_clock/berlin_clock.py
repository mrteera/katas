class BerlinClock:
    time = ""
    sec = ""
    min = ""
    berlin_sec = ""
    berlin_min = ""

    def setTime(self, time):
        self.sec = time[-2:]
        self.min = time[3:5]

    def toBerlin(self):
        if self.sec == "00":
            self.berlin_sec = "O "
        else:
            self.berlin_sec  = "Y "

        if self.min == "01":
            self.berlin_min = "Y"

    def display(self):
        self.toBerlin()
        return self.berlin_sec + "OOOO " + "OOOO " + "OOOOOOOOOOO " + self.berlin_min + "OOO"
