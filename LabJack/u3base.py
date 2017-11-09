import LabJackPython as LJ
import numpy as np
import io

#Returns a list of serial numbers of all connected u3-devices
def listSerials():
    return list(LJ.listAll(LJ.LJ_dtU3, LJ.LJ_ctUSB).keys())


#Connects to a device with matching serial number and returns its handle,
#or none, if there is no device with such handle
def connectToSerial(serial):
    u3dict = LJ.listAll(LJ.LJ_dtU3, LJ.LJ_ctUSB)
    try:
        connect = u3dict[serial]
        device = LJ.openLabJack(LJ.LJ_dtU3, LJ.LJ_ctUSB, str(connect["localId"]), 0)
        return device.handle
    except KeyError:
        return None


#Returns the voltage applied between two selected pins.
#If only one pin is given, voltage is measured against gnd.
#Ensures analog input mode
def readAN(handle, pinp, pinn=31):
    #Structure of ePut/eGet: (handle, command, channel, value, x1)
    LJ.ePut(handle, LJ.LJ_ioPUT_ANALOG_ENABLE_BIT, pinp, 1, 0)
    if pinn != 31:
        #Measuring against pinn (not recommended for pin 0-3)
        LJ.ePut(handle, LJ.LJ_ioPUT_ANALOG_ENABLE_BIT, pinn, 1, 0)
        return LJ.eGet(handle, LJ.LJ_ioGET_AIN_DIFF, pinp, 0, pinn)
    else:
        #Measuring against gnd (recommended)
        return LJ.eGet(handle, LJ.LJ_ioGET_AIN, pinp, 0, 0)


#Sets the voltage output on a given pin (only two avaible)
#Ensures analog output mode
def writeAN(handle, pin, voltage):
    LJ.ePut(handle, LJ.LJ_ioPUT_DAC, pin, voltage, 0)


#Returns boolean values for the digital state of the pin.
#Ensures digital input mode
def readIO(handle, pin):
    LJ.ePut(handle, LJ.LJ_ioPUT_ANALOG_ENABLE_BIT, pin, 0, 0)
    return bool(LJ.eGet(handle, LJ.LJ_ioGET_DIGITAL_BIT, pin, 0, 0))


#Sets the digital output of selected pin.
#Returns 0 if successfull
#Ensures digital output mode
def writeIO(handle, pin, state):
    LJ.ePut(handle, LJ.LJ_ioPUT_ANALOG_ENABLE_BIT, pin, 0, 0)
    LJ.ePut(handle, LJ.LJ_ioPut_DIGITAL_BIT, pin, int(state), 0)


listu3 = listSerials()
print listu3
handle = connectToSerial(listu3[0])
writeAN(handle, 0, 0)
writeAN(handle, 1, 0)

filename = str(raw_input("Enter filename: "))
datei = io.open(filename, "w")
mode = bool(int(raw_input("Write test (0) or read test(1)?")))
pin = int(raw_input("Enter pin number: "))
if mode:
    while True:
        try:
            external = float(raw_input("Measure the applied voltage: "))
        except:
            break
        internal = readAN(handle, pin)
        print ("Measured %f V") % (internal)
        line = unicode(str(external) + ", " + str(internal) + "\n")
        datei.write(line)
else:
    for internal in np.arange(0, 4.85, 0.2):
        writeAN(handle, pin, internal)
        print("Applied %f V") % (internal)
        external = float(raw_input("Measure the applied voltage: "))
        line = unicode(str(external) + ", " + str(internal) + "\n")
        datei.write(line)

datei.close()
