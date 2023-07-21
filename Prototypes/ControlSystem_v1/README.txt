Instructions for running the control system.

1) Run Stellarium, making sure the Remote Control plugin's server is up and running, using a matching port as the one specified in the file MyEnv.py as the STEL_RC_PORT variable (I set it to be 8090)
2) Run Client.py (assuming your Anaconda terminal is working on this directory, the command is 'python ./Client.py')
3) On the Anaconda terminal, press ENTER to start tracking. The telescope should track whatever you have selected on Stellarium. Hit ENTER again to stop tracking. 
    - Alternatively, you can deselect an object on Stellarium by RIGHT CLICKING, which will automatically STOP the antenna's movement.