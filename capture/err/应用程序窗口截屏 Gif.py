import win32gui
import sys
import os
import imageio
import time
import numpy as np
from PIL import ImageGrab
 
hwnd_title = dict()
 
def get_all_hwnd(hwnd,mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({win32gui.GetWindowText(hwnd):hwnd})
 
def GetMsgFromInput():
    Msg = input()
    Msg_list = Msg.split(',')
    if len(Msg_list)!= 4:
        print("输入格式错误")
        sys.exit(0)
    return Msg_list
 
def ShowSomeThings(hwnd_title):
    WinName = hwnd_title.keys()
 
    for Name in WinName:
        print(Name)
 
    print("请输入要截屏的窗口名称以及GIF属性")
    print("格式 : 窗口名称,GIF图帧数,GIF图速度,GIF图位置")
    print("注意:① 程序运行的时候不要用其他窗口遮挡住要截屏的窗口,速度建议0.3-0.1")
    print("注意:② 有可能你截取的GIF是不完整的，那是因为截取的是原本100%的文本显示，一般电脑推荐是125%或者更高，如果想要截取完整的GIF点击左下角开始键，设置，将显示调至100%，再运行该程序...................")
 
def CheckType(Mlist):
    Msg = []
    try:
        Msg.append(Mlist[0])
        Msg.append(int(Mlist[1]))
        Msg.append(float(Mlist[2]))
        Msg.append(Mlist[3])
    except ValueError:
        print("输入参数错误")
        sys.exit(0)
    return Msg
 
def CheckIsNoFile(path):
    try:
        os.remove(path)
    except IOError:
        pass
    return
 
if __name__ == "__main__":
    
    imgs = []
    frames = []
 
    win32gui.EnumWindows(get_all_hwnd, 0)                       #得到窗口列表
    ShowSomeThings(hwnd_title)                                  #显示说明
    Msg_list = GetMsgFromInput()                                #得到信息
    Msg_list = CheckType(Msg_list)                              #检查类型
    CheckIsNoFile(Msg_list[3])                                  #是否存在该文件（存在即删掉）
 
    try:
        hwnd = hwnd_title[Msg_list[0]]                          #得到句柄
    except KeyError:
        print("没有该窗口！")
        sys.exit(0)
 
 
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)     #得到窗口矩形框
    rect = (left, top, right, bottom)
 
    for i in range(Msg_list[1]):
        time.sleep(0.1)
        imgs.append(ImageGrab.grab(rect))                       #屏幕截图
        print("Catch  IMG_" + str(i+1) + " OK")                 #显示进度
 
    for i,img in enumerate(imgs):
        img = img.convert("RGB")                                # 通过convert将RGBA格式转化为RGB格式，以便后续处理 
        img = np.array(img)                                     # im还不是数组格式，通过此方法将img转化为数组
        frames.append(img)                                      # 批量化
        print(str(i) + " OK")
 
    imageio.mimsave(Msg_list[3], frames, 'GIF', duration=Msg_list[2])        #转为GIF
    print("-----------------DONE!-----------------")
