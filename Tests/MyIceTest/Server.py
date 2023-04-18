import sys
import traceback
import Ice
import MyDemo

class TrackerI(MyDemo.Tracker):
    def getString(self, current=None):
        s = "Hello World"
        return s

    def getPos(self, current=None):
        c = "Coords(0.5, 0.99)"
        return c

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    adapter = ic.createObjectAdapterWithEndpoints(
        "SimpleTrackerAdapter", "default -p 10000")
    object = TrackerI()
    adapter.add(object, ic.stringToIdentity("SimpleTracker"))
    adapter.activate()
    print("Server Set")
    ic.waitForShutdown()
except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)