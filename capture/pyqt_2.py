# from Qt import __binding__
#
# print(__binding__)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

'''
# Qt 中無法導入 QScreen 類
try:
    from PySide2.QtGui import QScreen
except:
    from PyQt5.QtGui import QScreen
'''
import sys


class WScreenShot(QWidget):
    # win = ''
    #
    # @classmethod
    # def run(cls):
    #     cls.win = cls()
    #     cls.win.show()

    def __init__(self, parent=None):
        super(WScreenShot, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''background-color:black; ''')
        self.setWindowOpacity(0.6)
        # desktop = QApplication.desktop()
        # rect = desktop.availableGeometry()
        desktopRect = QDesktopWidget().screenGeometry()
        self.setGeometry(desktopRect)
        self.setCursor(Qt.CrossCursor)
        self.blackMask = QBitmap(desktopRect.size())
        self.blackMask.fill(Qt.black)
        self.mask = self.blackMask.copy()
        self.isDrawing = False
        self.startPoint = QPoint()
        self.endPoint = QPoint()

    def paintEvent(self, event):
        if self.isDrawing:
            self.mask = self.blackMask.copy()
            pp = QPainter(self.mask)
            pen = QPen()
            pen.setStyle(Qt.NoPen)
            pp.setPen(pen)
            brush = QBrush(Qt.white)
            pp.setBrush(brush)
            pp.drawRect(QRect(self.startPoint, self.endPoint))
            self.setMask(QBitmap(self.mask))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.endPoint = self.startPoint
            self.isDrawing = True

    def mouseMoveEvent(self, event):
        if self.isDrawing:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # PySide2
            # screenshot = QPixmap.grabWindow(QApplication.desktop().winId())
            # PyQt5
            # screenshot = QApplication.primaryScreen().grabWindow(0)
            # 通用
            screenshot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
            rect = QRect(self.startPoint, self.endPoint)
            outputRegion = screenshot.copy(rect)
            outputRegion.save('./sho54t.jpg', format='JPG', quality=100)
            self.close()


if __name__ == '__main__':
    # app = QApplication.instance() or QApplication(sys.argv)
    # WScreenShot.run()
    # app.exec_()

    app = QApplication(sys.argv)
    win = WScreenShot()
    win.show()
    app.exec_()

    # app = QApplication(sys.argv)
    # win = DesktopChosenBox(700, 500, 30)
    # win.show()
    # app.exec_()























# =============================================================================
# import time
# import win32gui, win32ui, win32con, win32api
# 
# 
# def window_capture(filename):
#     #1、获得应用窗口句柄，0号表示当前活跃窗口
#     hwnd=win32gui.FindWindow(0,"窗口名字")   
#     # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
#     hwndDC = win32gui.GetWindowDC(hwnd)
#     # 根据窗口的DC获取mfcDC(注意主窗口用的是win32gui库，操作位图截图是用win32ui库)
#     mfcDC = win32ui.CreateDCFromHandle(hwndDC)
#     # mfcDC创建可兼容的DC，实际在内存开辟空间（ 将位图BitBlt至屏幕缓冲区（内存），而不是将屏幕缓冲区替换成自己的位图。同时解决绘图闪烁等问题）
#     neicunDC = mfcDC.CreateCompatibleDC()
#     # 创建bigmap准备保存图片
#     saveBitMap = win32ui.CreateBitmap()
#     
#     #6、设置位图的大小以及内容（图片为应用窗口的整个截图）
#     width=40
#     height=40  #（长宽为自己想要图片的大小，单位是像素）
#     saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
#     #7、将位图放置在兼容DC，即将位图数据放置在刚开辟的内存里
#     neicunDC.SleteObject(savebitmap)    
#     #8、截取位图部分，并将截图保存在剪贴板    
#     neicunDC.BitBle((w1,w2),width,height,mfcDC,(x,y),win32con.SRCCOPY)
#     #9、将截图数据从剪贴板中取出，并保存为bmp图片
#     saveBitMap.SaveBitmapFile(neicunDC,filename)
#     #10、释放内存
#     win32gui.delete(savebitmap.GetHandle())
#     neicunDC.DeleteDC()
#     mfcDC.DeleteDC()
#     win32gui.Release(hwnd,hwndDC)    
#     
# # =============================================================================
# #     # 获取监控器信息
# #     MoniterDev = win32api.EnumDisplayMonitors(None, None)
# #     w = MoniterDev[0][2][2]
# #     h = MoniterDev[0][2][3]
# #     # print w,h　　　#图片大小
# #     # 为bitmap开辟空间
# #     saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
# #     # 高度saveDC，将截图保存到saveBitmap中
# #     neicunDC.SelectObject(saveBitMap)
# #     # 截取从左上角（0，0）长宽为（w，h）的图片
# #     neicunDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
# #     saveBitMap.SaveBitmapFile(neicunDC, filename)
# # 
# # =============================================================================
# 
# beg = time.time()
# for i in range(10):
#     window_capture("haha.jpg")
# end = time.time()
# print(end - beg)
# =============================================================================

