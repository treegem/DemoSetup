from labjacku3 import *
import numpy
import io

listu3 = listSerials()
print listu3
u3 = LJU3(listu3[0])
u3.writeAN(0, 0)
u3.writeAN(1, 0)

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
        internal = u3.readAN(pin)
        print ("Measured %f V") % (internal)
        line = unicode(str(external) + ", " + str(internal) + "\n")
        datei.write(line)
else:
    for internal in numpy.arange(0, 4.85, 0.2):
        u3.writeAN(pin, internal)
        print("Applied %f V") % (internal)
        external = float(raw_input("Measure the applied voltage: "))
        line = unicode(str(external) + ", " + str(internal) + "\n")
        datei.write(line)

datei.close()
del u3