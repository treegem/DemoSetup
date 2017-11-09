import inspect
import sys
import threading
import time

from PyQt4 import uic  # , QtCore, QtGui
from PyQt4.QtCore import pyqtSignal, QSettings  # , QThread, QObject,
from PyQt4.QtGui import QWidget, QMessageBox, QLineEdit, QSpinBox, QDoubleSpinBox, QSlider

path = sys.path[0] + "\Gui"


# Function for loading the last settings of a gui
def loadSettings(gui, settings):
    pass
    """
    for name, obj in inspect.getmembers(gui):
        if settings.value(name) is not None:
            if isinstance(obj, QLineEdit):
                obj.setText(unicode(settings.value(name).toString()))
            if isinstance(obj, QSpinBox):
                obj.setValue(settings.value(name).toInt()[0])
            if isinstance(obj, QDoubleSpinBox):
                obj.setValue(settings.value(name).toFloat()[0])
            if isinstance(obj, QSlider):
                obj.setValue(settings.value(name).toInt()[0])
    #gui.restoreGeometry(settings.value("geometry").toByteArray())"""


# Function for saving the settings of a gui (not working yet)
def saveSettings(gui, settings):
    settings.clear()
    for name, obj in inspect.getmembers(gui):
        if isinstance(obj, QLineEdit):
            settings.setValue(name, obj.text())
        if isinstance(obj, QSpinBox):
            settings.setValue(name, obj.value())
        if isinstance(obj, QDoubleSpinBox):
            settings.setValue(name, obj.value())
        if isinstance(obj, QSlider):
            settings.setValue(name, obj.value())
    settings.setValue("geometry", gui.saveGeometry())


