from enum import Enum


class FishingStateEnum(Enum):
    notStarted = -1
    # 继续，不做处理
    continued = 0
    #钓鱼准备
    prepareFishing = 1
    # 开始钓鱼
    fishing = 2
    # 用力 抛鱼饵，点击蓄力
    exert = 5