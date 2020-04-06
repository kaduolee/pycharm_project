import time
import win32gui, win32ui, win32con, win32api
def window_capture(filename):
    hwnd = 0 # 視窗的編號，0號表示當前活躍視窗
    # 根據視窗控制代碼獲取視窗的裝置上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根據視窗的DC獲取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC建立可相容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 建立bigmap準備儲存圖片
    saveBitMap = win32ui.CreateBitmap()
    # 獲取監控器資訊
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#圖片大小
    # 為bitmap開闢空間
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，將截圖儲存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 擷取從左上角（0，0）長寬為（w，h）的圖片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    beg = time.time()
    for i in range(10):
        window_capture("haha.jpg")
        end = time.time()
    print(end - beg)


if __name__ == '__main__':  
    window_capture('test')