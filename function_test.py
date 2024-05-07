from glob import glob
import hashlib
import os
import send2trash

path = 'D:\\Coding\\WeChat_Clean\\test1'

# 遍历所有文件
def get_file_list(path, file_type = '*'):
    lookup_path = path + '/**/*.' + file_type
    file_list = glob(lookup_path,recursive=True)
    return file_list


# a = os.listdir(path)
# file_list = get_file_list(path, 'txt')
# print(file_list)

# def get_folder_list(path):
#     lookup_path = path + '/**'
#     folder_list = glob(lookup_path,recursive=True)
#     return folder_list

# a = get_file_list(path)

# print(a)
# 遍历文件夹，从底向上查
for root, dirnames, filenames in os.walk(path, topdown=False):
    if os.listdir(root):
        print('有文件')
    else:
        print('无文件')

# md5_list = []

# for file in file_list:

#     with open(file, 'rb') as f:
#         file_hash = hashlib.md5()
#         dir_path, file_name = os.path.split(file)
#         while chuck := f.read(8192):  # 处理大型文件，避免内存占用
#             file_hash.update(chuck)
#         file_md5 = file_hash.hexdigest()
#     if file_md5 not in md5_list:
#         md5_list.append(file_md5)
#     else:
#         send2trash.send2trash(file)
#         print('【已删除】', file)
#         try:
#             os.rmdir(dir_path)
#             print('【已删除-空文件夹】', dir_path)
#         except:
#             pass

# 获取所在文件夹

# print(md5_list)
