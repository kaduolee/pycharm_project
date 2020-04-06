#对后台窗口截图
import win32gui, win32ui, win32con
from ctypes import windll
from PIL import Image
import cv2
import numpy

#获取后台窗口的句柄，注意后台窗口不能最小化
hWnd = win32gui.FindWindow("NotePad",None) #窗口的类名可以用Visual Studio的SPY++工具获取
#获取句柄窗口的大小信息
left, top, right, bot = win32gui.GetWindowRect(hWnd)
width = right - left
height = bot - top
#返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
hWndDC = win32gui.GetWindowDC(hWnd)
#创建设备描述表
mfcDC = win32ui.CreateDCFromHandle(hWndDC)
#创建内存设备描述表
saveDC = mfcDC.CreateCompatibleDC()
#创建位图对象准备保存图片
saveBitMap = win32ui.CreateBitmap()
#为bitmap开辟存储空间
saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
#将截图保存到saveBitMap中
saveDC.SelectObject(saveBitMap)
#保存bitmap到内存设备描述表
saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)

#如果要截图到打印设备：
###最后一个int参数：0-保存整个窗口，1-只保存客户区。如果PrintWindow成功函数返回值为1
#result = windll.user32.PrintWindow(hWnd,saveDC.GetSafeHdc(),0)
#print(result) #PrintWindow成功则输出1

#保存图像
##方法一：windows api保存
###保存bitmap到文件
saveBitMap.SaveBitmapFile(saveDC,"img_Winapi.bmp")

##方法二(第一部分)：PIL保存
###获取位图信息
bmpinfo = saveBitMap.GetInfo()
bmpstr = saveBitMap.GetBitmapBits(True)
###生成图像
im_PIL = Image.frombuffer('RGB',(bmpinfo['bmWidth'],bmpinfo['bmHeight']),bmpstr,'raw','BGRX',0,1)
##方法二（后续转第二部分）

##方法三（第一部分）：opencv+numpy保存
###获取位图信息
signedIntsArray = saveBitMap.GetBitmapBits(True)
##方法三（后续转第二部分）

#内存释放
win32gui.DeleteObject(saveBitMap.GetHandle())
saveDC.DeleteDC()
mfcDC.DeleteDC()
win32gui.ReleaseDC(hWnd,hWndDC)
