# Date: 2016
# Place: WSI, NV demo setup
# Author: Stefan Appel
# Thesis title (not final): Diamond magnetometer showcase setup (BSc)
# Sources used in this program:
# ueye.py (and subclasses) by Friedemann Reinhard
# LabJackPython.py (and subclasses) by LabJack
# ok.py (and subclasses) by OpalKelly
# pulse_generator12ch.py by the Stuttgart attocube group
# pulse_gen12_wrapper by the Reinhard group @Walther Schottky Institute 2016, TUM
# PIL by unknown
# PyQt4 by unknown


import io
import os
import re
import sys
import threading
import time

import numpy
from PIL import Image
from PyQt4 import QtGui

import Gui.gui as gui
import LabJack.labjacku3 as labjacku3
import ueye.ueye as ueye
from Fpga.pulse_gen_12_wrapper import *


# This class controls all measurements that can be done at the demo setup
class Main:
    def __init__(self):

        # Camera information
        self.cam = None  # The camera Ueye
        self.aoiCam = [0, 0, 1280, 1024]  # The hardware-set aoi [left, bot, width, height]
        self.pixelclockCam = 35  # The cam pixel clock frequency in MHz
        self.exposureCam = 150.0  # The cam exposure time in ms

        # LabJack information
        self.labJack = None  # The Labjack U3 HV
        self.portLabJackVcc = 0  # The port connected to vcc at the vco
        self.portLabJackTune = 1  # The port connected to vtune at the vco
        self.vccLabJack = 5.0  # The voltage required by the vco at vcc

        # FPGA information
        self.fpga = None  # The fpga XEM3005, flashed with "PulseGenerator12x8.bit"

        # Mode variables
        self.modCam = 0  # The cam mode.
        #               0: No cam connected,
        #               1: Cam connected,
        #               2: Stream running,
        #               >2: Different Measurement running
        self.lastModCam = 0  # Marker for returning to the last active cam mode after an experiment
        self.modLabJack = 0  # The Labjack mode.
        #                   0: Not connected,
        #                   1: Connected,
        #                   2: Manual control,
        #                   >2: Different Measurements running
        self.lastModLabJack = 0  # Same for the Labjack
        self.modFpga = 0  # Fpga mode.
        #               0: Not connected,
        #               1: Connected,
        #               2: Manual control,
        #               >2: Different measurements running
        self.lastModFpga = 0  # ...

        # Threads
        self.threadCam = None  # The thread used for reading from the cam while streaming and during an experiment
        self.threadLabJack = None  # Same for the LabJack

        # Image information
        self.imageRaw = numpy.zeros([1024, 1280])  # The last captured image from the cam
        self.imageBackground = numpy.zeros([1024, 1280])  # The currently used background image
        self.aoiSoft = [0, 0, 1280, 1024]  # AOI dimensions for cutting the image AFTER recording it
        self.settingsBackground = None  # Settings for background measurement, spec. the number of images to be taken

        # Microwave information
        self.vtune = 0  # Current voltage at vtune @vco
        self.power = False  # Current state of the vcc-port @vco
        self.seq = 'Off'  # Current sequence active @switch, connected to labjack or fpga
        self.calibration = [[0.0, 5.0],
                            [0.0, 5.0]]  # Array for storing the vco-calibration data. Initialize with a linear
        self.settingsCalibration = None  # List of settings for a calibration measurement
        self.customSeqs = {
            'Rabi': "[(['Laser'], 1000), ([], 1500), (['Mw'], t), ([], 100)]",
            'Ramsey': "[(['Laser'], 1000), ([], 1500), (['Mw'], 20), ([], t), (['Mw'], 20), ([], 1000)]",
            'Echo': "[(['Laser'], 1000), ([], 1500), (['Mw'], 20), ([], 100), (['Mw'], 40), ([], t), (['Mw'], 20), ([], 1000)]",
            'On': "On",
            'Off': "Off",
            'Demo': "[(['Laser'], 1000), ([], 1500), (['Mw'], 1000), ([], 1000)]"}  # Custom sequences that can be easily loaded from the gui

        # Odmr information
        self.odmr = [[], [], [],
                     []]  # Array for storing measured odmr data. Voltage, Frequency, Intensity, average intensity
        self.settingsOdmr = None  # List of settings for setting up the odmr measurement

        # Rabi information
        self.rabi = [[], [],
                     []]  # Array for measured data on timed sequences. Pulselength, Intensitiy, average intensity
        self.settingsRabi = None  # List of setting for setting up the rabi measurement

        # General savepath for results
        self.savepath = ''
        self.setSavepath(sys.path[0])

        # Start the gui
        appGui = QtGui.QApplication(sys.argv)
        self.gui = gui.MainGui(self, appGui)
        sys.exit(appGui.exec_())

        # Set some modus variables
        self.setModCam(0)
        self.setModLabJack(0)

    # ******************
    # * File managment *
    # ******************

    # Changes the working directory for saving stuff
    def setSavepath(self, savepath):
        try:
            os.chdir(savepath)
            self.savepath = savepath
            return True
        except:
            return False

    # Converts a data array into a text to write into a file
    def arrayToText(self, array):
        text = ""
        for i in range(len(array[1])):
            for j in range(len(array)):
                # Seperate Colums by ;
                text += str((array[j])[i]) + ";"
            # Delete last ;, seperate rows by \n
            text = text[0:-1] + "\n"
        # Delete last \n
        text = text[0:-1]
        return text

    # Converts a text from a file into an array
    def textToArray(self, text):
        # Split by rows
        lines = re.split('\n', text)
        # Split by semicolons for colums. Entries has the form [Line1, .., LineN] with LineI in the form of [entry1, ..., entryM]
        entries = [re.split(';', line) for line in lines]
        # Get the maximum lenght of a line. The header only has one colum
        maxlinelenght = max([len(line) for line in entries])
        # Delete all lines in the beginning that are shorter. This gets rid of the header
        while True:
            if len(entries[0]) < maxlinelenght:
                entries.pop(0)
            else:
                break
        # And from the remaining delete the first line as it is the legend
        entries.pop(0)
        # Create the array
        floatarray = []
        for line in entries:
            floatcolum = []
            for word in line:
                floatcolum.append(float(word))
            floatarray.append(floatcolum)
        array = numpy.transpose(floatarray)
        return array

    # **********
    # * Camera *
    # **********

    # Returns the current camera modus
    # 0: No cam connected, 1: Cam connected, 2: Stream running, 3: Measurement running
    def getModCam(self):
        return self.modCam

    def setModCam(self, mod):
        self.modCam = mod
        self.gui.sigModCam.emit()

    # Returns the currently connected cameras
    # as the Function for this is not implemented jet, just returns "Standard", no matter what
    def getCams(self):
        return ["Standard"]

    # Connects a camera if none has been connected so far
    def connectCam(self, camName):
        if self.modCam == 0:
            # Standard means "connect any"
            if camName == "Standard":
                try:
                    # Connect the first cam
                    self.cam = ueye.UEyeCamera()
                    self.setModCam(1)
                    return True
                except:
                    return False
            else:
                return False
        else:
            return False

    # Disconnects the camera if connected and not doing anything
    def disconnectCam(self):
        if self.modCam == 1:
            try:
                del self.cam
                self.setModCam(0)
                return True
            except:
                return False
        else:
            return False

    # Write pixel clock and exposure settings to the cam
    def writeCamSettings(self, px, expos):
        if self.modCam == 1 or self.modCam == 2:
            try:
                self.cam.set_pixel_clock(px)
                self.cam.set_exposure(expos)
                # Check if it worked
                if numpy.round(self.cam._get_exposure(), 2) == expos:
                    self.pixelclockCam = px
                    self.exposureCam = expos
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False

    # Write the hardware aoi to the cam.
    # As this changes the image size, reset the software aoi, the background image and the image itself
    def writeAoiCam(self, aoi):
        if self.modCam == 1:
            try:
                self.cam.set_aoi(aoi)
                # Check if it worked
                if self.cam._get_aoi() == (aoi):
                    self.aoiCam = list(aoi)
                    # Reset the software aoi and background image
                    self.setAoiSoft((0, 0, self.aoiCam[2], self.aoiCam[3]))
                    self.deleteBackground()
                    # Aquire a new image of the right size
                    self.readImage()
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False

    # Function for acquiring a new image, and all further calculated images
    # Should work as soon as a camera is connected
    # Only run in extra threads, as it is quite slow
    def readImage(self):
        if self.modCam >= 1:
            # get a image
            self.imageRaw = self.cam.acquire_image()
            # calculate the aoi and diff image
            self.imageAoi = self.imageRaw[(self.aoiSoft[1]):(self.aoiSoft[1] + self.aoiSoft[3]),
                            (self.aoiSoft[0]):(self.aoiSoft[0] + self.aoiSoft[2])]
            bgAoi = self.imageBackground[(self.aoiSoft[1]):(self.aoiSoft[1] + self.aoiSoft[3]),
                    (self.aoiSoft[0]):(self.aoiSoft[0] + self.aoiSoft[2])]
            self.imageDiff = self.imageAoi - bgAoi
            self.intensity = self.imageDiff.sum()

    # Returns the pixel clock and exposure time settings
    def getCamSettings(self):
        return (self.pixelclockCam, self.exposureCam)

    # Returns the harware aoi
    def getAoiCam(self):
        return self.aoiCam

    # Returns the last taken raw image
    def getImageRaw(self):
        return self.imageRaw

    # Starts a stream when a camera is connected and not doing anything else
    def startStream(self):
        if self.modCam == 1:
            try:
                # Start the stream on the cam thread
                self.threadCam = threading.Thread(target=self.stream)
                self.setModCam(2)
                self.threadCam.start()
                return True
            except:
                return False
        else:
            return False

    # Stops a running camera stream
    def stopStream(self):
        if self.modCam == 2:
            try:
                self.setModCam(1)
                del self.threadCam
                return True
            except:
                return False
        else:
            return False

    # The camera stream itself
    def stream(self):
        # As long as it is running, get images
        while self.modCam == 2:
            self.readImage()
            # No autostop here

    # ***********
    # * LabJack *
    # ***********

    # Return the mode the Labjack is currently in:
    # 0: Not connected, 1: Connected, 2: <unused>, 3: Calibration running, >3: Measurement running
    # If >2, the threadLabJack is currently used
    def getModLabJack(self):
        return self.modLabJack

    # Set the mode the labjack is in and update the gui
    def setModLabJack(self, mod):
        self.modLabJack = mod
        self.gui.sigModLabJack.emit()

    # Return the serials of all connected LabJacks as a string list
    def getLabJacks(self):
        if self.modLabJack == 0 or self.modLabJack == 1:
            try:
                stringlist = []
                for i in labjacku3.listSerials():
                    stringlist.append(str(i))
                return stringlist
            except:
                return [""]
        else:
            return [""]

    # Connect the LabJack with the given string serial if there is none connected
    def connectLabJack(self, serial):
        if self.modLabJack == 0:
            try:
                self.labJack = labjacku3.LJU3(int(serial))
                self.setModLabJack(1)
                return True
            except:
                return False
        else:
            return False

    # Disconnect a connected Labjack if it is not doing anything
    def disconnectLabJack(self):
        if self.modLabJack == 1:
            try:
                del self.labJack
                self.setModLabJack(0)
                return True
            except:
                return False
        else:
            return False

    # Write the LabJack settings (port map for outputs). The vcc and vtune-ports refer to the DAC-ports, the rest are FIO
    def writeLabJackSettings(self, port1, port2, port3, vcc):
        if self.modLabJack == 1:
            try:
                self.portLabJackVcc = port1
                self.portLabJackTune = port2
                self.portLabJackPulse = port3
                self.vccLabJack = vcc
                return True
            except:
                return False
        else:
            return False

    # Apply a voltage at vtune if vcc is on.
    # Private method, should only run within the labjack thread
    def writeVtune(self, volt):
        if self.modLabJack >= 1 and self.power:
            self.labJack.writeAN(self.portLabJackTune, volt)
            self.vtune = volt

    # Power the vcc port. Private method, should only run within the labjack thread
    def powerVcc(self, state):
        if self.modLabJack >= 1:
            if state:
                self.labJack.writeAN(self.portLabJackVcc, self.vccLabJack)
            else:
                self.labJack.writeAN(self.portLabJackVcc, 0)
                # If shutting down, also cut power on vtune
                self.writeVtune(0)
            self.power = state

    # Returns the applied vtune-voltage
    def getVtune(self):
        return self.vtune

    # Starts the manual labjack control
    def startManual(self):
        if self.modLabJack == 1:
            try:
                self.threadLabJack = threading.Thread(target=self.manual)
                self.setModLabJack(2)
                self.threadLabJack.start()
                return True
            except:
                return False
        else:
            return False

    # Stops it again
    def stopManual(self):
        if self.modLabJack == 2:
            try:
                # Stop the thread
                self.setModLabJack(1)
                del self.threadLabJack
                # power down
                self.powerVcc(False)
                # Stop pulsing and turn off
                self.writeSeq('Off')
                return True
            except:
                return False
        else:
            return False

    # The manual mode
    def manual(self):
        self.powerVcc(True)
        while self.modLabJack == 2:
            # Write the current voltage wanted into the LabJack
            self.writeVtune(self.vtune)
            self.writeSeq(self.seq)  # Using the fpga for this
            # Slow down
            time.sleep(.1)

    # For setting the voltage while in manual mode
    def voltManual(self, volt):
        if self.modLabJack == 2:
            try:
                self.vtune = volt
                return True
            except:
                return False
        else:
            return False

    # For setting the sequence while in manual mode. This will work for the fpga as well, if connected
    def seqManual(self, seq):
        if self.modLabJack == 2:
            try:
                # Just in case somebody misses the apostrophes, On and Off will work as well
                Off = 'Off'
                On = 'On'
                self.seq = eval(seq)
                return True
            except:
                return False
        else:
            return False

    # ********
    # * FPGA *
    # ********

    # Returns the mode the fpga is in. 0: Not connected, 1: Connected, >: Doing something
    def getModFpga(self):
        return self.modFpga

    # Set the mode and update the gui
    def setModFpga(self, mod):
        self.modFpga = mod
        self.gui.sigModFpga.emit()

    # Connect the Fpga with the given string serial if there is none connected
    def connectFpga(self, serial):
        if self.modFpga == 0 and self.modLabJack <= 1:
            try:
                channelMap = {'Mw': 0, 'Laser': 1, 'ch2': 2, 'ch3': 3,
                              'ch4': 4, 'ch5': 5, 'ch6': 6, 'ch7': 7,
                              'ch8': 8, 'ch9': 9, 'ch10': 10, 'ch11': 11}
                self.fpga = PulseGenerator(serial=serial,
                                           channel_map=channelMap)  # One has to apply a channel map in the beginning
                self.setModFpga(1)
                return True
            except:
                return False
        else:
            return False

    # Disconnect the connected fpga, if it (or the labjack) is not doing anything
    def disconnectFpga(self):
        if self.modFpga == 1 and self.modLabJack <= 1:
            try:
                del self.fpga
                self.setModFpga(0)
                return True
            except:
                return False
        else:
            return False

    # Write a new channel map to the fpga
    def writeFpgaSettings(self, chMw, chLaser):
        if self.modFpga == 1 and self.modLabJack <= 1:
            try:
                # Get the old channels for updating
                chMwOld = self.fpga.channel_map['Mw']
                chLaserOld = self.fpga.channel_map['Laser']
                # Update the channel mapping list
                self.fpga.channel_map.update(
                    {'Mw': chMw, 'Laser': chLaser, ('ch%i' % chMwOld): chMwOld, ('ch%i' % chLaserOld): chLaserOld})
                return True
            except:
                return False
        else:
            return False

    # Write a pulse sequence to the fpga
    def writeSeq(self, seq):
        # If a fpga is connected, use it no matter what
        if self.modFpga >= 1:
            # All off
            if seq == 'Off':
                self.fpga.Continuous([])
                self.seq = 'Off'
            # All On
            elif seq == 'On':
                self.fpga.Continuous(['Mw', 'Laser'])
                self.seq = 'On'
            # Real Sequence
            else:
                # Shut off continuous mode
                self.fpga.Continuous([])
                try:
                    # Try to enter the sequence
                    self.fpga.Sequence(1000 * seq, loop=-1)
                    self.seq = seq
                except:
                    # If not succesful, enter the last sequence
                    self.writeSeq(self.seq)
        # if not, use the labjack
        elif self.modLabJack >= 1:
            # All off
            if seq == 'Off':
                self.labJack.writePulse(self.portLabJackPulse, 0)
                self.seq = 'Off'
            # All On
            elif seq == 'On':
                self.labJack.writePulse(self.portLabJackPulse, -1)
                self.seq = 'On'
            # Real Sequence
            else:
                # Since the labjack has no real sequence control, just use the first entry of the sequence as a pulsetime
                pulseTime = self.labJack.writePulse(self.portLabJackPulse, seq[0][1])
                self.seq = [(['Mw'], pulseTime), ([], (2 ** 8 * 1e3 / 48.) - pulseTime)]

    # Returns the applied pulse-time
    def getSeq(self):
        return self.seq

    def getCustomSeq(self, name):
        return self.customSeqs[name]

    # *********
    # * Image *
    # *********

    # Returns the current aoi image
    def getImageAoi(self):
        return self.imageAoi

    # Returns the current Background image
    def getImageBackground(self):
        return self.imageBackground

    # Returns the current difference image to the background within the software-aoi
    def getImageDiff(self):
        return self.imageDiff

    # Starts a measurement for creating a new background image
    # when there is a cam connected and no other measurement running
    def startBackground(self, number):
        if self.modCam == 1 or self.modCam == 2:
            try:
                # Remember the current mode
                self.lastModCam = self.modCam
                # Stop a eventually running stream and change the mode
                self.stopStream()
                self.setModCam(3)
                # Give the number of images to the thread
                self.settingsBackground = number
                # Start the Measurement in the cam thread
                self.threadCam = threading.Thread(target=self.measureBackground)
                self.threadCam.start()
                return True
            except:
                return False
        else:
            return False

    # The background measurement
    def measureBackground(self):
        # Start a counter and a sum-up matrix
        i = 0
        background = numpy.zeros([self.aoiCam[3], self.aoiCam[2]])
        while self.modCam == 3 and i < self.settingsBackground:
            # Take a photo and add it to the background
            self.readImage()
            background += self.imageRaw
            i += 1
        # make the average
        self.imageBackground = background / long(i)
        # Autostop at the end
        self.stopBackground()

    # Stops a running background measurement
    def stopBackground(self):
        if self.modCam == 3:
            try:
                # Reset the mode
                self.setModCam(1)
                # Stop the thread
                del self.threadCam
                # Restart the stream if necesary
                if self.lastModCam == 2:
                    self.startStream()
                return True
            except:
                return False
        else:
            return False

    # Deletes the current background image an replaces it by a black image with the size of a raw image
    # if there is no measurement running
    def deleteBackground(self):
        if self.modCam == 1 or self.modCam == 2:
            try:
                self.imageBackground = numpy.zeros([self.aoiCam[3], self.aoiCam[2]])
                return True
            except:
                return False
        else:
            return False

    # Save the current background
    def saveBackground(self, filename):
        if self.modCam <= 2:
            try:
                # prepare into 8bit integer array
                prepared = (self.imageBackground * 256 / numpy.amax(self.imageBackground)).astype('uint8')
                # Create the image in 8bit mode L
                image = Image.fromarray(prepared, mode='L')
                # and save it
                image.save(filename)
                return True
            except:
                return False
        else:
            return False

    # Sets the software aoi to the desired size if there is no measuremnt running
    # If the desired size is bigger than the actual image, oversizes will be cut off
    def setAoiSoft(self, aoi):
        if self.modCam == 1 or self.modCam == 2:
            try:
                # Cutting away too large defined aoi
                if aoi[0] < 0:
                    aoi[0] = 0
                if aoi[1] < 0:
                    aoi[1] = 0
                if aoi[0] + aoi[2] > self.aoiCam[2]:
                    aoi[2] = self.aoiCam[2] - aoi[0]
                if aoi[1] + aoi[3] > self.aoiCam[3]:
                    aoi[3] = self.aoiCam[3] - aoi[1]
                self.aoiSoft = aoi
                return True
            except:
                return False
        else:
            return False

    # Returns the software aoi, no matter what
    def getAoiSoft(self):
        return self.aoiSoft

    # *****************
    # * VCO/Microwave *
    # *****************

    # Starts a calibration measurement
    # if a labjack is connected and not measuring yet
    def startCalibration(self, minvolt, maxvolt, stepvolt):
        if self.modLabJack == 1 or self.modLabJack == 2:
            try:
                # Remeber the mode and stop manual control
                self.lastModLabJack = self.modLabJack
                self.stopManual()
                # Set the mode to calibration
                self.setModLabJack(3)
                # Save the settings
                self.settingsCalibration = (minvolt, maxvolt, stepvolt)
                # Start the calibration in the LabJack thread
                self.threadLabJack = threading.Thread(target=self.measureCalibration)
                self.threadLabJack.start()
                return True
            except:
                return False
        else:
            return False

    # The calibration measurement
    def measureCalibration(self):
        # Aquire the measuremnt settings
        minvolt = self.settingsCalibration[0]
        maxvolt = self.settingsCalibration[1]
        # Prepare the output
        self.calibration = [[], []]
        # Start the vco
        self.powerVcc(True)
        # Use a "on"-sequence for the calibration
        self.seq = 'On'
        # Write the applied voltages into vtune
        self.vtune = minvolt
        # Set the mode again to update the gui
        self.setModLabJack(3)
        while self.modLabJack == 3 and self.vtune < maxvolt:
            # Apply the voltage
            self.writeVtune(self.vtune)
            # Eventually slow here artificially in order to make it run more stable
            time.sleep(0.1)
            # Writing the frequencies and stepping forward is done in .enterCalibration()
        # Autostop at the end
        self.stopCalibration()

    # Enters a new dataset while in calibration mode
    def enterCalibration(self, frequ):
        if self.modLabJack == 3:
            try:
                # extend the calibration data with the new measurement
                self.calibration[0].append(float(self.vtune))
                self.calibration[1].append(float(frequ))
                # Raise the voltage
                self.vtune += self.settingsCalibration[2]
                # update the gui by sending the sigModLabJack - signal via setModLabJack
                self.setModLabJack(self.modLabJack)
                return True
            except:
                return False
        else:
            return False

    # Stops the calibration
    def stopCalibration(self):
        if self.modLabJack == 3:
            try:
                # Cut the power
                self.powerVcc(False)
                # Trun off
                self.writeSeq('Off')
                # Stop the thread
                self.setModLabJack(1)
                del self.threadLabJack
                # Restart manual mode if necessary
                if self.lastModLabJack == 2:
                    self.startManual()
                return True
            except:
                return False
        else:
            return False

    # Return the currently used calibration
    def getCalibration(self):
        return self.calibration

    # Save the current calibration
    def saveCalibration(self, filename):
        if self.modLabJack == 1 or self.modLabJack == 2:
            try:
                # Prepare everything
                d = self.calibration
                # Open the file
                data = io.open(filename, 'w')
                # Add a Header
                data.write(unicode("VCO Calibration\n"))
                data.write(unicode(time.strftime("Date: %Y_%m_%d, %H:%M\n")))
                data.write(unicode("Voltage [V];Frequency [MHz]\n"))
                # Write the data
                data.write(unicode(self.arrayToText(d)))
                # Close the file
                data.close()
                return True
            except:
                return False
        else:
            return False

    # Save the current calibration
    def loadCalibration(self, filename):
        if self.modLabJack == 1 or self.modLabJack == 2:
            try:
                # Open the file
                data = io.open(filename, 'r')
                # Read everything and put it into an array
                self.calibration = self.textToArray(data.read(None))
                # Close the file
                data.close()
                # Update the calibration display
                self.setModLabJack(self.modLabJack)
                return True
            except:
                return False
        else:
            return False

    # Deletes the calibration and replaces it with a linear from 0 to 5 V, if nothing is running
    # If no calibration is avaible, one can therefore enter just voltages instead of frequencies
    # when measuring
    def deleteCalibration(self):
        if self.modLabJack == 1:
            try:
                self.calibration = [[0.0, 5.0], [0.0, 5.0]]
                return True
            except:
                return False
        else:
            return False

    # ********
    # * ODMR *
    # ********

    # Start a odmr-measurement if both cam and labjack are connected and not measuring
    def startOdmr(self, minfreq, maxfreq, stepfreq, count, seq):
        if (self.modCam == 1 or self.modCam == 2) and (self.modLabJack == 1 or self.modLabJack == 2):
            try:
                # Try to translate the sequence
                # Just in case somebody misses the apostrophes, On and Off will work as well
                Off = 'Off'
                On = 'On'
                eval(seq)
                # Save the current modes for later and stop stream and manual control
                self.lastModCam = self.modCam
                self.stopStream()
                self.lastModLabJack = self.modLabJack
                self.stopManual()
                # Set the modes to odmr
                self.setModCam(4)
                self.setModLabJack(4)
                # Save the measurement settings. Check calibration before saving them
                minimum = min(self.getCalibration()[1])
                maximum = max(self.getCalibration()[1])
                if minfreq < minimum:
                    minfreq = minimum
                if maxfreq > maximum:
                    maxfreq = maximum
                self.settingsOdmr = [minfreq, maxfreq, stepfreq, count, seq]
                # Start the odmr in the LabJack thread (it really doesn't matter which thread you use here)
                self.threadLabJack = threading.Thread(target=self.measureOdmr)
                self.threadLabJack.start()
                return True
            except:
                return False
        else:
            return False

    def measureOdmr(self):
        # get the settings
        [minfreq, maxfreq, stepfreq, count, seq] = self.settingsOdmr
        # Start the vco
        self.powerVcc(True)
        # Start the sequence and reset settingsOdmr on the achieved sequence
        # Just in case somebody misses the apostrophes, On and Off will work as well
        Off = 'Off'
        On = 'On'
        self.writeSeq(eval(seq))
        self.settingsOdmr[4] = self.seq
        # Wait half a second to apply everything
        time.sleep(.5)
        # prepare the output: Voltages, frequencies, intensity, average intensity
        self.odmr = [[], [], [], []]
        # prepare the calibration data
        calib = self.getCalibration()
        # prepare an array with the needed frequencies
        freqs = numpy.arange(minfreq, maxfreq, stepfreq)
        # interpolate from the calibration to get an array of voltages
        volts = numpy.interp(freqs, calib[1], calib[0])

        # start an index for going through the measurement
        i = 0
        while self.modCam == 4 and self.modLabJack == 4 and i < len(freqs):
            # apply the next voltage
            self.writeVtune(volts[i])
            # Wait a short moment
            time.sleep(.1)
            # start a sum for the average intensity
            sumIntensity = 0

            # Start the image count at fixed voltage
            j = 0
            while (self.modCam == 4 and self.modLabJack == 4) and j < count:
                # get an image
                self.readImage()
                # Append the data
                self.odmr[0].append(volts[i])
                self.odmr[1].append(freqs[i])
                self.odmr[2].append(self.intensity)
                # For now, just write the intensity here
                self.odmr[3].append(self.intensity)
                # Sum up the intensities
                sumIntensity += self.intensity
                j += 1

            # Calculate the average intensity and overwrite all previously written entries for this voltage
            avgIntensity = sumIntensity / float(j)
            for k in range(j):
                (self.odmr[3])[-k - 1] = avgIntensity
            # Go to the next voltage
            i += 1

        # Autostop at the end
        self.stopOdmr()

    # Stop a running odmr measurement
    def stopOdmr(self):
        if self.modCam == 4 and self.modLabJack == 4:
            try:
                # Turn off the vco
                self.powerVcc(False)
                # Turn off pulsing
                self.writeSeq('Off')
                # Reset the modes
                self.setModCam(1)
                self.setModLabJack(1)
                # clean up the thread
                del self.threadLabJack
                # Restart the stream if necessary
                if self.lastModCam == 2:
                    self.startStream()
                # Restart manual mode if necesarry
                if self.lastModLabJack == 2:
                    self.startManual()
                return True
            except:
                return False
        else:
            return False

    # Save the current odmr measurement
    def saveOdmr(self, filename):
        if self.modLabJack == 1 or self.modLabJack == 2:
            try:
                # Prepare everything
                d = self.odmr
                # Open the file
                data = io.open(filename, 'w')
                # Add a Header
                data.write(unicode("ODMR measurement\n"))
                data.write(unicode(time.strftime("Date: %Y_%m_%d, %H:%M\n")))
                data.write(unicode("ODMR settings:\n"))
                data.write(unicode("Minimum [MHz]: %f \n" % self.settingsOdmr[0]))
                data.write(unicode("Maximum [MHz]: %f \n" % self.settingsOdmr[1]))
                data.write(unicode("Step [MHz]: %f \n" % self.settingsOdmr[2]))
                data.write(unicode("Repeat [#]: %i \n" % self.settingsOdmr[3]))
                data.write(unicode("Sequence: %s \n" % str(self.settingsOdmr[4])))
                data.write(unicode("Cam settings:\n"))
                data.write(unicode("Hardware AOI: [%i, %i, %i, %i] \n" % (
                    self.aoiCam[0], self.aoiCam[1], self.aoiCam[2], self.aoiCam[3])))
                data.write(unicode("Software AOI: [%i, %i, %i, %i] \n" % (
                    self.aoiSoft[0], self.aoiSoft[1], self.aoiSoft[2], self.aoiSoft[3])))
                data.write(unicode("Pixelclock [MHz]: %f \n" % self.pixelclockCam))
                data.write(unicode("Exposure [ms]: %f \n" % self.exposureCam))
                data.write(unicode("Voltage [V];Frequency [MHz];Intensity [count]; Average Intensity [count]\n"))
                # Write the data
                data.write(unicode(self.arrayToText(d)))
                # Close the file
                data.close()
                return True
            except:
                return False
        else:
            return False

    def getOdmr(self):
        return self.odmr

    # ********
    # * Rabi *
    # ********

    # Start a rabi-measurement if both cam and labjack are connected and not measuring
    def startRabi(self, mintime, maxtime, steptime, seq, count, freq):
        if (self.modCam == 1 or self.modCam == 2) and (self.modLabJack == 1 or self.modLabJack == 2):
            try:
                # try translating the sequence
                # Test for the initial time t
                t = mintime
                # Just in case somebody misses the apostrophes, On and Off will work as well
                Off = 'Off'
                On = 'On'
                eval(seq)
                # Save the current modes for later and stop stream and manual control
                self.lastModCam = self.modCam
                self.stopStream()
                self.lastModLabJack = self.modLabJack
                self.stopManual()
                # Set the modes to rabi
                self.setModCam(5)
                self.setModLabJack(5)
                # Save the measurement settings. Check calibration before saving them
                minimum = min(self.getCalibration()[1])
                maximum = max(self.getCalibration()[1])
                if freq < minimum:
                    freq = minimum
                if freq > maximum:
                    freq = maximum
                self.settingsRabi = [mintime, maxtime, steptime, seq, count, freq]
                # Start the rabi in the LabJack thread (it really doesn't matter which thread you use here)
                self.threadLabJack = threading.Thread(target=self.measureRabi)
                self.threadLabJack.start()
                return True
            except:
                return False
        else:
            return False

    def measureRabi(self):
        # get the settings
        [mintime, maxtime, steptime, seq, count, freq] = self.settingsRabi
        # Start the vco
        self.powerVcc(True)
        # Tune the vco using the calibration
        calib = self.getCalibration()
        self.writeVtune(numpy.interp(freq, calib[1], calib[0]))
        # Wait half a second to apply everything
        time.sleep(.5)
        # prepare the output: time, intensity, average intensity
        self.rabi = [[], [], []]
        # Set the initial pulselength
        lastt = None
        t = mintime
        Off = 'Off'
        On = 'On'
        # Start measuring
        while self.modCam == 5 and self.modLabJack == 5 and t <= maxtime:
            self.writeSeq(eval(seq))
            # Calculate the achieved time t from the time resolution of the fpga
            dt = self.fpga.dt
            t = dt * int(round(t / dt))
            # Wait a short time to be on the safe side
            time.sleep(.1)
            # Check wether the applied time differs from the last applied time
            # If it does, start measuring. If not, increase further
            if t != lastt:
                # Log the time in lasttime
                lastt = t
                # start a sum for the average intensity
                sumIntensity = 0
                # Start the image count at fixed time
                j = 0
                while (self.modCam == 5 and self.modLabJack == 5) and j < count:
                    # get an image
                    self.readImage()
                    # Append the data
                    self.rabi[0].append(t)
                    self.rabi[1].append(self.intensity)
                    # For now, just write the intensity here
                    self.rabi[2].append(self.intensity)
                    # Sum up the intensities
                    sumIntensity += self.intensity
                    j += 1
                # Calculate the average intensity and overwrite all previously written entries for this time
                avgIntensity = sumIntensity / float(j)
                for k in range(j):
                    (self.rabi[2])[-k - 1] = avgIntensity
            # Increase the time
            t = t + steptime

        # Autostop at the end
        self.stopRabi()

    # Stop a running rabi measurement
    def stopRabi(self):
        if self.modCam == 5 and self.modLabJack == 5:
            try:
                # Turn off the vco
                self.powerVcc(False)
                # Turn off pulsing
                self.writeSeq('Off')
                # Reset the modes
                self.setModCam(1)
                self.setModLabJack(1)
                # clean up the thread
                del self.threadLabJack
                # Restart the stream if necessary
                if self.lastModCam == 2:
                    self.startStream()
                # Restart manual mode if necesarry
                if self.lastModLabJack == 2:
                    self.startManual()
                return True
            except:
                return False
        else:
            return False

    # Save the current rabi measurement
    def saveRabi(self, filename):
        if self.modLabJack == 1 or self.modLabJack == 2:
            try:
                # Prepare everything
                d = self.rabi
                # Open the file
                data = io.open(filename, 'w')
                # Add a Header
                data.write(unicode("Rabi measurement\n"))
                data.write(unicode(time.strftime("Date: %Y_%m_%d, %H:%M\n")))
                data.write(unicode("Rabi settings:\n"))
                data.write(unicode("Minimum [ns]: %f \n" % self.settingsRabi[0]))
                data.write(unicode("Maximum [ns]: %f \n" % self.settingsRabi[1]))
                data.write(unicode("Step [ns]: %f \n" % self.settingsRabi[2]))
                data.write(unicode("Sequence: %s \n" % self.settingsRabi[3]))
                data.write(unicode("Repeat [#]: %i \n" % self.settingsRabi[4]))
                data.write(unicode("Freq [MHz]: %f \n" % self.settingsRabi[5]))
                data.write(unicode("Cam settings:\n"))
                data.write(unicode("Hardware AOI: [%i, %i, %i, %i] \n" % (
                    self.aoiCam[0], self.aoiCam[1], self.aoiCam[2], self.aoiCam[3])))
                data.write(unicode("Software AOI: [%i, %i, %i, %i] \n" % (
                    self.aoiSoft[0], self.aoiSoft[1], self.aoiSoft[2], self.aoiSoft[3])))
                data.write(unicode("Pixelclock [MHz]: %f \n" % self.pixelclockCam))
                data.write(unicode("Exposure [ms]: %f \n" % self.exposureCam))
                data.write(unicode("Time [ns];Intensity [count]; Average Intensity [count]\n"))
                # Write the data
                data.write(unicode(self.arrayToText(d)))
                # Close the file
                data.close()
                return True
            except:
                return False
        else:
            return False

    def getRabi(self):
        return self.rabi


main = Main()
