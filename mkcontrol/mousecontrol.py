import pyautogui as pg
import sys

try:
    while True:
        x, y = pg.position()
        positionStr = 'x:' + str(x) + " , y:" + str(y)
        sys.stdout.write("\r{0}".format(positionStr))
        sys.stdout.flush()
except KeyboardInterrupt:
    print('出错了')
