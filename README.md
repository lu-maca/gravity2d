# gravity2d
Simple python code for 2d gravity problems

# How does this work?
Configuration file config.txt contains information about the numerical method, the run options and the problem to be solved; it should have the following structure:
$NUMERICAL_METHOD
dt = time step
tfin = final simulation time
integrator = integrator type (EC for Euler-Cromer [1], Verlet for Velocity Verlet [2])
printfreq = print result frequency
plot (if this option is present, the program draws the the solution)
\--
$PARTICLE
mass = particle mass
charge = charge (not used)
position = x y
velocity = v_x v_y
acceleration = a_x a_y
color= r g b
\--
$PARTICLE 
...

# Run
Run the program by launch.bat script.

[1] https://www.physics.udel.edu/~bnikolic/teaching/phys660/numerical_ode/node2.html
[2] https://www.physics.udel.edu/~bnikolic/teaching/phys660/numerical_ode/node5.html
