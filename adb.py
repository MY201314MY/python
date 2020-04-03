import os
import time
arrary = None
def init():
    os.system("adb shell input tap 700 768")  # 主界面图标,后边两个参数表示坐标
    os.system("adb shell input tap 980 168")  # APP主页搜索按钮
    os.system("adb shell input tap 420 160")  # 点击搜索框跳出输入键盘

def serarch(ID):
    os.system("adb shell input text '{0}'".format(ID))#输入文本
    time.sleep(1.000)
    os.system("adb shell input tap 980 160")  # 点击搜索
    time.sleep(3.000) #延时以看清搜索内容
    os.system("adb shell input tap 840 148")  # 点击清空输入框内容(实际是点击输入框最后的'x'号)
    """
    可截图实现图像分析,这也正是朱哥研究生要走的路,网上有通过截图分析颜值然后关注靓女的,咳咳咳...
    """

if __name__ == '__main__':
    print("----Android----")
    # data.txt文件存储ID信息,每行以回车结尾,最后一行不要回车,否则最后一次搜索为搜索空ID
    with open("data.txt", 'r') as file:
        arrary = file.read().split("\n")
    print("There're {0} ID(s) totally.".format(len(arrary)))
    init()
    time.sleep(1.000)
    for i in range(len(arrary)):
        print("NO.{0}: ID:{1}".format(i+1, arrary[i]))
        serarch(ID = arrary[i])
    print("All done,thanks.")



