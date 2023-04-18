import sys
import traceback
import Ice
import RotorModule
import serial
from env.py import *




class RotorI(RotorModule.Rotor):
    # Currently using YAESU protocol. Planning to change to Rot2Prog eventually.

    def gotoAziAlt(self, azi, alt, current=None):
        #ser.reset_input_buffer()
        # The output of the serial.write() method is an integer representing the number of bytes written to the serial port
        azi = int(azi)
        alt = int(alt)
        command = f'W{azi:03d} {alt:03d}\r\n'
        print(command)
        
        #ser.write(command.encode('UTF-8'))
        
        #Reading response from serial port
        #response = ser.readline().decode().strip()
        #print(f"Response: {response}")

    def getCurrentPos(self, current=None):
        command = f'C2\r\n'
        #ser.reset_input_buffer()
        #ser.write(command.encode('UTF-8'))

        #pos = ser.readline().decode().strip()
        return pos


status = 0
ic = None
try:
    #ser = serial.Serial('COM3', 9600, timeout=5)

    ic = Ice.initialize(sys.argv)
    adapter = ic.createObjectAdapterWithEndpoints("SimpleRotorAdapter", "default -p 10001")
    object = RotorI()
    adapter.add(object, ic.stringToIdentity("SimpleRotor"))
    adapter.activate()
    print("Rotor Service activated")
    ic.waitForShutdown()
except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
        # Closing the serial connection
        #ser.close()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)