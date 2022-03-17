import time

import pyautogui as pg

if __name__ == '__main__':
    pg.moveTo(1500,-1080,0.5)
    pg.moveTo(1108,-1067)
    pg.click()
    pg.moveTo(392, -574)
    pg.dragTo(654, -574, 1, button='left')
    pg.hotkey('command', 'c')
    pg.moveTo(340, -1018)
    pg.dragTo(-51, -1018, 1, button='left')
    pg.press('backspace')
    time.sleep(1)
    pg.hotkey('command', 'v')


