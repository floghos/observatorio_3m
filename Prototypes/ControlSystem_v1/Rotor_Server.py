import sys
import traceback
import Ice
import RotorModule
import serial
import MyEnv


class RotorI(RotorModule.Rotor):
    # Currently using YAESU protocol. Planning to change to Rot2Prog eventually.

    def gotoAziAlt(self, azi, alt, current=None) -> None:
        # The following is using the YAESU protocol
        azi = int(azi)
        alt = int(alt)
        command = f'W{azi:03d} {alt:03d}\r\n'
        print(command)
        
        ser.reset_input_buffer()
        ser.write(command.encode('UTF-8'))
        # The output of the serial.write() method is an integer representing the number of bytes written to the serial port
        
        #Reading response from serial port
        response = ser.readline().decode().strip()
        #print(f"Response: {response}")

    def getCurrentPos(self, current=None) -> str:
        # The following is using the YAESU protocol
        command = f'C2\r\n'
        # The C2 command returns current rotor position in as: "AZ=aaa EL=eee"

        ser.reset_input_buffer()
        ser.write(command.encode('UTF-8'))
        res = ser.readline().decode().strip()

        s = res.split()
        s[0] = s[0].strip('AZ=')
        s[1] = s[1].strip('EL=')
        pos = s[0] + " " + s[1]

        return pos
    
    def stop(self, current=None) -> None:
        # The following is using the YAESU protocol
        command = f'S\r\n'
        ser.reset_input_buffer()
        ser.write(command.encode('UTF-8'))
        pass


status = 0
ic = None
try:
    ser = serial.Serial('COM6', 9600, timeout=5)

    ic = Ice.initialize(sys.argv)
    adapter = ic.createObjectAdapterWithEndpoints("SimpleRotorAdapter", f"default -p {MyEnv.ROTOR_PORT}")
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
        ser.close()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)