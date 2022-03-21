import pyautogui as pg
import sys

def getPosition():
    try:
        while True:
            x, y = pg.position()
            positionStr = 'x:' + str(x) + " , y:" + str(y)
            sys.stdout.write("\r{0}".format(positionStr))
            sys.stdout.flush()
    except KeyboardInterrupt:
        print('出错了')

import win32api
import time

def aaa():
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

    while True:
        a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)

        if a != state_left:  # Button state changed
            state_left = a
            print(a)
            if a < 0:
                print('Left Button Pressed')
                x, y = pg.position()
                positionStr = 'x:' + str(x) + " , y:" + str(y)
                print(positionStr)
            # else:
            #     print('Left Button Released')
            #     x, y = pg.position()
            #     positionStr = 'x:' + str(x) + " , y:" + str(y)
            #     print(positionStr)

        if b != state_right:  # Button state changed
            state_right = b
            print(b)
            if b < 0:
                print('Right Button Pressed')
            else:
                print('Right Button Released')
        time.sleep(0.001)

if __name__ == '__main__':
    aaa()