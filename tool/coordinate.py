import random


def getRandomCoordinate(x1,y1,x2,y2):
    "返回这个矩形中的一个随机的位置"
    return random.randint(x1,x2),random.randint(y1,y2)
