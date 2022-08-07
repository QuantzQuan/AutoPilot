from Package.Movement import Movement
from Package.GPS_Package import get_gps_data, init_serial
import math
import time

BDS = Movement()
SER = init_serial("/dev/ttyUSB0")

Target_Site = [36.163389, 120.49210033333334]


def get_cur_data(ser=None):
    LATITUDE, LONGITUDE, _, _, _, NAVI_DIRECTION = get_gps_data(ser=SER)
    cur_Site = [LATITUDE, LONGITUDE]
    # First adjust angle
    Angle = math.degrees(math.atan((Target_Site[0] - cur_Site[0]) / (Target_Site[1] - cur_Site[1])))
    if Target_Site[0] < cur_Site[0] and Target_Site[1] < cur_Site[1]:
        Angle = Angle + 180
    if Target_Site[0] < cur_Site[0] and Target_Site[1] > cur_Site[1]:
        Angle = Angle + 360
    if Target_Site[0] > cur_Site[0] and Target_Site[1] < cur_Site[1]:
        Angle = Angle + 180
    Distance = getDistance(Target_Site[0], Target_Site[1], cur_Site[0], cur_Site[1])
    print(cur_Site, Angle, Distance, NAVI_DIRECTION)
    return cur_Site, Angle, Distance, NAVI_DIRECTION


def getDistance(latA, lonA, latB, lonB):
    ra = 6378140  # 赤道半径
    rb = 6356755  # 极半径
    flatten = (ra - rb) / ra  # Partial rate of the earth
    # change angle to radians
    radLatA = math.radians(latA)
    radLonA = math.radians(lonA)
    radLatB = math.radians(latB)
    radLonB = math.radians(lonB)

    pA = math.atan(rb / ra * math.tan(radLatA))
    pB = math.atan(rb / ra * math.tan(radLatB))
    x = math.acos(math.sin(pA) * math.sin(pB) + math.cos(pA) * math.cos(pB) * math.cos(radLonA - radLonB))
    c1 = (math.sin(x) - x) * (math.sin(pA) + math.sin(pB)) ** 2 / math.cos(x / 2) ** 2
    c2 = (math.sin(x) + x) * (math.sin(pA) - math.sin(pB)) ** 2 / math.sin(x / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (x + dr)
    distance = round(distance / 1000, 4)
    return distance


if __name__ == '__main__':
    cur_Site, Angle, Distance, NAVI_DIRECTION = get_cur_data(ser=SER)
    while Distance > 0.001:
        while abs(NAVI_DIRECTION - Angle) > 5:
            if Angle > NAVI_DIRECTION:
                BDS.left()
                print("Turn left")
            if Angle < NAVI_DIRECTION:
                BDS.right()
                print("Turn right")
            cur_Site, Angle, Distance, NAVI_DIRECTION = get_cur_data(ser=SER)
            print(Angle, Distance)
            time.sleep(0.1)
        BDS.forward()
        print("Forward")
        time.sleep(0.1)
    print("Arrived!")
