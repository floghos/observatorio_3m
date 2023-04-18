import sys
import traceback
import Ice
import TrackingModule, RotorModule
import time, re
from env import *

class Telescope:
    def __init__(self, ce, cp):
        self.close_enough = ce
        self.current_pos = cp
        self.current_target = None


def main():
    #print("testing env vars ", ROTOR_IP)
    while True:
        print("Hit Enter to start tracking, type 'exit' to quit.")
        source = input()
        if source == 'exit': 
            break
        prev_s = ""
        print(f'Tracking {source}')
        try:
            while True:
                try:
                    res = tracker.getAziAlt(source)
                    #print(res)
                    if res != "NoSourceSelected":
                        sys.stdout.write('\r' + res + (' ' * max(0, (len(prev_s) - len(res))))) 
                        prev_s = res
                        aziAlt = re.findall("\d+\.\d+", res)
                        alt = float(aziAlt[0])
                        azi = float(aziAlt[1])
                        #rotor.gotoAziAlt(alt, azi)
                    else:
                        print(res)
                    time.sleep(1)
                except Ice.UnknownException:
                    print(f"[{source}] doesn't exist")
                    break

        except KeyboardInterrupt:
            print("\nTracking stopped\n")
            pass


if __name__ == '__main__':
    status = 0
    ic = None

    try:
        ic = Ice.initialize(sys.argv)
        
        # Creating Tracker Proxy
        port_tracker = 10000
        tracker_base_prx = ic.stringToProxy(f"SimpleTracker:default -p {port_tracker}")
        tracker = TrackingModule.TrackerPrx.checkedCast(tracker_base_prx)
        if not tracker:
            raise RuntimeError("Invalid tracker proxy")
        
        # Creating Rotor Proxy
        """ ip_rotors = ROTOR_IP
        port_rotors = 10001
        rotor_base_prx = ic.stringToProxy(f"SimpleRotor:default -h {ip_rotors} -p {port_rotors}")
        rotor = RotorModule.RotorPrx.checkedCast(rotor_base_prx)
        if not rotor:
            raise RuntimeError("Invalid rotor proxy") """

        main()
        
    except:
        traceback.print_exc()
        status = 1
    
    main()

    if ic:
        # Clean up
        try:
            ic.destroy()
        except:
            traceback.print_exc()
            status = 1

    sys.exit(status)

