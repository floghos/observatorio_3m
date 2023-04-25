import sys
import traceback
import Ice
import TrackingModule, RotorModule
import time, re
#from MyEnv import *
import MyEnv

def parseAziAlt(res):
    #aziAlt = re.findall("\d+\.\d+", res)
    aan = res.split()
    alt = float(aan[0])
    azi = float(aan[1])
    target_name = ""
    for i in range(2, len(aan)):
        target_name += " " + aan[i]

    return (azi, alt), target_name.strip()

class Telescope:
    def __init__(self, ce, r_prx):
        # Distance to be considered close enough to "be on target", expressed in degrees. (INT)
        self.close_enough = ce
        
        # Reference to rotor proxy
        self.rotor_prx = r_prx
        
        # Coords of the current target being tracked. Stored as a tuple of the form (azimuth, altitude)
        self.current_target = None

        # Current position of the rotors. Stored as a tuple of the form (azimuth, altitude)
        self.current_pos, _name = parseAziAlt(self.rotor_prx.getCurrentPos())

    def update_current_pos(self) -> None:
        self.current_pos, _name = parseAziAlt(self.rotor_prx.getCurrentPos())

    def track_object(self, target_azi, target_alt, name):
        if self.current_target != name:
            self.current_target = name
        self.update_current_pos()
        if not self.is_on_target(target_azi, target_alt):
            self.rotor_prx.gotoAziAlt(target_azi, target_alt)

    def is_on_target(self, target_azi, target_alt) -> bool:
        return not (self.current_pos[0] - self.close_enough < target_azi < self.current_pos[0] + self.close_enough) or \
            not (self.current_pos[1] - self.close_enough < target_alt < self.current_pos[1] + self.close_enough)

         

def main():
    #_alt, _azi = parseAziAlt(ROTOR_PX.getCurrentPos())
    close_enough_angle = 2
    #tel = Telescope(close_enough_angle, ROTOR_PRX)
    #print("testing env vars ", ROTOR_IP)
    while True:
        print("Hit Enter to start tracking. Type 'exit' to quit.")
        source = input()
        if source == 'exit': 
            break
        prev_s = ""
        print(f'Tracking {source}')
        try:
            while True:
                try:
                    res = TRACKER_PRX.getAziAlt(source)
                    sys.stdout.write('\r' + res + (' ' * max(0, (len(prev_s) - len(res))))) 
                    prev_s = res
                    #(azi, alt) , target_name = parseAziAlt(res)
                    #print(azi, alt, target_name)
                    #ROTOR_PRX.gotoAziAlt(azi, alt)
                    
                    #if res != "NoSourceSelected":
                    #else:
                    #    print(res)
                    
                    time.sleep(1) # arbitrary timer
                except Ice.UnknownException:
                    print(f"[{source}] doesn't exist")
                    break

        except KeyboardInterrupt:
            print("\nTracking stopped\n")
            pass


if __name__ == '__main__':
    status = 0
    IC = None

    try:
        IC = Ice.initialize(sys.argv)
        
        # Creating Tracker Proxy
        tracker_base_prx = IC.stringToProxy(f"SimpleTracker:default -p {MyEnv.TRACKER_PORT}")
        TRACKER_PRX = TrackingModule.TrackerPrx.checkedCast(tracker_base_prx)
        if not TRACKER_PRX:
            raise RuntimeError("Invalid tracker proxy")
        
        # Creating Rotor Proxy
        
        #rotor_base_prx = IC.stringToProxy(f"SimpleRotor:default -h {MyEnv.ROTOR_IP} -p {MyEnv.ROTOR_PORT}")
        #For a locally running rotor server there's no need to add a host ip (-h).
        #Example: 
        #    rotor_base_prx = IC.stringToProxy(f"SimpleRotor:default -p {MyEnv.ROTOR_PORT}") 
        
        #ROTOR_PRX = RotorModule.RotorPrx.checkedCast(rotor_base_prx)
        #if not ROTOR_PRX:
        #    raise RuntimeError("Invalid rotor proxy")

        main()
        
    except:
        traceback.print_exc()
        status = 1

    if IC:
        # Clean up
        try:
            IC.destroy()
        except:
            traceback.print_exc()
            status = 1

    sys.exit(status)

