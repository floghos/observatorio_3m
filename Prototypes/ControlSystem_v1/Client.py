import sys
import traceback
import Ice
import TrackingModule, RotorModule
import time, re
from env.py import *

class Telescope:
    def __init__(self, ce):
        self.close_enough = ce
        self.current_target = (0, 0)


def main():
    while True:
        print("Type the name of an object to track:")
        source = input()
        if source == 'exit': 
            break
        prev_s = ""
        print(f'Tracking {source}')
        try:
            while True:
                try:
                    res = tracker.getAziAlt(source)
                    sys.stdout.write('\r' + res + (' ' * max(0, (len(prev_s) - len(res)))))
                    altAzi = re.findall("\d+\.\d+", res)

                    alt = float(altAzi[0])
                    azi = float(altAzi[1])
                    rotor.gotoAziAlt(alt, azi)
                    time.sleep(3)
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
        port_tracker = 10000
        tracker_base_prx = ic.stringToProxy(f"SimpleTracker:default -p {port_tracker}")
        tracker = TrackingModule.TrackerPrx.checkedCast(tracker_base_prx)
        if not tracker:
            raise RuntimeError("Invalid tracker proxy")
        
        # 
        ip_rotors = ROTOR_IP
        port_rotors = 10001
        rotor_base_prx = ic.stringToProxy(f"SimpleRotor:default -h {ip_rotors} -p {port_rotors}")
        rotor = RotorModule.RotorPrx.checkedCast(rotor_base_prx)
        if not rotor:
            raise RuntimeError("Invalid rotor proxy")

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

