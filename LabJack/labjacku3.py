import LabJackPython as LJ


#Returns a list of serial numbers of all connected u3-devices
def listSerials():
    return list(LJ.listAll(LJ.LJ_dtU3, LJ.LJ_ctUSB).keys())


class LJU3:
    #Connects to a u3-device with matching serial number
    def __init__(self, serial=None):
        if serial is not None:
            u3dict = LJ.listAll(LJ.LJ_dtU3, LJ.LJ_ctUSB)
            connect = str((u3dict[serial])["localId"])
        else:
            connect = ""
        #One can use device for low-level commands, if necesarry
        self.device = LJ.openLabJack(LJ.LJ_dtU3, LJ.LJ_ctUSB, connect, 0)
        self.handle = self.device.handle

    def __del__(self):
        self.device.close()

    #Returns the voltage applied between two selected pins.
    #If only one pin is given, voltage is measured against gnd.
    #Ensures analog input mode
    def readAN(self, pinp, pinn=31):
        #Structure of ePut/eGet: (handle, command, channel, value, x1)
        LJ.ePut(self.handle, LJ.LJ_ioPUT_ANALOG_ENABLE_BIT, pinp, 1, 0)
        if pinn != 31:
            #Measuring against pinn (not recommended for pin 0-3)
            LJ.ePut(self.handle, LJ.LJ_ioPUT_ANALOG_ENABLE_BIT, pinn, 1, 0)
            return LJ.eGet(self.handle, LJ.LJ_ioGET_AIN_DIFF, pinp, 0, pinn)
        else:
            #Measuring against gnd (recommended)
            return LJ.eGet(self.handle, LJ.LJ_ioGET_AIN, pinp, 0, 0)

    #Sets the voltage output on a given pin (only two avaible)
    #Analog output mode is automatically ensured
    def writeAN(self, pin, voltage):
        LJ.ePut(self.handle, LJ.LJ_ioPUT_DAC, pin, voltage, 0)

    #Returns boolean values for the digital state of the pin.
    #Ensures digital input mode
    def readIO(self, pin):
        LJ.ePut(self.handle, LJ.LJ_ioPUT_ANALOG_ENABLE_BIT, pin, 0, 0)
        return bool(LJ.eGet(self.handle, LJ.LJ_ioGET_DIGITAL_BIT, pin, 0, 0))

    #Sets the digital output of selected pin.
    #Returns 0 if successfull
    #Ensures digital output mode
    def writeIO(self, pin, state):
        LJ.ePut(self.handle, LJ.LJ_ioPUT_ANALOG_ENABLE_BIT, pin, 0, 0)
        LJ.ePut(self.handle, LJ.LJ_ioPUT_DIGITAL_BIT, pin, int(state), 0)

    #Makes a digital output oscillate with the given frequency in MHz
    def writeFreq(self, pin, freqout):
        #Shut Off
        if freqout == 0:
            #Reset divisor for minimal analog voltage noise
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chTIMER_CLOCK_DIVISOR, 1, 0)
            #Reset to non-division standard clock
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chTIMER_CLOCK_BASE, LJ.LJ_tc48MHZ, 1)
            #Shut Off the timer
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chNUMBER_TIMERS_ENABLED, 0, 0)
        #Turn on
        else:
            #Prepare the timer. Set starting pin
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chTIMER_COUNTER_PIN_OFFSET, pin, 0)
            #enable 1 timer
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chNUMBER_TIMERS_ENABLED, 1, 0)
            #Disable counter 0 (used for division of frequencies internally)
            LJ.ePut(self.handle, LJ.LJ_ioPUT_COUNTER_ENABLE, 0, 0, 0)
            #Set the clock freq to enable two divisors. Don't change the frequ itself for noise reasons!
            #Output frequency is half the clock frequency
            freqin = 24
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chTIMER_CLOCK_BASE, LJ.LJ_tc48MHZ_DIV, 1)
            #Set the frequency as close as possible by applying a division factor
            div = int(freqin / float(freqout))
            #Cut on the maximum frequency
            if div == 0:
                div = 1
            #Set the first divisor, if the division factor gets to high
            #WARNING: High div1 leads to more noise in Analog outputs!
            div1 = 1
            div2 = div
            if div2 > 256:
                while div2 > 256:
                    div2 = div2 / 2
                    div1 = div1 * 2
            div1 = div1 % 256
            div2 = div2 % 256
            #print "freqin = %f, divtot = %i, div1 = %i, div2 = %i" % (freqin, div, div1, div2)
            #Apply the first Divisor
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chTIMER_CLOCK_DIVISOR, div1, 0)
            #Put the timer on frequency mode
            LJ.ePut(self.handle, LJ.LJ_ioPUT_TIMER_MODE, 0, LJ.LJ_tmFREQOUT, 0)
            #Apply the second divisor through "value"
            LJ.ePut(self.handle, LJ.LJ_ioPUT_TIMER_VALUE, 0, div2, 0)
            #return the output frequency achieved
            return freqin / float(div)

    #Makes a digital output make pulses with defined length at a fixed repetition rate of 93.750 kHz
    def writePulse(self, pin, pulseTime):
        #The minimum pulse time is the inverse of the clock frequency
        minPulseTime = 1e3 / 48.
        #Reset to non-division standard clock, just in case
        LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chTIMER_CLOCK_BASE, LJ.LJ_tc48MHZ, 1)
        #Reset divisor, just in case
        LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chTIMER_CLOCK_DIVISOR, 1, 0)
        #Stop if the pulselength is not usefull
        if pulseTime < 0 or pulseTime >= (2 ** 8) * minPulseTime:
            #Shut Off the timer
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chNUMBER_TIMERS_ENABLED, 0, 0)
            #Turn on the pin
            self.writeIO(pin, 1)
            return pulseTime
        #Turn the pin off for time 0
        elif pulseTime == 0:
            #Shut Off the timer
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chNUMBER_TIMERS_ENABLED, 0, 0)
            #Turn off the pin
            self.writeIO(pin, 0)
            return pulseTime
        #Turn on otherwise
        else:
            #Calculate the 8-bit integer that defines the LOW-time
            low = int(2 ** 8 - pulseTime / minPulseTime) % (2 ** 8)
            #Correct for too short pulses
            if low >= 2 ** 8:
                low = (2 ** 8) - 1
            #Prepare the timer. Set starting pin
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chTIMER_COUNTER_PIN_OFFSET, pin, 0)
            #enable 1 timer
            LJ.ePut(self.handle, LJ.LJ_ioPUT_CONFIG, LJ.LJ_chNUMBER_TIMERS_ENABLED, 1, 0)
            #Disable counter 0 (used for division of frequencies internally)
            LJ.ePut(self.handle, LJ.LJ_ioPUT_COUNTER_ENABLE, 0, 0, 0)
            #Put the timer on PWM mode
            LJ.ePut(self.handle, LJ.LJ_ioPUT_TIMER_MODE, 0, LJ.LJ_tmPWM8, 0)
            #Apply the low-value as a 16 bit
            LJ.ePut(self.handle, LJ.LJ_ioPUT_TIMER_VALUE, 0, low * 2 ** 8, 0)
            return (2 ** 8 - low) * minPulseTime