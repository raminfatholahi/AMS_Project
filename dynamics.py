import numpy as np

# Ball Screw Dynamic Model
def ball_screw_dynamics(force, friction, pitch, radius):
    # Calculate the torque needed based on force, friction, and screw pitch
    torque = force * radius * np.tan(pitch + friction)
    return torque
