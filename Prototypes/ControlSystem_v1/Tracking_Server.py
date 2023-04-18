import sys
import traceback
import Ice
import TrackingModule
import requests
# import json



class TrackerI(TrackingModule.Tracker):
    def getAziAlt(self, source, current=None):
        if source != '':
            source = f'name={source}&'
        req = requests.get(f'http://localhost:8090/api/objects/info?{source}format=json')
        data = req.json()
        #return f'Azi: {data["azimuth"]:.10f} Alt: {data["altitude"]:.10f}'
        return f'{data["azimuth"]:.10f} {data["altitude"]:.10f}'


status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    adapter = ic.createObjectAdapterWithEndpoints("SimpleTrackerAdapter", "default -p 10000")
    object = TrackerI()
    adapter.add(object, ic.stringToIdentity("SimpleTracker"))
    adapter.activate()
    print("Tracking Service activated")
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