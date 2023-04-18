module MyDemo {
    /**
     * Coords are azimuth, altitude
     * Altitude is also known as Elevation, used interchangebly
     * Tried using custom data structures but failed.
     **/

    /**
     *class Coords {
     *    double azi;
     *    double alt;
     *};
     **/

    interface Tracker {
        string getString();
        string getPos();
    };
};