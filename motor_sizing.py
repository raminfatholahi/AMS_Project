# Motor catalog
motors = [
    {"name": "SGMSV-20A", "torque": 6.36, "max_speed": 5000},
    {"name": "SGMSV-25A", "torque": 7.96, "max_speed": 6000},
    {"name": "SGMSV-30A", "torque": 9.80, "max_speed": 5000},
    {"name": "SGMSV-40A", "torque": 12.6, "max_speed": 5000},
    {"name": "SGMSV-50A", "torque": 15.8, "max_speed": 5000},
    {"name": "SGMSV-70A", "torque": 22.3, "max_speed": 5000}
]

# Function to size motor based on required torque and speed
def size_motor(required_torque, required_speed):
    for motor in motors:
        if motor["torque"] >= required_torque and motor["max_speed"] >= required_speed:
            return motor
    return None
