import numpy as np

# Cubic motion curve
def cubic_motion(t, h):
    pos = 3 * (t ** 2) - 2 * (t ** 3)
    vel = 6 * t * (1 - t)
    acc = 6 * (1 - 2 * t)
    return pos * h, vel * h, acc * h

# Cycloidal motion curve
def cycloidal_motion(t, h):
    pos = t - (np.sin(2 * np.pi * t) / (2 * np.pi))
    vel = 1 - np.cos(2 * np.pi * t)
    acc = 2 * np.pi * np.sin(2 * np.pi * t)
    return pos * h, vel * h, acc * h
