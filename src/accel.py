# Import the mpu6050 class and sleep function from respective modules.
from mpu6050 import mpu6050
from time import sleep
import math
# Initialize the MPU-6050 sensor with the I2C address 0x68.
sensor = mpu6050(0x68)

class Accelerator:
    def __init__():
        self prev_filtered_x = 0
        self prev_filtered_y = 0
        self prev_filtered_z = 0

    def get_net_acceleration(self, accel_data):

        return math.sqrt((accel_data['x'] ** 2) + (accel_data['y'] ** 2) + (accel_data['z'] ** 2))

    def low_pass_filter(self, previous_filtered_value, new_raw_value, alpha):
        """
        Applies a simple first-order low-pass filter.

        Args:
            previous_filtered_value (float): The previously filtered value.
            new_raw_value (float): The new raw accelerometer reading.
            alpha (float): The filter coefficient (between 0 and 1).
                        Higher alpha means more smoothing (more weight on previous value).
                        Lower alpha means less smoothing (more weight on new value).

        Returns:
            float: The new filtered value.
        """
        return alpha * previous_filtered_value + (1 - alpha) * new_raw_value

    # Example usage:
    # Initialize with the first raw reading or 0
    filtered_accel_x = 0 
    alpha_value = 0.85 # Adjust this value for desired smoothing

    # Simulate receiving new accelerometer data
    raw_data = [1.2, 1.5, 1.1, 2.0, 1.3, 1.6, 1.4, 2.2, 1.5, 1.7]

    filtered_data = []
    for new_reading in raw_data:
        filtered_accel_x = low_pass_filter(filtered_accel_x, new_reading, alpha_value)
        filtered_data.append(filtered_accel_x)
        print(f"Raw: {new_reading:.2f}, Filtered: {filtered_accel_x:.2f}")

    print("\nFiltered data:", filtered_data)
    def get_gyro_data(self):
        gyro_data = sensor.get_gyro_data()
        return gyro_data

    def get_accelearator_values(self)
        accel_data = sensor.get_accel_data()
        if self.prev_filtered_x == 0:
            self.prev_filtered_x = accel_data['x']
        else:
            
        if self.prev_filtered_y == 0:
            self.prev_filtered_y = accel_data['y']
        if self.prev_filtered_z == 0:
            self.prev_filtered_z = accel_data['z']

if __name__ == "__main__":
# Infinite loop to continuously read data from the sensor.
#TODO: Clean exit
#TODO: calibrationhttps://makersportal.com/blog/calibration-of-an-inertial-measurement-unit-imu-with-raspberry-pi-part-ii?srsltid=AfmBOooObBxxE3nYRF4GYXp_gVcbPqOs0Z-s4J5bKXVxrzNw54Rbn4-C
accelerator = Accelerator()
    while True:
        # Retrieve accelerometer data from the sensor.
        accel_data = sensor.get_accel_data()
        # Retrieve gyroscope data from the sensor.
        gyro_data = sensor.get_gyro_data()
        # Retrieve temperature data from the sensor.
        temp = sensor.get_temp()

        # Print accelerometer data.
        print("Accelerometer data")
        print("x: " + str(accel_data['x']))
        print("y: " + str(accel_data['y']))
        print("z: " + str(accel_data['z']))
        print("net acceleration: %f"%get_net_acceleration(accel_data))
        # Print gyroscope data.
        print("Gyroscope data")
        print("x: " + str(gyro_data['x']))
        print("y: " + str(gyro_data['y']))
        print("z: " + str(gyro_data['z']))

        # Print the temperature in Celsius.
        print("Temp: " + str(temp) + " C")

        # Pause for 0.5 seconds before the next read cycle.
        sleep(0.5)
