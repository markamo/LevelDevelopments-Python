import serial
import time

device_path = '/dev/ttyUSB0'
baudrate = 38400

ser = serial.Serial(device_path, baudrate)
print("Device connected!\nInitilizing ...")
ser.write(b'setoasc')
res = ser.read(2)

print("Device response: ", res)

def get_inclination(refreshtime=0.01):
    ser.write(b'get-x&y')
    res = ser.read(18)
    res_x = float(res[0:8])
    res_y = float(res[9:17])
    print("Inclination (RAW): ", res, "X = ", res_x, "Y = ", res_y)
    time.sleep(refreshtime)

try:
    while True:
        get_inclination()
except KeyboardInterrupt:
    ser.close()
    print("Device disconnected!")
    pass



