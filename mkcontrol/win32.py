import ctypes.wintypes
import sys
import time

import cv2
import win32api, win32con, win32gui
from PIL import Image, ImageGrab
from PyQt5.QtWidgets import QApplication
hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def get_window_pos(name):
    name = name
    handle = win32gui.FindWindow(0, name)
    # 获取窗口句柄
    if handle == 0:
        return None
    else:
        # 返回坐标值和handle
        return win32gui.GetWindowRect(handle), handle

def findTitle(window_title):
    '''
    查找指定标题窗口句柄
    @param window_title: 标题名
    @return: 窗口句柄
    '''
    hWndList = []
    # 函数功能：该函数枚举所有屏幕上的顶层窗口，办法是先将句柄传给每一个窗口，然后再传送给应用程序定义的回调函数。
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    for hwnd in hWndList:
        # 函数功能：该函数获得指定窗口所属的类的类名。
        # clsname = win32gui.GetClassName(hwnd)
        # 函数功能：该函数将指定窗口的标题条文本（如果存在）拷贝到一个缓存区内
        title = win32gui.GetWindowText(hwnd)
        if (title == window_title):
            print("标题：", title, "句柄：", hwnd)
            break
    return hwnd

def get_window_rect(hwnd):
    try:
        f = ctypes.windll.dwmapi.DwmGetWindowAttribute
    except WindowsError:
        f = None
    if f:
        rect = ctypes.wintypes.RECT()
        DWMWA_EXTENDED_FRAME_BOUNDS = 9
        f(ctypes.wintypes.HWND(hwnd),
          ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
          ctypes.byref(rect),
          ctypes.sizeof(rect)
          )
        return rect.left, rect.top, rect.right, rect.bottom






def fetch_image():
    # (x1, y1, x2, y2), handle = get_window_pos('ExpressVPN')
    # # 发送还原最小化窗口的信息
    # win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    # # 设为高亮
    # win32gui.SetForegroundWindow(handle)
    # # 截图
    # print(x1, y1, x2, y2)
    # img = ImageGrab.grab(x1, y1, x2, y2)
    # img.save("11.jpg")
    # screen = QApplication.primaryScreen()
    # img = screen.grabWindow(QApplication.desktop().winId(), x1, y1, x2-x1, y2-y1)
    # img.save("screenshot.jpg")
    #   GetCursorPos 获取鼠标指针的当前位置

    hwnd = findTitle('原神')

    win32gui.SetForegroundWindow(hwnd)
    win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    hwnd = findTitle('原神')
    #  GetWindowRect 获得整个窗口的范围矩形，窗口的边框、标题栏、滚动条及菜单等都在这个矩形内
    x, y, w, h = get_window_rect(hwnd)
    print((x, y, w, h))
    # 鼠标坐标减去指定窗口坐标为鼠标在窗口中的坐标值
    # bbox = (x, y, w, h)
    # im = ImageGrab.grab(bbox)
    # a = im.transpose(Image.ROTATE_90)
    # 参数 保存截图文件的路径
    # a.save('1.png')

    time.sleep(0.2)
    im = ImageGrab.grab(bbox=(x, y, w, h))  # X1,Y1,X2,Y2
    im.show()








if __name__ in "__main__":
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t is not "":
            print(h, t)
    fetch_image()
