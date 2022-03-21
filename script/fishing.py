import time

from script.base import MineScreen
from script.enum.fishingStateEnum import FishingStateEnum
from tool.mouse import random_time, random_move_click
from tool.picTool import contrastScreen
import pyautogui as pg


class Fishing:

    def __init__(self):
        self.screen = MineScreen()
        self.totalFishingCount = 0
        self.pondFishingCount = 0
        # todo 此处待改为基于配置读取
        self.maxWaitFishingTime = 15
        self.maxPondFishingCount = 3
        self.fishingInterval = 0.3
        self.maxRetryCount = 5
        self.outerInterval = 1
        self.xiaohongPic = "..\\pic\\小红鱼.png"
        self.hongErPic='todo 待截图'
        self.arriveSign='..\\pic\\diaoyu.png'
        self.startSign="..\\pic\\开始钓鱼.png"
        self.state = FishingStateEnum.notStarted
        self.timeInterval = self.outerInterval
    # todo 待截图计算钓鱼进度条位置
    # todo 待截图拉钩时出现的图片和位置比例

    def startFishing(self):
        l = [0.54,0.45,0.23,0.12]
        if contrastScreen(self.screen,self.arriveSign, l):
            print("到达钓鱼点")
            pg.press('f')
            print("进入钓鱼页面")
            self.timeInterval = self.fishingInterval
            self.state = FishingStateEnum.prepareFishing
            print("修改当前刷新时间为钓鱼模式刷新时间,当前刷新频率:"+str(self.timeInterval))
        else:
            pass

    def prepareFishing(self):
    #     todo 待完成 根据鱼的种类选择鱼饵种类的方法，图片已存
        self.state = FishingStateEnum.fishing
        l = [0.69,0.93,0.2,0.05]
        random_move_click(self.screen, l)

    def changeBait(self):
        # 换饵
        pass

    def fishing(self):
        pass

    def doFishing(self):
        if self.state == FishingStateEnum.notStarted:
            self.startFishing()
        if self.state == FishingStateEnum.prepareFishing:
            self.prepareFishing()



if __name__ == '__main__':
    o = Fishing()
    while True:
        o.doFishing()
        time.sleep(o.timeInterval)
    pass

