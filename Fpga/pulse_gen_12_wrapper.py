# wrapper class to ensure compability between old and new pulse-generator
import math
from pulse_generator12ch import PulseGenerator as PulseGeneratorBase


class PulseGenerator(PulseGeneratorBase):

    def __init__(self, serial='', channel_map=None):
        if channel_map is None:
            PulseGeneratorBase.__init__(self, serial)
        else:
            PulseGeneratorBase.__init__(self, serial, channel_map)

    def Continuous(self, channels):
        self.setContinuous(channels)

    def Sequence(self, sequence, loop=None):
        if sequence.__len__() < 200:  # This makes sure that the length of the sequence is at least 200. This is needed for the Pulser.
            print "lengthening the sequence"
            sequence *= int(math.ceil(float(200) / sequence.__len__()))
        # self.setSequence(sequence, loop=True)
        self.setSequence(sequence, loops=-1)  # loop keyword changed

    def Night(self):
        self.setContinuous(0x0000)

    def Light(self):
        # self.setContinuous(0x000f)
        self.setContinuous(0xffff)  # all open when "light"

    def Open(self):
        self.setContinuous(0xffff)

# pulse_generator = PulseGenerator()