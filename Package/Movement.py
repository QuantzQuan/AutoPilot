from Package.GPS_Package import get_gps_data, draw_map
import serial


class Movement:
    def __init__(self):
        self.ser = serial.Serial("com2", 115200, timeout=0.5)
        # # under raspy
        # ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.5)
        if self.ser.isOpen():
            self.ser.close()
        self.ser.open()

    def forward(self):
        self.ser.write(b"$CTRL11\n")

    def backward(self):
        self.ser.write(b"$CTRL00\n")

    def left(self):
        self.ser.write(b"$CTRL10\n")

    def right(self):
        self.ser.write(b"$CTRL01\n")

    def bump(self, num=None):
        if num is None:
            raise ValueError
        if num == 0:
            self.ser.write(b"$BUMP00\n")
        if num == 1:
            self.ser.write(b"$BUMP01\n")
        if num == 2:
            self.ser.write(b"$BUMP10\n")
        if num == 3:
            self.ser.write(b"$BUMP11\n")
