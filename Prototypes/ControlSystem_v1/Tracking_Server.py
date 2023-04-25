import sys
import traceback
import Ice
import TrackingModule
import requests
import MyEnv
# import json



class TrackerI(TrackingModule.Tracker):
    def getAziAlt(self, source, current=None):
        if source != '':
            source = f'name={source}&'
        req = requests.get(f'http://localhost:{MyEnv.STEL_RC_PORT}/api/objects/info?{source}format=json')
        if req.ok:
            data = req.json()
            print(f'{data["name"]}')
            return f'{data["azimuth"]:.10f} {data["altitude"]:.10f} {data["name"]}'
        else:
            #I will assume that the error code is 404 and no source was selected
            print("No Source Selected")
            return 'NoSourceSelected'


status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    adapter = ic.createObjectAdapterWithEndpoints("SimpleTrackerAdapter", f"default -p {MyEnv.TRACKER_PORT}")
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