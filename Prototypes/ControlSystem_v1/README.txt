Instructions for running the control system.

1) Run Stellarium, making sure the Remote Control plugin's server is up and running, using a matching port as the one specified in the file MyEnv.py as the STEL_RC_PORT variable (I set it to be 8090)
2) Run Client.py (assuming your Anaconda terminal is working on this directory, the command is 'python ./Client.py')
    2.1) Select the appropiate Boot Option:
        - "Start required services automatically" will automatically launch all the services required for the system to work.
        - "I have manually started the required services" will only launch the main Client that conects to the required services. Select this if you have already started the required services.
        - "Exit" will exit the application without launching anything.
    2.2) On the Anaconda terminal, select the desired Control Mode:
        - "Tracking Mode": The telescope should point to and track whatever you have selected on Stellarium. Hit ENTER again to stop tracking. 
            - Alternatively, you can deselect an object on Stellarium by RIGHT CLICKING, which will automatically STOP the antenna's movement.
        - "Manual Mode": The terminal will wait for you to input azi/alt coordinates. (E.g.: 160 72) (where 160 is azimuth, 72 is altitude/elevation. Both are required on the same line)
