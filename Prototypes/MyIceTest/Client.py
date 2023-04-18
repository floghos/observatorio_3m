import sys
import traceback
import Ice
import MyDemo

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("SimpleTracker:default -p 10000")
    tracker = MyDemo.TrackerPrx.checkedCast(base)
    if not tracker:
        raise RuntimeError("Invalid proxy")

    s = tracker.getString()
    print(s)
    
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