# Main Gui for selcting the different subguys
# and selecting the savepath
class MainGui(QWidget):
    # Modus update signals
    sigModLabJack = pyqtSignal()
    sigModCam = pyqtSignal()
    sigModFpga = pyqtSignal()

    def __init__(self, backend, qapp):
        # Loading the main gui
        super(QWidget, self).__init__()
        uic.loadUi(path + "\main.ui", self)

        # Restoring last settings
        loadSettings(self, QSettings("SAppel", "DemoMain"))

        # Connecting to the logical program behind
        self.backend = backend

        # Connecting to the system process
        self.qapp = qapp

        # Initialising subguys
        self.guiCam = CamGui(self.backend)
        self.guiLabJack = LabJackGui(self.backend)
        self.guiFpga = FpgaGui(self.backend)
        self.guiImage = ImageGui(self.backend)
        self.guiMw = MwGui(self.backend)
        self.guiOdmr = OdmrGui(self.backend)
        self.guiRabi = RabiGui(self.backend)

        # Looping through all signals
        self.sigModCam.connect(self.guiCam.sigModCam.emit)
        self.sigModCam.connect(self.guiImage.sigModCam.emit)
        self.sigModCam.connect(self.guiOdmr.sigModCam.emit)
        self.sigModCam.connect(self.guiRabi.sigModCam.emit)
        self.sigModLabJack.connect(self.guiLabJack.sigModLabJack.emit)
        self.sigModLabJack.connect(self.guiMw.sigModLabJack.emit)
        self.sigModLabJack.connect(self.guiOdmr.sigModLabJack.emit)
        self.sigModLabJack.connect(self.guiRabi.sigModLabJack.emit)
        self.sigModLabJack.connect(self.guiFpga.sigModLabJack.emit)
        self.sigModFpga.connect(self.guiFpga.sigModFpga.emit)

        # setting button actions
        self.btn_cam.clicked.connect(self.guiCam.show)
        self.btn_labjack.clicked.connect(self.guiLabJack.show)
        self.btn_fpga.clicked.connect(self.guiFpga.show)
        self.btn_image.clicked.connect(self.guiImage.show)
        self.btn_mw.clicked.connect(self.guiMw.show)
        self.btn_odmr.clicked.connect(self.guiOdmr.show)
        self.btn_rabi.clicked.connect(self.guiRabi.show)
        self.btn_path.clicked.connect(self.setSavepath)

        # Show the main gui
        self.show()

    # On closing: Ask before closing ALL windows
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit? \nAll data not saved yet will be lost!"
        reply = QMessageBox.question(self, 'Exit',
                                     quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # Save the settings
            saveSettings(self, QSettings("SAppel", "DemoMain"))
            saveSettings(self.guiCam, QSettings("SAppel", "DemoCam"))
            saveSettings(self.guiLabJack, QSettings("SAppel", "DemoLabJack"))
            saveSettings(self.guiFpga, QSettings("SAppel", "DemoFpga"))
            saveSettings(self.guiImage, QSettings("SAppel", "DemoImage"))
            saveSettings(self.guiMw, QSettings("SAppel", "DemoMw"))
            saveSettings(self.guiOdmr, QSettings("SAppel", "DemoOdmr"))
            saveSettings(self.guiRabi, QSettings("SAppel", "DemoRabi"))
            self.guiCam.close()
            self.guiFpga.close()
            self.guiLabJack.close()
            self.guiImage.close()
            self.guiMw.close()
            self.guiOdmr.close()
            self.guiRabi.close()
            # self.saveSettings()
            event.accept()
        else:
            event.ignore()

    # Change the current default savepath
    def setSavepath(self):
        if self.backend.setSavepath(str(self.line_path1.text())):
            self.line_path2.setText(self.line_path1.text())


'''
#For testing QThread (it doesn't work anyway)
class customThread(QThread):
    def __init__(self, target):
        super(QThread, self).__init__()
        self.target = target

    def run(self):
        self.target()
'''


# This Gui is for connecting and setting up the camera
# for intensity measurement.
# Every action is run via the backend object of the program
class CamGui(QWidget):
    sigPlot = pyqtSignal()
    sigModCam = pyqtSignal()

    def __init__(self, backend):
        # Loading the cam gui
        super(QWidget, self).__init__()
        uic.loadUi(path + "\cam.ui", self)

        # Restoring last settings
        loadSettings(self, QSettings("SAppel", "DemoCam"))

        # Connecting to the program
        self.backend = backend

        # Connecting signals
        self.sigModCam.connect(self.updateModCam)
        self.sigPlot.connect(self.mpl_raw.figure.canvas.draw)

        # Setting up the update thread
        self.thread = None
        self.plot = False

        # Preparing the image area
        self.mpl_raw.figure.clear()
        self.mpl_raw.figure.add_axes([0, 0, 1, 1])
        self.axesRaw = self.mpl_raw.figure.gca()
        self.axesRaw.axis('off')

        # setting button actions
        self.btn_search.clicked.connect(self.getCams)
        self.btn_con.clicked.connect(self.connectCam)
        self.btn_discon.clicked.connect(self.disconnectCam)
        self.btn_startstream.clicked.connect(self.startStream)
        self.btn_stopstream.clicked.connect(self.stopStream)

        # setting input box actions
        self.box_pixelclock.editingFinished.connect(self.setCamSettings)
        self.box_expos.editingFinished.connect(self.setCamSettings)
        self.box_left.editingFinished.connect(self.setAoiCam)
        self.box_width.editingFinished.connect(self.setAoiCam)
        self.box_bot.editingFinished.connect(self.setAoiCam)
        self.box_height.editingFinished.connect(self.setAoiCam)

        # Update
        self.sigModCam.emit()

        # Show the gui
        # self.show()

    # Updating gui settings after a cam mod change
    def updateModCam(self):
        modCam = self.backend.getModCam()
        if modCam == 0:
            # Enable/disable buttons and other elements
            self.btn_search.setEnabled(True)
            self.btn_con.setEnabled(True)
            self.btn_discon.setEnabled(False)
            self.btn_startstream.setEnabled(False)
            self.btn_stopstream.setEnabled(False)
            self.box_pixelclock.setEnabled(False)
            self.box_expos.setEnabled(False)
            self.box_left.setEnabled(False)
            self.box_width.setEnabled(False)
            self.box_bot.setEnabled(False)
            self.box_height.setEnabled(False)
            # Print a status
            self.label_stat1.setText("No camera connected")
            # Enable/disable the plotting of images
            self.setPlot(False)
        elif modCam == 1:
            self.btn_search.setEnabled(True)
            self.btn_con.setEnabled(False)
            self.btn_discon.setEnabled(True)
            self.btn_startstream.setEnabled(True)
            self.btn_stopstream.setEnabled(False)
            self.box_pixelclock.setEnabled(True)
            self.box_expos.setEnabled(True)
            self.box_left.setEnabled(True)
            self.box_width.setEnabled(True)
            self.box_bot.setEnabled(True)
            self.box_height.setEnabled(True)
            self.label_stat1.setText("Camera connected")
            self.setPlot(False)
        elif modCam == 2:
            self.btn_search.setEnabled(False)
            self.btn_con.setEnabled(False)
            self.btn_discon.setEnabled(False)
            self.btn_startstream.setEnabled(False)
            self.btn_stopstream.setEnabled(True)
            self.box_pixelclock.setEnabled(True)
            self.box_expos.setEnabled(True)
            self.box_left.setEnabled(False)
            self.box_width.setEnabled(False)
            self.box_bot.setEnabled(False)
            self.box_height.setEnabled(False)
            self.label_stat1.setText("Stream running")
            self.setPlot(True)
        elif modCam >= 3:
            self.btn_search.setEnabled(False)
            self.btn_con.setEnabled(False)
            self.btn_discon.setEnabled(False)
            self.btn_startstream.setEnabled(False)
            self.btn_stopstream.setEnabled(False)
            self.box_pixelclock.setEnabled(False)
            self.box_expos.setEnabled(False)
            self.box_left.setEnabled(False)
            self.box_width.setEnabled(False)
            self.box_bot.setEnabled(False)
            self.box_height.setEnabled(False)
            self.label_stat1.setText("Measurement running")
            self.setPlot(True)

    # Change wether to plot images or not
    def setPlot(self, state):
        if state != self.plot:
            if state:
                self.thread = threading.Thread(target=self.plotTrigger)
                self.plot = True
                self.thread.start()
            else:
                self.plot = False
                del self.thread

    # Deals with triggering image plotting.
    def plotTrigger(self):
        # When plotting is activated
        while self.plot:
            # and the gui is visible,
            if self.isVisible():
                # before triggering the plot signal, prepare all plot areas
                try:
                    self.axesRaw.cla()
                except IndexError as e:
                    print(e)
                self.axesRaw.imshow(self.backend.getImageRaw(), cmap='gray')
                # And send the plot signal
                self.sigPlot.emit()
                time.sleep(.5)

    def getCams(self):
        # Update the cam list
        self.list_cams.clear()
        cams = self.backend.getCams()
        self.list_cams.addItems(cams)

    # Connects the selcted cam and transmits the initial settings
    def connectCam(self):
        cam = self.list_cams.currentItem().text()
        self.label_stat2.setText("Connecting...")
        if self.backend.connectCam(cam):
            self.label_stat2.setText("Connected")
            # As soon as the camera is connected, write the current settings in the gui to the cam once
            self.setCamSettings()
            self.setAoiCam()
        else:
            self.label_stat2.setText("Failed to connect")

    # Disconnects from the connected cam
    def disconnectCam(self):
        self.label_stat2.setText("Disconnecting...")
        if self.backend.disconnectCam():
            self.label_stat2.setText("Disconnected")
        else:
            self.label_stat2.setText("Failed to disconnect")

    # Write cam settings
    def setCamSettings(self):
        pc = self.box_pixelclock.value()
        expos = self.box_expos.value()
        self.label_stat2.setText("Writing settings to cam...")
        if self.backend.writeCamSettings(pc, expos):
            self.label_stat2.setText("Settings set")
        else:
            self.label_stat2.setText("Settings could not be set")

    # Write hardware aoi
    def setAoiCam(self):
        left = self.box_left.value()
        bot = self.box_bot.value()
        width = self.box_width.value()
        height = self.box_height.value()
        self.label_stat2.setText("Writing aoi to cam...")
        if self.backend.writeAoiCam((left, bot, width, height)):
            self.label_stat2.setText("Aoi set")
        else:
            self.label_stat2.setText("Aoi could not be set")

    # Starts the image stream from the cam
    def startStream(self):
        self.label_stat2.setText("Starting stream...")
        if self.backend.startStream():
            self.label_stat2.setText("Stream started")
        else:
            self.label_stat2.setText("Failed to start stream")

    # Stops the stream
    def stopStream(self):
        self.label_stat2.setText("Stopping stream...")
        if self.backend.stopStream():
            self.label_stat2.setText("Stream stopped")
        else:
            self.label_stat2.setText("Failed to stop stream")


# This Gui is for connecting and setting up the controlable voltage source
# for controlling the vco/microwave
# Every action is run via the backend object of the program
class LabJackGui(QWidget):
    sigModLabJack = pyqtSignal()
    sigModFpga = pyqtSignal()
    sigPlot = pyqtSignal()

    def __init__(self, backend):
        # Loading the cam gui
        super(QWidget, self).__init__()
        uic.loadUi(path + "\labjack.ui", self)

        # Restoring last settings
        loadSettings(self, QSettings("SAppel", "DemoLabJack"))
        # Connecting to the program
        self.backend = backend

        # Initialising plot thread
        self.thread = None
        self.plot = False

        # Connecting signals
        self.sigModLabJack.connect(self.updateModLabJack)
        self.sigModFpga.connect(self.updateModLabJack)
        viewVolt = lambda: self.label_volt.setText(str(self.backend.getVtune()))
        viewTime = lambda: self.label_time.setText(str(self.backend.getSeq()))
        self.sigPlot.connect(viewVolt)
        self.sigPlot.connect(viewTime)

        # setting button actions
        self.btn_search.clicked.connect(self.getLabJacks)
        self.btn_con.clicked.connect(self.connectLabJack)
        self.btn_discon.clicked.connect(self.disconnectLabJack)
        self.btn_activate.clicked.connect(self.activateManual)
        self.btn_deactivate.clicked.connect(self.deactivateManual)

        # setting input box actions
        self.box_port1.editingFinished.connect(self.setLabJackSettings)
        self.box_port2.editingFinished.connect(self.setLabJackSettings)
        self.box_supplyvolt.editingFinished.connect(self.setLabJackSettings)
        self.box_tunevolt.editingFinished.connect(self.enterVolt)
        self.line_seq.editingFinished.connect(self.enterSeq)
        self.box_seq.addItems(self.backend.customSeqs.keys())
        self.box_seq.currentIndexChanged.connect(self.customSeq)

        # Update
        self.sigModLabJack.emit()

        # Show the gui
        # self.show()

    # Updating gui settings after a labjack mod change
    def updateModLabJack(self):
        modLabJack = self.backend.getModLabJack()
        if modLabJack == 0:
            # Enable/disable buttons and other elements
            self.btn_search.setEnabled(True)
            self.btn_con.setEnabled(True)
            self.btn_discon.setEnabled(False)
            self.btn_activate.setEnabled(False)
            self.btn_deactivate.setEnabled(False)
            self.box_port1.setEnabled(False)
            self.box_port2.setEnabled(False)
            self.box_port3.setEnabled(False)
            self.box_supplyvolt.setEnabled(False)
            self.box_tunevolt.setEnabled(False)
            self.line_seq.setEnabled(False)
            # Print a status
            self.label_stat1.setText("No LabJack connected")
            # Start/stop plotting data (here only one little display)
            self.setPlot(False)
        elif modLabJack == 1:
            self.btn_search.setEnabled(True)
            self.btn_con.setEnabled(False)
            self.btn_discon.setEnabled(True)
            self.btn_activate.setEnabled(True)
            self.btn_deactivate.setEnabled(False)
            self.box_port1.setEnabled(True)
            self.box_port2.setEnabled(True)
            self.box_port3.setEnabled(True)
            self.box_supplyvolt.setEnabled(True)
            self.box_tunevolt.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.label_stat1.setText("LabJack connected")
            self.setPlot(False)
        elif modLabJack == 2:
            self.btn_search.setEnabled(False)
            self.btn_con.setEnabled(False)
            self.btn_discon.setEnabled(False)
            self.btn_activate.setEnabled(False)
            self.btn_deactivate.setEnabled(True)
            self.box_port1.setEnabled(False)
            self.box_port2.setEnabled(False)
            self.box_port3.setEnabled(False)
            self.box_supplyvolt.setEnabled(False)
            self.box_tunevolt.setEnabled(True)
            self.line_seq.setEnabled(True)
            self.label_stat1.setText("Manual control")
            self.setPlot(True)
        elif modLabJack >= 3:
            self.btn_search.setEnabled(False)
            self.btn_con.setEnabled(False)
            self.btn_discon.setEnabled(False)
            self.btn_activate.setEnabled(False)
            self.btn_deactivate.setEnabled(False)
            self.box_port1.setEnabled(False)
            self.box_port2.setEnabled(False)
            self.box_port3.setEnabled(False)
            self.box_supplyvolt.setEnabled(False)
            self.box_tunevolt.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.label_stat1.setText("Measurement running")
            self.setPlot(True)

    # Change wether to plot data or not
    def setPlot(self, state):
        if state != self.plot:
            if state:
                self.thread = threading.Thread(target=self.plotTrigger)
                self.plot = True
                self.thread.start()
            else:
                self.plot = False
                del self.thread

    # Deals with triggering image plotting.
    def plotTrigger(self):
        # When plotting is activated
        while self.plot:
            # and the gui is visible,
            if self.isVisible():
                # Send the plot signal
                self.sigPlot.emit()
                time.sleep(.2)

    # Updates the labjack list
    def getLabJacks(self):
        self.list_labjacks.clear()
        labjacks = self.backend.getLabJacks()
        self.list_labjacks.addItems(labjacks)

    # Connects the selcted LabJack and transmits the initial settings
    def connectLabJack(self):
        serial = int(self.list_labjacks.currentItem().text())
        self.label_stat2.setText("Connecting...")
        if self.backend.connectLabJack(serial):
            self.label_stat2.setText("Connected")
            # As soon as the labjack is connected
            # write the current settings in the gui to the labjack once
            # and power down
            self.setLabJackSettings()
            self.backend.powerVcc(False)
            self.backend.writeSeq('Off')
        else:
            self.label_stat2.setText("Failed to connect")

    # Disconnects from the connected LabJack
    def disconnectLabJack(self):
        self.label_stat2.setText("Disconnecting...")
        if self.backend.disconnectLabJack():
            self.label_stat2.setText("Disconnected")
        else:
            self.label_stat2.setText("Failed to disconnect")

    # Write LabJack settings
    def setLabJackSettings(self):
        portVcc = self.box_port1.value()
        portVtune = self.box_port2.value()
        portPulse = self.box_port3.value()
        vcc = self.box_supplyvolt.value()
        self.label_stat2.setText("Writing settings to Labjack...")
        if self.backend.writeLabJackSettings(portVcc, portVtune, portPulse, vcc):
            self.label_stat2.setText("Settings set")
        else:
            self.label_stat2.setText("Settings could not be set")

    # Activate manual conrol
    def activateManual(self):
        self.label_stat2.setText("Activating manual mode...")
        if self.backend.startManual():
            self.label_stat2.setText("Manual mode activated")
        else:
            self.label_stat2.setText("Could not activate manual mode")

    # Deactivate manual control
    def deactivateManual(self):
        self.label_stat2.setText("Deactivating manual mode...")
        if self.backend.stopManual():
            self.label_stat2.setText("Manual mode deactivated")
        else:
            self.label_stat2.setText("Could not deactivate manual mode")

    # Enter a voltage setting via manual control
    def enterVolt(self):
        volt = self.box_tunevolt.value()
        self.label_stat2.setText("Entering voltage...")
        if self.backend.voltManual(volt):
            self.label_stat2.setText("Voltage applied")
        else:
            self.label_stat2.setText("Could not apply voltage")

    # Enter a Sequence via manual mode
    def enterSeq(self):
        seq = str(self.line_seq.text())
        self.label_stat2.setText("Entering sequence...")
        if self.backend.seqManual(seq):
            self.label_stat2.setText("Sequence set")
        else:
            self.label_stat2.setText("Could not set sequence")

    # Enters a custom sequence stored in the backend
    def customSeq(self):
        if self.box_seq.currentIndex() > 0:
            self.label_stat2.setText("Loading custom sequence...")
            # try:
            seq = self.backend.getCustomSeq(str(self.box_seq.currentText()))
            self.line_seq.setText(str(seq))
            self.label_stat2.setText("Custom sequence loaded")
            # except:
            # self.label_stat2.setText("Failed to load custom Sequence")
            self.box_seq.setCurrentIndex(0)


# This Gui is for connecting and setting up the FPGA
# for controlling pulsing
# Every action is run via the backend object of the program
class FpgaGui(QWidget):
    sigModLabJack = pyqtSignal()
    sigModFpga = pyqtSignal()
    sigPlot = pyqtSignal()

    def __init__(self, backend):
        # Loading the cam gui
        super(QWidget, self).__init__()
        uic.loadUi(path + "/fpga.ui", self)

        # Restoring last settings
        loadSettings(self, QSettings("SAppel", "DemoFpga"))

        # Connecting to the program
        self.backend = backend

        # Initialising plot thread
        self.thread = None
        self.plot = False

        # Connecting signals
        self.sigModFpga.connect(self.updateMod)
        self.sigModLabJack.connect(self.updateMod)

        # setting button actions
        self.btn_con.clicked.connect(self.connect)
        self.btn_discon.clicked.connect(self.disconnect)

        # setting input box actions
        self.box_port1.editingFinished.connect(self.setSettings)
        self.box_port2.editingFinished.connect(self.setSettings)

        # Update
        self.sigModFpga.emit()

        # Show the gui
        # self.show()

    # Updating gui settings after a labjack mod change
    def updateMod(self):
        modFpga = self.backend.getModFpga()
        modLabJack = self.backend.getModLabJack()
        # Connecting an fpga alters the behaviour of any measurement using the Labjack
        if modFpga == 0 and modLabJack <= 1:
            # Enable/disable buttons and other elements
            self.btn_con.setEnabled(True)
            self.btn_discon.setEnabled(False)
            self.box_port1.setEnabled(False)
            self.box_port2.setEnabled(False)
            # Print a status
            self.label_stat1.setText("No FPGA connected")
            # Start/stop plotting data (here only one little display)
            self.setPlot(False)
        elif modFpga == 1 and modLabJack <= 1:
            self.btn_con.setEnabled(False)
            self.btn_discon.setEnabled(True)
            self.box_port1.setEnabled(True)
            self.box_port2.setEnabled(True)
            self.label_stat1.setText("FPGA connected")
            self.setPlot(False)
        elif modLabJack == 2:
            self.btn_con.setEnabled(False)
            self.btn_discon.setEnabled(False)
            self.box_port1.setEnabled(False)
            self.box_port2.setEnabled(False)
            self.label_stat1.setText('Manual control - Use "Demo Setup - Labjack-Settings" to control')
            self.setPlot(True)
        elif modLabJack >= 3:
            self.btn_con.setEnabled(False)
            self.btn_discon.setEnabled(False)
            self.box_port1.setEnabled(False)
            self.box_port2.setEnabled(False)
            self.label_stat1.setText("Measurement running")
            self.setPlot(True)

    # Change wether to plot data or not
    def setPlot(self, state):
        if state != self.plot:
            if state:
                self.thread = threading.Thread(target=self.plotTrigger)
                self.plot = True
                self.thread.start()
            else:
                self.plot = False
                del self.thread

    # Deals with triggering image plotting.
    def plotTrigger(self):
        # When plotting is activated
        while self.plot:
            # and the gui is visible,
            if self.isVisible():
                # Send the plot signal
                self.sigPlot.emit()
                time.sleep(.2)

    # Connects the selcted Fpga and transmits the initial settings
    def connect(self):
        serial = str(self.line_serial.text())
        self.label_stat2.setText("Connecting...")
        if self.backend.connectFpga(serial):
            self.label_stat2.setText("Connected")
            # As soon as the labjack is connected
            # write the current settings in the gui to the labjack once
            # and power down
            self.setSettings()
            self.backend.writeSeq('Off')
        else:
            self.label_stat2.setText("Failed to connect")

    # Disconnects from the connected LabJack
    def disconnect(self):
        self.label_stat2.setText("Disconnecting...")
        if self.backend.disconnectFpga():
            self.label_stat2.setText("Disconnected")
        else:
            self.label_stat2.setText("Failed to disconnect")

    # Write Fpga settings
    def setSettings(self):
        portMw = self.box_port1.value()
        portLaser = self.box_port2.value()
        self.label_stat2.setText("Writing settings to Labjack...")
        if self.backend.writeFpgaSettings(portMw, portLaser):
            self.label_stat2.setText("Settings set")
        else:
            self.label_stat2.setText("Settings could not be set")


# This gui is for adjusting the aoi for the measurement
# and taking background measuremnts
class ImageGui(QWidget):
    sigModCam = pyqtSignal()
    sigPlot = pyqtSignal()

    def __init__(self, backend):
        # Loading the cam gui
        super(QWidget, self).__init__()
        uic.loadUi(path + "\image.ui", self)

        # Restoring last settings
        loadSettings(self, QSettings("SAppel", "DemoImage"))

        # Connecting to the program
        self.backend = backend

        # Connecting signals
        self.sigModCam.connect(self.updateModCam)
        self.sigPlot.connect(self.mpl_raw.figure.canvas.draw)
        self.sigPlot.connect(self.mpl_diff.figure.canvas.draw)

        # Setting up the update thread
        self.thread = None
        self.plot = False

        # Preparing the image areas
        self.mpl_raw.figure.clear()
        self.mpl_raw.figure.add_axes([0, 0, 1, 1])
        self.axesRaw = self.mpl_raw.figure.gca()
        self.axesRaw.axis('off')
        self.axesRaw.hold(False)
        self.mpl_backg.figure.clear()
        self.mpl_backg.figure.add_axes([0, 0, 1, 1])
        self.axesBackg = self.mpl_backg.figure.gca()
        self.axesBackg.axis('off')
        self.axesBackg.hold(False)
        self.mpl_diff.figure.clear()
        self.mpl_diff.figure.add_axes([0, 0, 1, 1])
        self.axesDiff = self.mpl_diff.figure.gca()
        self.axesDiff.axis('off')
        self.axesDiff.hold(False)

        # setting button actions
        self.btn_measure.clicked.connect(self.measure)
        self.btn_abort.clicked.connect(self.abort)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_save.clicked.connect(self.save)

        # setting slider actions
        self.sli_bot.sliderReleased.connect(self.setAoiSoft)
        self.sli_left.sliderReleased.connect(self.setAoiSoft)
        self.sli_right.sliderReleased.connect(self.setAoiSoft)
        self.sli_top.sliderReleased.connect(self.setAoiSoft)

        # Update
        self.sigModCam.emit()

        # Show the gui
        # self.show()

    # Updating gui settings after a cam mod change
    def updateModCam(self):
        modCam = self.backend.getModCam()
        if modCam == 0:
            # Enable/disable buttons and other elements
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_delete.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.sli_bot.setEnabled(False)
            self.sli_left.setEnabled(False)
            self.sli_right.setEnabled(False)
            self.sli_top.setEnabled(False)
            # Print a status
            self.label_stat1.setText("No camera connected")
            # Enable/disable the plotting of images
            self.setPlot(False)
        elif modCam == 1:
            self.btn_measure.setEnabled(True)
            self.btn_abort.setEnabled(False)
            self.btn_delete.setEnabled(True)
            self.btn_save.setEnabled(True)
            self.sli_bot.setEnabled(True)
            self.sli_left.setEnabled(True)
            self.sli_right.setEnabled(True)
            self.sli_top.setEnabled(True)
            self.label_stat1.setText("Camera connected")
            # Plot the current background once
            self.axesBackg.imshow(self.backend.getImageBackground(), cmap='gray')
            self.mpl_backg.figure.canvas.draw()
            self.setPlot(False)
        elif modCam == 2:
            self.btn_measure.setEnabled(True)
            self.btn_abort.setEnabled(False)
            self.btn_delete.setEnabled(True)
            self.btn_save.setEnabled(True)
            self.sli_bot.setEnabled(True)
            self.sli_left.setEnabled(True)
            self.sli_right.setEnabled(True)
            self.sli_top.setEnabled(True)
            self.label_stat1.setText("Camera connected, Stream running")
            # Plot the current background once
            self.axesBackg.imshow(self.backend.getImageBackground(), cmap='gray')
            self.mpl_backg.figure.canvas.draw()
            self.setPlot(True)
        elif modCam == 3:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(True)
            self.btn_delete.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.sli_bot.setEnabled(False)
            self.sli_left.setEnabled(False)
            self.sli_right.setEnabled(False)
            self.sli_top.setEnabled(False)
            self.label_stat1.setText("Background measurement running")
            self.setPlot(False)
        elif modCam >= 4:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_delete.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.sli_bot.setEnabled(False)
            self.sli_left.setEnabled(False)
            self.sli_right.setEnabled(False)
            self.sli_top.setEnabled(False)
            self.label_stat1.setText("Measurement running")
            self.setPlot(True)

    # Change wether to plot images or not
    def setPlot(self, state):
        if state != self.plot:
            if state:
                self.thread = threading.Thread(target=self.plotTrigger)
                self.plot = True
                self.thread.start()
            else:
                self.plot = False
                del self.thread

    # Deals with triggering image plotting.
    def plotTrigger(self):
        # When plotting is activated
        while self.plot:
            # and the gui is visible,
            if self.isVisible():
                # before triggering the plot signal, prepare all plot areas
                aoi = self.backend.getAoiSoft()
                self.axesRaw.cla()
                self.axesRaw.imshow(self.backend.getImageRaw(), cmap='gray')
                self.axesRaw.axvline(aoi[0], color='g')
                self.axesRaw.axvline(aoi[0] + aoi[2] - 1, color='g')
                self.axesRaw.axhline(aoi[1], color='g')
                self.axesRaw.axhline(aoi[1] + aoi[3] - 1, color='g')
                self.mpl_diff.figure.clear()
                self.mpl_diff.figure.add_axes([0, 0, .9, 1])
                self.axesDiff = self.mpl_diff.figure.gca()
                self.axesDiff.axis('off')
                imageDiff = self.axesDiff.imshow(self.backend.getImageDiff())
                self.mpl_diff.figure.colorbar(imageDiff, ax=self.axesDiff, shrink=0.8)
                # And send the plot signal
                self.sigPlot.emit()
                time.sleep(1)

    def measure(self):
        self.label_stat2.setText("Starting background measurement...")
        if self.backend.startBackground(int(self.box_number.value())):
            self.label_stat2.setText("Measuring Background")
        else:
            self.label_stat2.setText("Background measurement failed")

    def abort(self):
        self.label_stat2.setText("Aborting background measurement...")
        if self.backend.stopBackground():
            self.label_stat2.setText("Measurement aborted")
        else:
            self.label_stat2.setText("Failed to abort Measurement")

    def delete(self):
        self.label_stat2.setText("Deleting current background...")
        if self.backend.deleteBackground():
            self.label_stat2.setText("Background successfully deleted")
        else:
            self.label_stat2.setText("Failed to delete Background")

    def save(self):
        self.label_stat2.setText("Saving current background...")
        if self.backend.saveBackground(str(self.line_file.text())):
            self.label_stat2.setText("Background successfully saved")
        else:
            self.label_stat2.setText("Failed to save Background")

    def setAoiSoft(self):
        # read the aoi-sliders and ensure correct reading
        left = self.sli_left.value()
        bot = self.sli_bot.value()
        right = self.sli_right.value()
        top = self.sli_top.value()
        # Correct mixover and zero-select
        if left > right:
            left, right = right, left
        if left == right:
            left -= 1
            right += 1
        if bot > top:
            bot, top = top, bot
        if top == bot:
            top += 1
            bot -= 1
        # set the aoi-values
        self.label_stat2.setText("Setting AOI...")
        if self.backend.setAoiSoft([left, bot, right - left, top - bot]):
            self.label_stat2.setText("AOI set")
        else:
            self.label_stat2.setText("Failed to set AOI")
        # Putting the sliders at the corrected position
        aoi = self.backend.getAoiSoft()
        self.sli_left.setValue(aoi[0])
        self.sli_bot.setValue(aoi[1])
        self.sli_right.setValue(aoi[0] + aoi[2])
        self.sli_top.setValue(aoi[1] + aoi[3])


# This Gui is for calibrating the vco.
# Every action is run via the backend object of the program
class MwGui(QWidget):
    sigModLabJack = pyqtSignal()

    def __init__(self, backend):
        # Loading the cam gui
        super(QWidget, self).__init__()
        uic.loadUi(path + "\mw.ui", self)

        # Restoring last settings
        loadSettings(self, QSettings("SAppel", "DemoMw"))

        # Connecting to the program
        self.backend = backend

        # Connecting signals
        self.sigModLabJack.connect(self.updateModLabJack)

        # Preparing result area
        self.mpl_result.figure.clear()
        self.mpl_result.figure.add_axes([.15, .05, .85, .95])
        self.axesResults = self.mpl_result.figure.gca()

        # setting button actions
        self.btn_measure.clicked.connect(self.measure)
        self.btn_abort.clicked.connect(self.abort)
        self.btn_save.clicked.connect(self.save)
        self.btn_load.clicked.connect(self.load)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_enter.clicked.connect(self.enter)

        # Update
        self.sigModLabJack.emit()

        # Show the gui
        # self.show()

    # Updating gui settings after a labjack mod change
    def updateModLabJack(self):
        modLabJack = self.backend.getModLabJack()
        if modLabJack == 0:
            # Enable/disable buttons and other elements
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.btn_load.setEnabled(False)
            self.btn_delete.setEnabled(False)
            self.btn_enter.setEnabled(False)
            self.box_minvoltage.setEnabled(True)
            self.box_maxvoltage.setEnabled(True)
            self.box_stepvoltage.setEnabled(True)
            self.box_frequ.setEnabled(False)
            # Print a status
            self.label_stat1.setText("No LabJack connected")
        elif modLabJack == 1:
            self.btn_measure.setEnabled(True)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.btn_load.setEnabled(True)
            self.btn_delete.setEnabled(True)
            self.btn_enter.setEnabled(False)
            self.box_minvoltage.setEnabled(True)
            self.box_maxvoltage.setEnabled(True)
            self.box_stepvoltage.setEnabled(True)
            self.box_frequ.setEnabled(False)
            self.label_stat1.setText("LabJack connected")
            # Plot the calibration once
            calibration = self.backend.getCalibration()
            self.axesResults.cla()
            self.axesResults.plot(calibration[0], calibration[1], 'b-')
            self.mpl_result.figure.canvas.draw()
        elif modLabJack == 2:
            self.btn_measure.setEnabled(True)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.btn_load.setEnabled(True)
            self.btn_delete.setEnabled(True)
            self.btn_enter.setEnabled(False)
            self.box_minvoltage.setEnabled(True)
            self.box_maxvoltage.setEnabled(True)
            self.box_stepvoltage.setEnabled(True)
            self.box_frequ.setEnabled(False)
            self.label_stat1.setText("LabJack connected")
            # Plot the calibration once
            calibration = self.backend.getCalibration()
            self.axesResults.cla()
            self.axesResults.plot(calibration[0], calibration[1], 'b-')
            self.mpl_result.figure.canvas.draw()
        elif modLabJack == 3:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(True)
            self.btn_save.setEnabled(False)
            self.btn_load.setEnabled(False)
            self.btn_delete.setEnabled(False)
            self.btn_enter.setEnabled(True)
            self.box_minvoltage.setEnabled(False)
            self.box_maxvoltage.setEnabled(False)
            self.box_stepvoltage.setEnabled(False)
            self.box_frequ.setEnabled(True)
            self.label_stat1.setText("Calibration running: Please enter values")
            # Missuse the update here to write results from the calibration
            # As there are only simple tasks to do, this shouldn't really matter in speed
            self.label_voltage.setText(str(self.backend.getVtune()))
            calibration = self.backend.getCalibration()
            self.axesResults.cla()
            self.axesResults.plot(calibration[0], calibration[1], 'b-')
            self.mpl_result.figure.canvas.draw()
        elif modLabJack >= 4:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.btn_load.setEnabled(False)
            self.btn_delete.setEnabled(False)
            self.btn_enter.setEnabled(False)
            self.box_minvoltage.setEnabled(False)
            self.box_maxvoltage.setEnabled(False)
            self.box_stepvoltage.setEnabled(False)
            self.box_frequ.setEnabled(False)
            self.label_stat1.setText("Measurement running")
            # Even though it should still be present: Plot the current calibration once more
            calibration = self.backend.getCalibration()
            self.axesResults.cla()
            self.axesResults.plot(calibration[0], calibration[1], 'b-')
            self.mpl_result.figure.canvas.draw()

    # Starts the calibration of the vco. With every press on "Enter",
    # the displayed output voltage of the LabJack and the entered frequency are
    # saved together for a correlation
    def measure(self):
        minvolt = self.box_minvoltage.value()
        maxvolt = self.box_maxvoltage.value()
        stepvolt = self.box_stepvoltage.value()
        self.label_stat2.setText("Starting calibration...")
        if self.backend.startCalibration(minvolt, maxvolt, stepvolt):
            self.label_stat2.setText("Calibration started")
        else:
            self.label_stat2.setText("Failed to start calibration")

    # Aborts a running calibration
    def abort(self):
        self.label_stat2.setText("Aborting calibration...")
        if self.backend.stopCalibration():
            self.label_stat2.setText("Calibration aborted")
        else:
            self.label_stat2.setText("Failed to abort calibration")

    # Saves a finished calibration
    def save(self):
        path = str(self.line_file.text())
        self.label_stat2.setText("Saving calibration...")
        if self.backend.saveCalibration(path):
            self.label_stat2.setText("Calibration saved")
        else:
            self.label_stat2.setText("Failed to save calibration")

    # Loads a presaved calibration
    def load(self):
        path = str(self.line_file.text())
        self.label_stat2.setText("Loading calibration...")
        if self.backend.loadCalibration(path):
            self.label_stat2.setText("Calibration loaded")
        else:
            self.label_stat2.setText("Failed to load calibration")

    # Deletes the currently active calibration
    def delete(self):
        self.label_stat2.setText("Deleting calibration...")
        if self.backend.deleteCalibration():
            self.label_stat2.setText("Calibration deleted")
        else:
            self.label_stat2.setText("Failed to delete calibration")

    # Enters a new measuremnt while calibrating
    def enter(self):
        freq = self.box_frequ.value()
        self.label_stat2.setText("Entering frequency value...")
        if self.backend.enterCalibration(freq):
            self.label_stat2.setText("Value added")
        else:
            self.label_stat2.setText("Failed to add value")


# Gui for running an odmr measurement
class OdmrGui(QWidget):
    sigModLabJack = pyqtSignal()
    sigModCam = pyqtSignal()
    sigPlot = pyqtSignal()

    def __init__(self, backend):
        # Loading the odmr gui
        super(QWidget, self).__init__()
        uic.loadUi(path + "\odmr.ui", self)

        # Restoring last settings
        loadSettings(self, QSettings("SAppel", "DemoOdmr"))

        # Connecting to the program
        self.backend = backend

        # Connecting signals
        self.sigModLabJack.connect(self.updateMod)
        self.sigModCam.connect(self.updateMod)
        self.sigPlot.connect(self.mpl_results.figure.canvas.draw)

        # Preparing plot update
        self.thread = None
        self.plot = False

        # Preparing result area
        self.mpl_results.figure.clear()
        self.mpl_results.figure.add_axes([.05, .05, .85, .90])
        self.axesResults = self.mpl_results.figure.gca()

        # setting button actions
        self.btn_measure.clicked.connect(self.measure)
        self.btn_abort.clicked.connect(self.abort)
        self.btn_save.clicked.connect(self.save)
        self.box_seq.addItems(self.backend.customSeqs.keys())
        self.box_seq.currentIndexChanged.connect(self.customSeq)

        # Update
        self.sigModLabJack.emit()

        # Show the gui
        # self.show()

    # Updating gui settings after a labjack mod change
    def updateMod(self):
        modLabJack = self.backend.getModLabJack()
        modCam = self.backend.getModCam()
        if modLabJack == 0 and modCam == 0:
            # Enable/disable buttons and other elements
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.box_count.setEnabled(False)
            self.line_seq.setEnabled(False)
            # Print a status
            self.label_stat1.setText("No LabJack or Camera connected")
            # Enable/Diable plot update
            self.setPlot(False)
        elif modLabJack >= 1 and modCam == 0:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.box_count.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.label_stat1.setText("Camera disconnected")
            self.setPlot(False)
        elif modLabJack == 0 and modCam >= 1:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.box_count.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.label_stat1.setText("LabJack disconnected")
            self.setPlot(False)
        elif (modLabJack == 1 or modLabJack == 2) and (modCam == 1 or modCam == 2):
            self.btn_measure.setEnabled(True)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.box_min.setEnabled(True)
            self.box_max.setEnabled(True)
            self.box_step.setEnabled(True)
            self.box_count.setEnabled(True)
            self.line_seq.setEnabled(True)
            self.label_stat1.setText("LabJack and Camera connected")
            # Update the borders of the frequency boxes according to the calibration
            calib = self.backend.getCalibration()
            self.box_min.setMinimum(min(calib[1]))
            self.box_min.setMaximum(max(calib[1]))
            self.box_max.setMinimum(min(calib[1]))
            self.box_max.setMaximum(max(calib[1]))
            self.setPlot(False)
        elif modLabJack >= 3 and modCam < 3:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.box_count.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.label_stat1.setText("LabJack measuring")
            self.setPlot(False)
        elif modLabJack < 3 and modCam >= 3:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.box_count.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.label_stat1.setText("Camera measuring")
            self.setPlot(False)
        elif modLabJack == 4 and modCam == 4:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(True)
            self.btn_save.setEnabled(False)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.box_count.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.label_stat1.setText("ODMR-Measurement running")
            self.setPlot(True)
        elif modLabJack > 4 or modCam > 4:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.box_count.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.label_stat1.setText("Other measurement running")
            self.setPlot(False)

    # Change wether to plot results or not
    def setPlot(self, state):
        if state != self.plot:
            if state:
                self.thread = threading.Thread(target=self.plotTrigger)
                self.plot = True
                self.thread.start()
            else:
                self.plot = False
                del self.thread

    # Deals with triggering image plotting.
    def plotTrigger(self):
        # When plotting is activated
        while self.plot:
            # and the gui is visible,
            if self.isVisible():
                # before triggering the plot signal, prepare all plot areas
                odmr = self.backend.getOdmr()
                self.axesResults.cla()
                self.axesResults.plot(odmr[1], odmr[3], 'b-')
                # And send the plot signal
                self.sigPlot.emit()
                time.sleep(1)

    # Starts the ODMR-Measurement
    def measure(self):
        minfreq = self.box_min.value()
        maxfreq = self.box_max.value()
        stepfreq = self.box_step.value()
        count = self.box_count.value()
        seq = str(self.line_seq.text())
        self.label_stat2.setText("Starting ODMR...")
        if self.backend.startOdmr(minfreq, maxfreq, stepfreq, count, seq):
            self.label_stat2.setText("ODMR started")
        else:
            self.label_stat2.setText("Failed to start ODMR")

    # Aborts a running ODMR
    def abort(self):
        self.label_stat2.setText("Aborting ODMR...")
        if self.backend.stopOdmr():
            self.label_stat2.setText("ODMR aborted")
        else:
            self.label_stat2.setText("Failed to abort ODMR")

    # Saves the current measurement
    def save(self):
        path = str(self.line_file.text())
        self.label_stat2.setText("Saving ODMR...")
        if self.backend.saveOdmr(path):
            self.label_stat2.setText("ODMR saved")
        else:
            self.label_stat2.setText("Failed to save ODMR")

    # Enters a custom sequence stored in the backend
    def customSeq(self):
        if self.box_seq.currentIndex() > 0:
            self.label_stat2.setText("Loading custom sequence...")
            try:
                seq = self.backend.getCustomSeq(str(self.box_seq.currentText()))
                self.line_seq.setText(str(seq))
                self.label_stat2.setText("Custom sequence loaded")
            except:
                self.label_stat2.setText("Failed to load custom Sequence")
            self.box_seq.setCurrentIndex(0)


# Gui for running an rabi measurement
class RabiGui(QWidget):
    sigModLabJack = pyqtSignal()
    sigModCam = pyqtSignal()
    sigPlot = pyqtSignal()

    def __init__(self, backend):
        # Loading the rabi gui
        super(QWidget, self).__init__()
        uic.loadUi(path + "/rabi.ui", self)

        # Restoring last settings
        loadSettings(self, QSettings("SAppel", "DemoRabi"))

        # Connecting to the program
        self.backend = backend

        # Connecting signals
        self.sigModLabJack.connect(self.updateMod)
        self.sigModCam.connect(self.updateMod)
        self.sigPlot.connect(self.mpl_results.figure.canvas.draw)

        # Preparing plot update
        self.thread = None
        self.plot = False

        # Preparing result area
        self.mpl_results.figure.clear()
        self.mpl_results.figure.add_axes([.15, .05, .85, .95])
        self.axesResults = self.mpl_results.figure.gca()

        # setting button actions
        self.btn_measure.clicked.connect(self.measure)
        self.btn_abort.clicked.connect(self.abort)
        self.btn_save.clicked.connect(self.save)
        self.box_seq.addItems(self.backend.customSeqs.keys())
        self.box_seq.currentIndexChanged.connect(self.customSeq)

        # Update
        self.sigModLabJack.emit()

        # Show the gui
        # self.show()

    # Updating gui settings after a labjack mod change
    def updateMod(self):
        modLabJack = self.backend.getModLabJack()
        modCam = self.backend.getModCam()
        if modLabJack == 0 and modCam == 0:
            # Enable/disable buttons and other elements
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.box_count.setEnabled(False)
            self.box_freq.setEnabled(False)
            # Print a status
            self.label_stat1.setText("No LabJack or Camera connected")
            # Enable/Diable plot update
            self.setPlot(False)
        elif modLabJack >= 1 and modCam == 0:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.box_count.setEnabled(False)
            self.box_freq.setEnabled(False)
            self.label_stat1.setText("Camera disconnected")
            self.setPlot(False)
        elif modLabJack == 0 and modCam >= 1:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.box_count.setEnabled(False)
            self.box_freq.setEnabled(False)
            self.label_stat1.setText("LabJack disconnected")
            self.setPlot(False)
        elif (modLabJack == 1 or modLabJack == 2) and (modCam == 1 or modCam == 2):
            self.btn_measure.setEnabled(True)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(True)
            self.box_min.setEnabled(True)
            self.box_max.setEnabled(True)
            self.box_step.setEnabled(True)
            self.line_seq.setEnabled(True)
            self.box_count.setEnabled(True)
            self.box_freq.setEnabled(True)
            self.label_stat1.setText("LabJack and Camera connected")
            # Update the borders of the frequency box according to the calibration
            calib = self.backend.getCalibration()
            self.box_freq.setMinimum(min(calib[1]))
            self.box_freq.setMaximum(max(calib[1]))
            self.setPlot(False)
        elif modLabJack >= 3 and modCam < 3:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.box_count.setEnabled(False)
            self.box_freq.setEnabled(False)
            self.label_stat1.setText("LabJack measuring")
            self.setPlot(False)
        elif modLabJack < 3 and modCam >= 3:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.box_count.setEnabled(False)
            self.box_freq.setEnabled(False)
            self.label_stat1.setText("Camera measuring")
            self.setPlot(False)
        elif modLabJack == 5 and modCam == 5:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(True)
            self.btn_save.setEnabled(False)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.box_count.setEnabled(False)
            self.box_freq.setEnabled(False)
            self.label_stat1.setText("Rabi-Measurement running")
            self.setPlot(True)
        elif modLabJack > 4 or modCam > 4:
            self.btn_measure.setEnabled(False)
            self.btn_abort.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.box_min.setEnabled(False)
            self.box_max.setEnabled(False)
            self.box_step.setEnabled(False)
            self.line_seq.setEnabled(False)
            self.box_count.setEnabled(False)
            self.box_freq.setEnabled(False)
            self.label_stat1.setText("Other measurement running")
            self.setPlot(False)

    # Change wether to plot results or not
    def setPlot(self, state):
        if state != self.plot:
            if state:
                self.thread = threading.Thread(target=self.plotTrigger)
                self.plot = True
                self.thread.start()
            else:
                self.plot = False
                del self.thread

    # Deals with triggering image plotting.
    def plotTrigger(self):
        # When plotting is activated
        while self.plot:
            # and the gui is visible,
            if self.isVisible():
                # before triggering the plot signal, prepare all plot areas
                rabi = self.backend.getRabi()
                self.axesResults.cla()
                self.axesResults.plot(rabi[0], rabi[2], 'b-')
                # And send the plot signal
                self.sigPlot.emit()
                time.sleep(1)

    # Starts the Rabi-Measurement
    def measure(self):
        mintime = self.box_min.value()
        maxtime = self.box_max.value()
        steptime = self.box_step.value()
        seq = str(self.line_seq.text())
        count = self.box_count.value()
        freq = self.box_freq.value()
        self.label_stat2.setText("Starting Rabi...")
        if self.backend.startRabi(mintime, maxtime, steptime, seq, count, freq):
            self.label_stat2.setText("Rabi started")
        else:
            self.label_stat2.setText("Failed to start Rabi")

    # Aborts a running Rabi
    def abort(self):
        self.label_stat2.setText("Aborting Rabi...")
        if self.backend.stopRabi():
            self.label_stat2.setText("Rabi aborted")
        else:
            self.label_stat2.setText("Failed to abort Rabi")

    # Saves the current measurement
    def save(self):
        path = str(self.line_file.text())
        self.label_stat2.setText("Saving Rabi...")
        if self.backend.saveRabi(path):
            self.label_stat2.setText("Rabi saved")
        else:
            self.label_stat2.setText("Failed to save Rabi")

    # Enters a custom sequence stored in the backend
    def customSeq(self):
        if self.box_seq.currentIndex() > 0:
            self.label_stat2.setText("Loading custom sequence...")
            try:
                seq = self.backend.getCustomSeq(str(self.box_seq.currentText()))
                self.line_seq.setText(str(seq))
                self.label_stat2.setText("Custom sequence loaded")
            except:
                self.label_stat2.setText("Failed to load custom Sequence")
            self.box_seq.setCurrentIndex(0)
