import tkinter as tk
import tkinter.messagebox
import os
from tkinter.filedialog import askdirectory
from main import *

# from download import *

# app基本信息
w = tk.Tk()
ver = '1.0'
# date = datetime.datetime.now().strftime('%Y-%m-%d')
date = "2024-05-07"
app_name = "重复文件清理"


# 窗口设置
w.title('%s v%s，%s编译  by Kent' % (app_name, ver, date))
w.geometry('450x100')
w.resizable(width=False, height=False)


def openDir():
    fileDir = askdirectory()  # 选择目录，返回目录名
    if fileDir.strip() != '':
        dirpath.set(fileDir)  # 设置变量outputpath的值
        
    else:
        # print("do not choose Dir")
        pass



# 选择路径
# def selectPath(path):
# 	path_ = askdirectory() #使用askdirectory()方法返回文件夹的路径
# 	if path_ == "":
# 		path.get() #当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
# 	else:
# 		path_ = path_.replace("/", "\\")  # 实际在代码中执行的路径为“\“ 所以替换一下
# 		path.set(path_)

dirpath = tk.StringVar()

tk.Label(w, text='选择目录：').grid(row=0, column=0,  padx=5, pady=5)
tk.Entry(w, textvariable=dirpath, state='readonly').grid(row=0, column=1, ipadx=80, pady=5)
tk.Button(w, text='打开目录', command=openDir).grid(row=0, column=2, padx=5, pady=5)

def execute():
    path = dirpath.get()
    whole_process(path)
    askback = tkinter.messagebox.askyesno(title='完成', message="""当前文件夹已清理完毕！\n是否继续清理？""")
    if askback == False:
        w.destroy()

tk.Button(w, text = '开始清理', command=execute).grid(row=1, column=1, padx=5, pady=5)

w.mainloop()