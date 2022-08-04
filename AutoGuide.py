from Package.Movement import Movement
from Package.GPS_Package import get_gps_data
import math

BDS = Movement()

Target_Site = [38.16114433333333, 126]


def get_cur_data():
    LATITUDE, LONGITUDE, _, _, _, NAVI_DIRECTION = get_gps_data("com3")
    cur_Site = [LATITUDE, LONGITUDE]
    # First adjust angle
    Angle = math.degrees(math.atan((Target_Site[0] - cur_Site[0]) / (Target_Site[1] - cur_Site[1])))
    if Target_Site[0] < cur_Site[0] and Target_Site[1] < cur_Site[1]:
        Angle = Angle + 180
    if Target_Site[0] < cur_Site[0] and Target_Site[1] > cur_Site[1]:
        Angle = Angle + 360
    if Target_Site[0] > cur_Site[0] and Target_Site[1] < cur_Site[1]:
        Angle = Angle + 180
    Distance = math.sqrt((Target_Site[0] - cur_Site[0]) ** 2 + (Target_Site[1] - cur_Site[1]) ** 2)
    return cur_Site, Angle, Distance, NAVI_DIRECTION


if __name__ == '__main__':
    cur_Site, Angle, Distance, NAVI_DIRECTION = get_cur_data()
    while Distance > 1:
        while abs(NAVI_DIRECTION - Angle) > 5:
            if Angle > NAVI_DIRECTION:
                BDS.left()
                print("Turn left")
            if Angle < NAVI_DIRECTION:
                BDS.right()
                print("Turn right")
            cur_Site, Angle, Distance, NAVI_DIRECTION = get_cur_data()
            print(Angle, Distance)
        for i in range(5):
            BDS.forward()
            print("Forward")
