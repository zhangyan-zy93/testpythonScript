import datetime
import time

from PIL import ImageGrab


from script.base import MineScreen
from similarity.getPicCoordinates import MatchImg, load_image_file

# 屏幕指定位置截图，返回截图对象
def getScreenShot(x1, y1, x2, y2):
    print(x1, y1, x2, y2)
    dt_ms = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))  # X1,Y1,X2,Y2
    imgPath = "../pic/yunxing/"+dt_ms+'.png'
    img.save(imgPath)
    return load_image_file(imgPath)


def contrastScreen(screen, picPath, adjustmentList):
    x, y, w, h = screen.boundary(adjustmentList)
    big = getScreenShot(x,y,w,h)
    small = load_image_file(picPath)
    process = MatchImg(big, small, 0.5)
    points = process.get_img_center()
    if len(points)==0:
        return False
    return True

if __name__ == '__main__':
    o = MineScreen()
    adjustmentList = [0.69,0.93,0.2,0.05]
    x, y, w, h = o.boundary(adjustmentList)
    time.sleep(0.2)
    big = getScreenShot(x, y, w, h)
