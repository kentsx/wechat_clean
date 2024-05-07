from glob import glob
import hashlib
import os
import send2trash

path = 'D:\\Coding\\WeChat_Clean'

# 遍历所有文件
def get_file_list(path, file_type = '*'):
    lookup_path = path + '/**/*.' + file_type
    file_list = glob(lookup_path,recursive=True)
    return file_list

file_list = get_file_list(path, 'txt')
# print(file_list)


md5_list = []

for file in file_list:

    with open(file, 'rb') as f:
        file_hash = hashlib.md5()
        while chuck := f.read(8192):  # 处理大型文件，避免内存占用
            file_hash.update(chuck)
        file_md5 = file_hash.hexdigest()
    if file_md5 not in md5_list:
        md5_list.append(file_md5)
    else:
        send2trash.send2trash(file)
        print('【已删除】', file)

# 获取所在文件夹

print(md5_list)
