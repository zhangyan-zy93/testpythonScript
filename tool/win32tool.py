import ctypes.wintypes

import win32api, win32con, win32gui

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