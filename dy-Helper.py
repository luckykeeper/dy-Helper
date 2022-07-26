# -*- coding:utf-8 -*-
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# adb need imports os

import os,datetime,random,time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# 帮助信息窗口 对应 Button3
def showHelpInfo():
    HelpInfo = Tk()
    HelpInfo.title("dy-Helper 帮助信息")
    HelpInfo.iconbitmap('.\\assets\\images\\favicon.ico')
    HelpInfo.geometry("300x150")
    HelpInfo.configure(bg = "#FFFFFF")
    HelpInfoText = Text(HelpInfo, width=300, height=150, undo=True, autoseparators=False)
    HelpInfoText.pack()
    HelpInfoText.insert("end", '手机打开ADB连接电脑，点 “开启连接”，打开短视频页面，点击“开始刷视频”。\n结束时请点击“断开连接”，再关闭程序。\n找不到设备时请点击“重启连接”。\n软件免费开源，仅供学习使用，谨防受骗。\n个人博客：https://www.luckykeeper.site\nGitHub：https://github.com/luckykeeper\n下载、更新请前往Github 如果觉得软件不错，请去 GitHub点个Star~\n版本 ver1.0 Build 20200721 By Luckykeeper')

# 获取时间
def gettime():
    # 获取当前时间
    nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return nowTime

# 获取随机时间间隔
def getSleepingTime():
    sleepTime = random.uniform(3.4,30.6)
    return sleepTime

# 获取随机起始结束坐标 起始X 起始Y 结束X 结束Y
def getSildePosition():
    # 获取手机分辨率
    deviceResolution = os.popen("adb.exe shell wm size").read().split("Physical size: ")[1]

    ResX = int(deviceResolution.split("x")[0])
    ResY = int(deviceResolution.split("x")[1])

    # 滑动时间
    slideTime = random.uniform(0.3*1000,0.5*1000)

    # 基于 1080x1920推算需要的XY位置
    # startX = random.randint(300,700)
    # startY = random.randint(500,1200)

    startX = random.randint(300,ResX-380)
    startY = random.randint(1000,ResY-500)

    if startX < 400:
        stopX = startX+random.randint(5,49)
    elif startX > 600:
        stopX = startX-random.randint(5,49)
    elif random.randint(1,10) > 5:
        stopX = startX+random.randint(10,100)
    else:
        stopX = startX-random.randint(10,100)

    stopY = startY-random.randint(500,800)

    return str(startX)+" "+str(startY)+" "+str(stopX)+" "+str(stopY)+" "+str(int(slideTime))

# 输出文本到文本框方法
# DebugWindow -> entry_2
# DevicesTree -> entry_1
def outputText(outputWindow,str):
    outputWindow.insert("end", str+"\n")

# 检测手机信息，反映在左边窗口
def showDeviceInfo():
    devicesInfo = os.popen("adb.exe devices -l").read()
    deviceId = devicesInfo.split("               device")[0][-8:]
    deviceModel = devicesInfo.split("model:")[1].split(" device:")[0]
    deviceResolution = os.popen("adb.exe shell wm size").read().split("Physical size: ")[1]
    outputText(entry_1,"————————————————————————")
    outputText(entry_1,gettime())
    outputText(entry_1,"设备ID | 设备型号 | 分辨率")
    outputText(entry_1,deviceId+" | "+deviceModel+" | "+deviceResolution)
    outputText(entry_1,"————————————————————————")

# 开始ADB连接 对应 Button4
def connectADB():
    outputText(entry_2,"————————————————————————")
    outputText(entry_2,gettime())
    outputText(entry_2,"准备开始使用ADB连接手机，请注意观察左侧连接设备列表，如果没有找到设备请检查连接是否正常！")
    outputText(entry_2,"当前使用的ADB版本和位置如下：")
    outputText(entry_2,os.popen("adb.exe --version").read())
    outputText(entry_2,"开始连接手机，请稍等……")
    outputText(entry_2,gettime())
    outputText(entry_2,os.popen("adb.exe devices -l").read())
    showDeviceInfo()

