import time

from tool.coordinate import getRandomCoordinate
from tool.mouse import move_click
from zonghe.yuanshenwindow import getwin


class MineScreen():
    def clickRandom(self):
        move_click(self.getYSRandomCoordinate())

    def boundary(self,adjustmentList):
        x, y, w, h = self.top_left_x, self.top_left_y, self.bottom_right_x, self.bottom_right_y
        if len(adjustmentList) == 4:
            x = int(self.top_left_x + adjustmentList[0] * self.wide)
            y = int(self.top_left_y + adjustmentList[1] * self.high)
            w = int(x + adjustmentList[2] * self.wide)
            h = int(y + adjustmentList[3] * self.high)
        return x, y, w, h

    def getYSRandomCoordinate(self):
        # todo 此处需要加上特殊位置校验
        # todo 此处大概搞个比例
        return getRandomCoordinate(self.top_left_x, self.top_left_y, self.bottom_right_x, self.bottom_right_y)

    def __init__(self):
        self.top_left_x, self.top_left_y, self.bottom_right_x, self.bottom_right_y = getwin('原神')
        self.wide = self.bottom_right_x - self.top_left_x
        self.high = self.bottom_right_y - self.top_left_y



