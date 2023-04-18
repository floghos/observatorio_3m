import sys
import traceback
import Ice
import RotorModule
import serial




class RotorI(RotorModule.Rotor):
    def gotoAltAzi(self, alt, azi, current=None):
        # Writing any commands to the controller always seem to return a response, which should be cleared from the buffer 
        # before issuing the next   
        #ser.reset_input_buffer()
        # The output of the serial.write() method is an integer representing the number of bytes written to the serial port
        alt = int(alt)
        azi = int(azi)
        command = f'W{azi:03d} {alt:03d}\r\n'
        print(command)
        
        #ser.write(command.encode('UTF-8'))
        
        #Reading response from serial port
        #response = ser.readline().decode().strip()
        #print(f"Response: {response}")
        
# TODO:
# [] Func to check if antenna is on target
#       - Idea: 
#           * define a "close-enough-to-observe" parameter for our telescope (probably related to the observation beam)
#           * use the C2 command to ask the controller for the rotors position and compare distance to target}}
#
# [] Add a "recording" module. This would probably make use of the previuosly defined "is-on-target" function.
#


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