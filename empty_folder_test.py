import os

path = 'D:\\Coding\\WeChat_Clean\\test1'

## 各一个文件路径，判断它所在文件夹除此文件外是否还有文件，无文件的删除，且从下往上遍历
def del_empty_folder(file_path):
    for root, dirnames, filenames in os.walk(file_path, topdown=False):
        if os.listdir(root):
            print('有文件')
        else:
            # 删除文件夹
            print('无文件')
            # os.rmdir(root)

del_empty_folder(path)