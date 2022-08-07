import serial


class Movement:
    def __init__(self):
        self.ser = serial.Serial("com2", 115200, timeout=0.5)
        # # under raspy
        # ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.5)
        if self.ser.isOpen():
            self.ser.close()

    def forward(self):
        self.ser.open()
        self.ser.write(b"$CTRL11\n")
        self.ser.flushOutput()
        self.ser.close()

    def backward(self):
        self.ser.open()
        self.ser.write(b"$CTRL00\n")
        self.ser.flushOutput()
        self.ser.close()

    def left(self):
        self.ser.open()
        self.ser.write(b"$CTRL10\n")
        self.ser.flushOutput()
        self.ser.close()

    def right(self):
        self.ser.open()
        self.ser.write(b"$CTRL01\n")
        self.ser.flushOutput()
        self.ser.close()

    def bump(self, num=None):
        if num is None:
            raise ValueError
        if num == 0:
            self.ser.open()
            self.ser.write(b"$BUMP00\n")
            self.ser.flushOutput()
            self.ser.close()
        if num == 1:
            self.ser.open()
            self.ser.write(b"$BUMP01\n")
            self.ser.flushOutput()
            self.ser.close()
        if num == 2:
            self.ser.open()
            self.ser.write(b"$BUMP10\n")
            self.ser.flushOutput()
            self.ser.close()
        if num == 3:
            self.ser.open()
            self.ser.write(b"$BUMP11\n")
            self.ser.flushOutput()
            self.ser.close()
