import numpy as np
import matplotlib.pyplot as plt
from motion_curves import cubic_motion, cycloidal_motion
from dynamics import ball_screw_dynamics
from motor_sizing import size_motor

# Set Parameters for the simulation
h = 0.1  # Height for motion curve
force = 4440  # Force to cut wire
pitch = 0.05  # Pitch for ball screw
friction = 0.25  # Friction coefficient
radius = 0.05 / 2  # Radius of ball screw

# Time array for motion curve
t = np.linspace(0, 1, 100)

# Cubic motion curve
pos, vel, acc = cubic_motion(t, h)

# Plotting the motion curves
plt.plot(t, pos, label="Position")
plt.plot(t, vel, label="Velocity")
plt.plot(t, acc, label="Acceleration")
plt.legend()
plt.show()

# Dynamics and Motor Sizing
torque = ball_screw_dynamics(force, friction, pitch, radius)
motor = size_motor(torque, 3000)  # Example required speed

if motor:
    print(f"Selected Motor: {motor['name']} with Torque: {motor['torque']} Nm")
else:
    print("No suitable motor found")
