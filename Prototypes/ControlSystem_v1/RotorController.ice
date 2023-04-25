module RotorModule {
    interface Rotor {
        /**
         * Commands the rotor to go to a given Azimuth/Altitude
         **/
        void gotoAziAlt(float azi, float alt);

        /**
         * Retrieves the current position of the rotors as a pair of coordinates.
         * Returned as a string of the following form: "AZ=aaa EL=eee"
         **/
        string getCurrentPos();

        /**
         * Stops any ongoing command. (e.g: movement)
         **/
        void stop();
    };
};