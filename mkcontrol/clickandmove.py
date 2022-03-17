import time

import pydirectinput as pg

def yuanshen():
    pg.moveTo(1172,434, 1)
    # pg.click()
    # pg.press('m')
    # pg.moveTo(1364, 656, 1)
    # pg.click()
    # pg.moveTo(1618, 715, 1)
    # pg.click()

def test():
    pg.moveTo(1500, -1080, 0.5)
    pg.moveTo(1108, -1067)
    pg.click()
    pg.moveTo(392, -574)
    pg.dragTo(654, -574, 1, button='left')
    pg.hotkey('command', 'c')
    pg.moveTo(340, -1018)
    pg.dragTo(-51, -1018, 1, button='left')
    pg.press('backspace')
    time.sleep(1)
    pg.hotkey('command', 'v')


if __name__ == '__main__':
    while True:
        yuanshen()
        time.sleep(3)


