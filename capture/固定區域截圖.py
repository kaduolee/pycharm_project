from time import sleep
from PIL import ImageGrab
 
# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
bbox = (760, 0, 1160, 1080)
im = ImageGrab.grab(bbox)
 
# 参数 保存截图文件的路径
im.save('zy.png')



'''屏幕的視頻錄製'''
m=int(input("输入录屏几分钟："))
m=m*60
n=1
while n<m:
    sleep(0.02)
    im=ImageGrab.grab()
    local=(r"%s.jpg"%(n))
    im.save(local,'jpeg')
    n=n+1

