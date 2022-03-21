import win32con
import win32gui

from tool.coordinate import getRandomCoordinate
from tool.keyboard import openMap
from tool.mouse import move_click
from tool.win32tool import findTitle, get_window_rect
# import pydirectinput as pg
import pyautogui as pg

# 得到原神窗口的坐标
def getwin(title):
    hwnd = findTitle(title)
    win32gui.SetForegroundWindow(hwnd)
    win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    hwnd = findTitle(title)
    #  GetWindowRect 获得整个窗口的范围矩形，窗口的边框、标题栏、滚动条及菜单等都在这个矩形内
    x1, y1, x2, y2 = get_window_rect(hwnd)
    print(x1, y1, x2, y2)
    return x1, y1, x2, y2

def enter():
    x1, y1, x2, y2 = getwin('原神')
    x,y = getRandomCoordinate(x1, y1, x2, y2)
    move_click(x,y)

def trunRight():
    # x1, y1, x2, y2 = get_window_rect(findTitle('原神'))
    nx,ny = pg.position()
    # x, y = getRandomCoordinate(x1, ny, nx, ny)
    pg.moveTo(nx+1, ny, 1)
    # pg.moveTo(1365, 489, 0.3)

def trunLeft():
    # x1, y1, x2, y2 = get_window_rect(findTitle('原神'))
    nx,ny = pg.position()
    # x, y = getRandomCoordinate(nx, ny, x2, ny)
    # pg.moveTo(x, y, 0.3)
    # pg.moveTo(1365,489,0.3)
    # pg.moveTo(nx - 1, ny, 1)
    pg.click()

def meiri():
    openMap()


