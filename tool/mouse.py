import random
import time

# import pydirectinput as pg
import pyautogui as pg

def random_time():
    t = round(random.uniform(0.2, 2),2)
    print("本次鼠标随机移动时间：" + str(t))
    return t

def move_click(x,y):
    print("当前位置："+str(pg.position())+"\t目标位置："+str(x)+","+str(y),end="\t")
    t = random_time()
    pg.moveTo(x, y, t)
    pg.click()

def randomCoordinate(x1, y1, x2, y2):
    return random.randint(x1,x2),random.randint(y1,y2)


def random_move_click(screen, adjustmentList):
    x1, y1, x2, y2 = screen.boundary(adjustmentList)
    x,y = randomCoordinate(x1, y1, x2, y2)
    move_click(x,y)



if __name__ == '__main__':
    move_click(1361, 673)