# 断开ADB连接 对应 Button6
def disconnectADB():
    outputText(entry_2,"————————————————————————")
    outputText(entry_2,gettime())
    outputText(entry_2,"正在断开ADB连接，请稍等！")
    outputText(entry_2,"输出信息：")
    outputText(entry_2,os.popen("adb.exe disconnect").read())
    outputText(entry_2,os.popen("adb.exe kill-server").read())
    outputText(entry_2,"如果你看到“disconnected everything”，那么你可以安全断开手机了！")

# 重启ADB连接 对应 Button5
def reconnectADB():
    outputText(entry_2,"————————————————————————")
    outputText(entry_2,gettime())
    outputText(entry_2,"正在重启ADB连接，请稍等！")
    outputText(entry_2,os.popen("adb.exe reconnect device").read())
    outputText(entry_2,gettime())
    outputText(entry_2,"重启ADB连接成功！")
    outputText(entry_2,"以下是设备信息，请注意同时观察左侧窗口最新设备信息！")
    outputText(entry_2,os.popen("adb.exe devices -l").read())
    showDeviceInfo()

# 开始刷视频，对应 Button1
def startFlashVideo():
    outputText(entry_2,"————————————————————————")
    # while 检查用变量
    global runWhile
    runWhile = True
    outputText(entry_2,gettime())
    outputText(entry_2,"准备启动抖音极速版")
    os.system("adb.exe shell am start -n com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity")
    outputText(entry_2,"抖音极速版启动完成！进入主页面开始刷视频！")
    outputText(entry_2,"在控制台Crtl+C可退出")
    print("在控制台Crtl+C可退出")

    time.sleep(getSleepingTime())
    while runWhile:
        outputText(entry_2,gettime())
        sleepTime = getSleepingTime()
        adbCommand="adb shell input swipe "+getSildePosition()
        outputText(entry_2,"将执行命令："+adbCommand)
        print("将执行命令：",adbCommand)
        os.system(adbCommand)
        time.sleep(sleepTime)

# 暂停刷视频，对应 Button2
def pauseFlashVideo():
    outputText(entry_2,"————————————————————————")
    outputText(entry_2,gettime())
    outputText(entry_2,"正在停止刷视频……")
    global runWhile
    runWhile = False

window = Tk()

window.geometry("1280x760")
window.configure(bg = "#FFFFFF")
window.title("dy-Helper Ver 1.0 Build 20220721 By Luckykeeper | https://www.luckykeeper.site | https://github.com/luckykeeper")
window.iconbitmap('D:\\dy-Helper\\build\\assets\\images\\favicon.ico')

# GUI

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 760,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    760.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    69.0,
    50.0,
    499.0,
    710.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    69.0,
    50.0,
    499.0,
    80.0,
    fill="#A8A5A5",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    284.0,
    395.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=69.0,
    y=80.0,
    width=430.0,
    height=628.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    868.0,
    496.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#000000",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=553.0,
    y=282.0,
    width=630.0,
    height=426.0
)

canvas.create_text(
    199.0,
    50.0,
    anchor="nw",
    text="已连接设备列表",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    816.0,
    248.0,
    anchor="nw",
    text="调试信息",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: startFlashVideo(),
    relief="flat"
)
button_1.place(
    x=553.0,
    y=178.0,
    width=174.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pauseFlashVideo(),
    relief="flat"
)
button_2.place(
    x=781.0,
    y=178.0,
    width=174.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: print("button_3 clicked"),
    command=lambda: showHelpInfo(),
    relief="flat"
)
button_3.place(
    x=1009.0,
    y=178.0,
    width=174.0,
    height=60.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: connectADB(),
    relief="flat"
)
button_4.place(
    x=553.0,
    y=80.0,
    width=174.0,
    height=60.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: reconnectADB(),
    relief="flat"
)
button_5.place(
    x=781.0,
    y=78.0,
    width=174.0,
    height=60.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: disconnectADB(),
    relief="flat"
)
button_6.place(
    x=1008.0,
    y=81.0,
    width=174.0,
    height=60.0
)
window.resizable(False, False)
window.mainloop()
