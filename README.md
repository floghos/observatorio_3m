# observatorio_3m
Diseñando un sistema de control para el observatorio Wenulafken

# Objetivo
El objetivo de este proyecto es diseñar un sistema de control para el radiotelescopio de 3m de Wenulafken, utilizando el framework de Ice como middleware.



# TODO:
[ ] Func to check if antenna is on target
       - Idea: 
           * define a "close-enough-to-observe" parameter for our telescope (probably related to the observation beam)
           * use the C2 command to ask the controller for the rotors position and compare distance to target

[ ] Add a "recording" module. This would probably make use of the previuosly defined "is-on-target" function.
