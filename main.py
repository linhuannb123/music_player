import os
import random
import ctypes

print("\n选择这次要播放音乐的文件夹位置，输入A为默认路径，输入B自己重新选择路径:\n")
m = input('请输入你的选项：')

if m == 'B':
    music_dir = input('请输入你播放的路径：')
elif m == 'A':
    music_dir ='D:\酷狗音乐下载'#'C:\Users\dengjun\Music\Music'


def getname(music_dir):   #获取音乐名字函数
    music_list = []
    path_dir = os.listdir(music_dir) #列出文件夹下所有的目录与文件
    for i in range(0,len(path_dir)):  
           path = os.path.join(music_dir,path_dir[i])  #
           if os.path.isfile(path):
              file_name = os.path.basename(path)
              (name,ext) = os.path.splitext(file_name)
              music_list.append(name)
    return(music_list)


def play():                         #音乐播放函数
    music_list = getname(music_dir)

    music_name = random.choice(music_list)

    print("\n正在播放 %s" % music_name)

    ctypes.windll.winmm.mciSendStringW(r"open %s\%s.mp3 alias s" % (music_name,music_dir) ,None, 0, None)
    ctypes.windll.winmm.mciSendStringW(r"play s repeat", None, 0, None)

    input("\n按回车键退出......")

if __name__=='__main__':
    play()

