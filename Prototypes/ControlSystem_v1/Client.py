import sys
import traceback
import Ice
import TrackingModule, RotorModule
import time, re
#from MyEnv import *
import MyEnv
import subprocess
import threading

def parseAziAlt(res):
    #aziAlt = re.findall("\d+\.\d+", res)
    aan = res.split()
    azi = float(aan[0])
    alt = float(aan[1])
    target_name = ""
    for i in range(2, len(aan)):
        target_name += " " + aan[i]

    return (azi, alt), target_name.strip()


class Telescope:
    def __init__(self, ce, r_prx):
        # Distance to be considered close enough to "be on target", expressed in degrees. (INT)
        self.close_enough = ce # consider changing to "resolution" or something like that
        
        # Reference to rotor server proxy
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

exit_tracking_loop = threading.Event()
         
def trackingLoop():
    #source = input()
    source = ""
    prev_s = ""
    print("Tracking...")
    while not exit_tracking_loop.is_set():
        try:
            res = TRACKER_PRX.getAziAlt(source)
            sys.stdout.write('\r' + res + (' ' * max(0, (len(prev_s) - len(res))))) 
            prev_s = res
            
            if res != "NoSourceSelected":
                (azi, alt) , target_name = parseAziAlt(res)
                #print(azi, alt, target_name)
                ROTOR_PRX.gotoAziAlt(azi, alt)
            else:
                ROTOR_PRX.stop()
            #    print(res)
            
            time.sleep(1) # arbitrary timer
        except Ice.UnknownException:
            print(f"[{source}] doesn't exist")
            break
    ROTOR_PRX.stop()
    print("\nTracking stopped\n")
        


def main():
    #_alt, _azi = parseAziAlt(ROTOR_PX.getCurrentPos())
    close_enough_angle = 1
    #tel = Telescope(close_enough_angle, ROTOR_PRX)
    #print("testing env vars ", ROTOR_IP)
    tloop = threading.Thread(target=trackingLoop)
    
    input("Press enter to start tracking")
    print("Press Enter to stop tracking")
    tloop.start()
    
    input()
    exit_tracking_loop.set()
    tloop.join()
        



def run_service(script_path):
    return subprocess.Popen(["python", script_path])

def terminate_service(process):
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill() 
        # I read somewhere that .kill() is the same as .terminate() in windows, unlike in Linux. 
        # If this is the case then this is try/except block should be redundant but for now I'll keep this in here to be safe
    
def bootOptions() -> int:
    # The purpose of this is to ask the user if they want to start required services automatically or do so themselves
    # Useful when running separate services on separate machines
    optionsList = ["Start required services automatically", "I have manually started the required services", "Exit"]
    option = 0
    while not ((len(optionsList) - option >= 0) and (option != 0)):
        print("Select the corresponding option:")
        for idx, op in enumerate(optionsList):
            print(f"{idx+1}) {op}")
        try:
            option = abs(int(input()))
        except ValueError:
            print("Please enter a valid number")
            continue
    return option


if __name__ == '__main__':
    status = 0

    # Starting Tracking and Rotor services
    list_of_services = ["Rotor_Server.py", "Tracking_Server.py"]
    subprocesses = []
    
    option = bootOptions()
    
    if option == 1:
        for service in list_of_services:
            p = run_service(service)
            subprocesses.append(p)
    elif option == 2:
        pass
    elif option == 3:
        sys.exit(status)

    
    IC = None

    try:
        IC = Ice.initialize(sys.argv)
        
        # Creating Tracker Proxy
        tracker_base_prx = IC.stringToProxy(f"SimpleTracker:default -p {MyEnv.TRACKER_PORT}")
        TRACKER_PRX = TrackingModule.TrackerPrx.checkedCast(tracker_base_prx)
        if not TRACKER_PRX:
            raise RuntimeError("Invalid tracker proxy")
        
        # Creating Rotor Proxy
        
        #For a remote rotor server use the following proxy
        #rotor_base_prx = IC.stringToProxy(f"SimpleRotor:default -h {MyEnv.ROTOR_IP} -p {MyEnv.ROTOR_PORT}")
        
        #For a local rotor server use the following proxy (no IP is needed, so we remove the -h option)
        rotor_base_prx = IC.stringToProxy(f"SimpleRotor:default -p {MyEnv.ROTOR_PORT}") 
        
        ROTOR_PRX = RotorModule.RotorPrx.checkedCast(rotor_base_prx)
        if not ROTOR_PRX:
            raise RuntimeError("Invalid rotor proxy")

        main()
        
    except:
        traceback.print_exc()
        status = 1

    if IC:
        # Clean up
        try:
            IC.destroy()
            # terminate child subprocesses
            for p in subprocesses:
                terminate_service(p)

        except:
            traceback.print_exc()
            status = 1

    sys.exit(status)

